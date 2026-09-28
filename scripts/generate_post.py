import os
import re
import sys
import json
import difflib
from pathlib import Path
from datetime import datetime, timezone, timedelta, date
import anthropic
import opencc

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

MODEL = "claude-sonnet-5"

today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
today_date = date.fromisoformat(today)

TREND_HISTORY_FILE = Path("scripts/github_trend_history.json")
TREND_DISPLAY_DAYS = 14
TREND_KEEP_DAYS = 30

TOPIC_HISTORY_FILE = Path("scripts/topic_history.json")
TOPIC_DISPLAY_DAYS = 4
TOPIC_KEEP_DAYS = 14
FIXED_CATEGORY_TAGS = {"physical-ai", "generative-ai", "ai-agent", "ai-policy"}

# 原始輸出保存位置：主流程呼叫 API 成功後立刻存檔，
# 後續任何檢查或程式失敗，都可以沿用這份輸出重跑，不必再付一次 API 費用
RAW_DIR = Path("raw_output")
RAW_FILE = RAW_DIR / "raw.md"
REUSE_RAW = os.environ.get("REUSE_RAW") == "1"

# 偵測長段未翻譯英文句子（連續60字元以上的英文並以句號/驚嘆號/問號收尾），
# 短的專有名詞、產品名稱（如 OpenAI、Agents API）不會誤判，因為長度不夠
UNTRANSLATED_ENGLISH_PATTERN = re.compile(r'[A-Za-z][A-Za-z0-9\s,\'"-]{60,}[.!?]')
MAX_REPAIR_ATTEMPTS = 2
URL_PATTERN = re.compile(r"https?://[^\s)\]]+")

# 模型輸出偶發的亂碼字元（U+FFFD），可能出現在任何段落
GARBLED_CHAR = "\ufffd"
# 只有亂碼、沒有英文的行，修復後與原文相似度需達此門檻，避免模型順手改寫整行
GARBLED_ONLY_MIN_SIMILARITY = 0.9

converter = opencc.OpenCC('s2twp')


def run_model(user_prompt, max_tokens, use_search=False):
    kwargs = dict(
        model=MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": user_prompt}],
    )
    if use_search:
        kwargs["tools"] = [{"type": "web_search_20250305", "name": "web_search"}]
    with client.messages.stream(**kwargs) as stream:
        for event in stream:
            pass
        return stream.get_final_message()


def extract_markdown(response):
    blocks = response.content
    last_non_text_idx = -1
    for i, block in enumerate(blocks):
        if block.type != "text":
            last_non_text_idx = i
    text = "\n".join(b.text for b in blocks[last_non_text_idx + 1:] if b.type == "text").strip()
    text = re.sub(r"^```[a-zA-Z]*\n|```$", "", text).strip()
    m = re.search(r"^---", text, re.MULTILINE)
    if m:
        text = text[m.start():]
    return text


def get_text(response):
    text = "".join(b.text for b in response.content if b.type == "text").strip()
    text = re.sub(r"^```[a-zA-Z]*\s*|\s*```$", "", text).strip()
    return text


def strip_links(line):
    # 排除 markdown 連結（含英文標題）與網址，只檢查正文
    line = re.sub(r"\[[^\]]*\]\([^)]*\)", "", line)
    line = re.sub(r"https?://\S+", "", line)
    return line


def find_problem_lines(md):
    """回傳 [(行號, {"english": 英文片段或None, "garbled": 是否含亂碼})]
    英文檢查會略過來源連結區塊；亂碼檢查則涵蓋全文（含來源區塊與 front matter）"""
    problems = {}
    in_sources = False
    for i, line in enumerate(md.split("\n")):
        if line.startswith("## "):
            in_sources = line.strip() == "## 來源連結"
        info = {"english": None, "garbled": GARBLED_CHAR in line}
        if not in_sources:
            m = UNTRANSLATED_ENGLISH_PATTERN.search(strip_links(line))
            if m:
                info["english"] = m.group()
        if info["english"] or info["garbled"]:
            problems[i] = info
    return sorted(problems.items())


def repair_problem_lines(md, problems):
    """只把有問題的那幾行送去修復（成本遠低於整篇重跑），其餘內容完全不動"""
    lines = md.split("\n")
    targets = [i for i, _ in problems]
    payload = []
    for n, (i, info) in enumerate(problems):
        issues = []
        if info["english"]:
            issues.append("english")
        if info["garbled"]:
            issues.append("garbled")
        payload.append({"id": n, "issues": issues, "text": lines[i]})

    repair_prompt = """以下 JSON 陣列的每個項目是文章中的一行 Markdown，issues 欄位標示該行的問題：
- english：夾雜未翻譯的英文句子。請把英文句子翻成通順的繁體中文（台灣用語）。
- garbled：含有亂碼字元「\ufffd」。請依上下文推斷原本應該是哪個字並還原；該字可能是被取代，也可能是多出來的，若判斷是多出來的請直接刪除。不要改寫其他任何字。
其餘內容（已是中文的部分、Markdown 符號、連結文字與網址、專有名詞與產品名稱）一字不改。請只回傳 JSON 陣列（每項包含 id 與 text，不需要 issues），不要加任何說明文字或程式碼框。

{payload}""".format(payload=json.dumps(payload, ensure_ascii=False))

    resp = run_model(repair_prompt, 8000)
    print(f"repair usage: {resp.usage}")
    if resp.stop_reason == "max_tokens":
        print("修復回應被截斷，略過本次修復")
        return md, 0

    try:
        data = json.loads(get_text(resp))
        fixed = {int(item["id"]): item["text"] for item in data}
    except (ValueError, KeyError, TypeError) as e:
        print(f"修復結果無法解析：{e}")
        return md, 0

    changed = 0
    for n, (i, info) in enumerate(problems):
        new_line = fixed.get(n)
        if not new_line or new_line == lines[i]:
            continue
        if GARBLED_CHAR in new_line:
            print(f"略過第 {i + 1} 行：修復後仍含亂碼字元")
            continue
        if sorted(URL_PATTERN.findall(new_line)) != sorted(URL_PATTERN.findall(lines[i])):
            print(f"略過第 {i + 1} 行：修復後網址與原文不一致")
            continue
        if info["garbled"] and not info["english"]:
            ratio = difflib.SequenceMatcher(None, lines[i], new_line).ratio()
            if ratio < GARBLED_ONLY_MIN_SIMILARITY:
                print(f"略過第 {i + 1} 行：僅需還原亂碼字元，但修復後改動過大（相似度 {ratio:.2f}）")
                continue
        lines[i] = converter.convert(new_line)
        changed += 1
    return "\n".join(lines), changed


def load_recent(history_file, days):
    if not history_file.exists():
        return []
    with open(history_file, "r", encoding="utf-8") as f:
        records = json.load(f)
    cutoff = today_date - timedelta(days=days)
    items = set()
    for r in records:
        if date.fromisoformat(r["date"]) >= cutoff:
            items.update(r["items"])
    return sorted(items)


def append_history(history_file, items, keep_days):
    records = []
    if history_file.exists():
        with open(history_file, "r", encoding="utf-8") as f:
            records = json.load(f)
    records.append({"date": today, "items": items})
    cutoff = today_date - timedelta(days=keep_days)
    records = [r for r in records if date.fromisoformat(r["date"]) >= cutoff]
    history_file.parent.mkdir(parents=True, exist_ok=True)
    with open(history_file, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def build_prompt():
    recent_repos = load_recent(TREND_HISTORY_FILE, TREND_DISPLAY_DAYS)
    trend_avoid_note = ""
    if recent_repos:
        trend_avoid_note = "過去 {} 天已經介紹過這些專案，這次不要重複選（除非有重大更新新聞，且需特別說明為何值得再次入選）：{}".format(
            TREND_DISPLAY_DAYS, "、".join(recent_repos)
        )

    recent_topics = load_recent(TOPIC_HISTORY_FILE, TOPIC_DISPLAY_DAYS)
    topic_avoid_note = ""
    if recent_topics:
        topic_avoid_note = "以下公司/主題最近{}天已經是文章的新聞主角：{}。今天請優先選擇其他公司/主題作為新聞重點；如果這些公司/主題有重大新進展值得繼續追蹤，可以再次提及，但只能作為次要新聞角度帶過，並且必須明確說明「相較先前報導，這次新進展是什麼」，不能重複講已經講過的舊資訊。".format(
            TOPIC_DISPLAY_DAYS, "、".join(recent_topics)
        )

    return """你是「產業脈動追蹤網站」(tech-pulse) 的每日內容產生器。

【成本控制原則，優先於其他所有指示】
整個內容蒐集階段，搜尋次數合計請控制在8次以內。優先用較少但精準的搜尋涵蓋需求，可以合併關鍵字、一次搜尋涵蓋多個子主題，不需要每個子主題都個別搜尋一次，也不需要為了「確認得更完整」而重複搜尋類似的關鍵字。

【第一步：內容蒐集】
搜尋今天全球科技產業最值得關注的動態，重點涵蓋：
(1) Physical AI/具身智慧/機器人（機器狗、人形機器人）最新進展
(2) 生成式AI/LLM產業動態（新模型發表、募資、併購、晶片/算力相關新聞）
(3) AI Agent與自動化的產業應用案例
(4) AI政策與監管動態（含中美競爭，也包含國內監管/法律行動、平台治理爭議）
每類找1-2篇候選新聞即可，不用求全。{topic_avoid_note}

來源選擇原則：
- 優先採用國際主流媒體（如The Verge、TechCrunch、Bloomberg、Reuters、CNBC、日經等）與台灣本地媒體（如數位時代、科技報橘、iThome），單一地區來源不要超過整體來源的一半
- 避免來源集中在單一國家的內容農場或訂閱聚合平台，優先選有具名記者、有公信力的原始報導
- 報導中國相關新聞時，優先採用國際第三方媒體的報導角度，若引用中國本地媒體或企業官方發布，需保持查證與批判距離，不逕自複述業者自身的宣傳成就

另外搜尋今天實際的 GitHub Trending 頁面（https://github.com/trending，可加上 since=daily 或 since=weekly 參數），找1個真正當前上榜、跟以上四大主題相關的開源專案，找到明顯符合的就停止，不用比較多個候選。只需要用1次額外搜尋確認選中的專案「近期真的有新版本發布、功能更新、或star數在近期明顯增長」，不要重複查證。如果完全找不到任何真正當前上榜且相關的專案，這個段落可以整段省略，不要為了湊數勉強放進不符合條件的專案。{trend_avoid_note}

【第二步：整理成文章】
從第一步蒐集到的候選新聞中，只挑出全部類別加總後最重要的2-3則，實際寫成獨立段落——不用把每個找到的候選都寫進文章，只寫真正最值得關注的2-3則。全文必須用繁體中文台灣用語撰寫，即使引用的新聞來源是英文報導，也必須完整翻譯、改寫成通順的中文，絕對不可以保留任何未翻譯的英文句子或段落直接混雜在中文內文中——單獨的專有名詞、產品名稱、公司名稱可以維持英文原文（例如 OpenAI、Agents API），但完整的英文句子一律要翻譯成中文，這是硬性規則。格式如下（只回傳這份 Markdown，不要加任何說明文字或程式碼框）：

---
title: "<依當日主題下的標題>"
date: {today}T09:00:00+08:00
description: "<30秒重點摘要，40字以內>"
tags: ["<從 physical-ai / generative-ai / ai-agent / ai-policy 挑1-2個，再加1-2個更具體的關鍵字如公司名或技術名詞，全部使用英文小寫、多字詞用連字號連接，例如 unitree、fcc、ai-chip>"]
glossary_term: "<這篇最主要挑的名詞小教室用詞，沒有適合的則留空字串>"
draft: false
---

## 30秒看重點
（條列2-4點）

## <第一則新聞的標題，用問句>
（2-4段敘述，適時用引言框就地嵌入名詞小教室，格式：`> **名詞小教室**：<名詞> ... <白話解釋>`。文中若提到「上週一」「本週三」這類相對時間詞，務必附上具體日期，例如「上週一（2026.08.31）」，不要只寫相對時間詞）

## <第二則新聞的標題，用問句>
（依實際挑選的2-3則重複這個結構，不用涵蓋所有蒐集到的候選，同樣注意相對時間詞需附上具體日期）

## 編輯觀點
（第一人稱短文，講你對這些新聞放在一起看的看法，不要用條列格式。風格要求：
- 口語化、平實，避免生硬的書面語
- 可以善用比喻幫助理解，但每段最多用一個主要比喻，講完就收，不要在同一句/同一段疊加多個比喻
- 可以借用SA、系統整合、接案開發等技術工作圈常見的泛用概念類比（例如demo與量產的落差、技術債、需求變化），但絕對不可以捏造具體的「我曾經...」「我自己看過...」這種第一人稱親身經歷、發言或評論——這是硬性規則
- 長短句混搭，帶有自然的轉折，避免全篇都是同一種節奏
- 避免自我肯定式的俏皮轉折用語（例如「無聊但要命」「看似A其實B」這種帶有『我來點破你』姿態的說法），改用平實沉穩的措辭（例如「經典議題」）
- 避免過度熟絡、鄉民化的語氣，不要像PTT或個人網誌）

## 台灣視角
（這些新聞對台灣供應鏈、法規、產業或本地廠商的意涵，沒有明顯對應角度就不強寫；可以觸及系統整合/專案管理視角的觀察，但同樣不可捏造具體親身經歷）

## 明天值得關注
（一段前瞻性內容）

## 今日 GitHub Trend
（1個相關開源專案，格式：**[專案完整名稱](GitHub連結網址)** — 星數與近期成長幅度，接著1-2句說明為何入選/值得關注。星數與成長數字須來自實際搜尋結果，不要憑空估計。若無符合條件的專案則整段省略）

## 常見問題 FAQ

### <問題1>
<回答>

### <問題2>
<回答>

## 來源連結
- [標題](網址)

---

> 這份快報由 AI 根據上方引用來源整理，每日 08:00 自動發佈。
""".format(today=today, topic_avoid_note=topic_avoid_note, trend_avoid_note=trend_avoid_note)


def main():
    if REUSE_RAW:
        if not RAW_FILE.exists():
            print("錯誤：指定沿用先前輸出，但找不到 raw_output/raw.md")
            sys.exit(1)
        raw_markdown = RAW_FILE.read_text(encoding="utf-8")
        print(f"沿用先前的原始輸出（{len(raw_markdown)} 字元），不呼叫 API")
    else:
        response = run_model(build_prompt(), 24000, use_search=True)

        print(f"stop_reason: {response.stop_reason}")
        print(f"usage: {response.usage}")
        print(f"content block types: {[block.type for block in response.content]}")

        if response.stop_reason == "max_tokens":
            print("錯誤：回應在 max_tokens 被截斷，內容不完整，不寫入檔案")
            sys.exit(1)

        raw_markdown = extract_markdown(response)
        if raw_markdown:
            RAW_DIR.mkdir(parents=True, exist_ok=True)
            RAW_FILE.write_text(raw_markdown, encoding="utf-8")
            print("已保存原始輸出到 raw_output/raw.md（後續檢查失敗時可沿用，不用再付 API 費用）")

    markdown = converter.convert(raw_markdown)

    if not markdown:
        print("錯誤：沒有抓到任何文字內容，不寫入檔案")
        sys.exit(1)

    # 偵測到未翻譯英文或亂碼字元時，只把有問題的那幾行送去修復，不重跑整個流程
    for attempt in range(1, MAX_REPAIR_ATTEMPTS + 1):
        problems = find_problem_lines(markdown)
        if not problems:
            break
        print(f"偵測到 {len(problems)} 行有問題，進行第 {attempt} 次修復")
        for i, info in problems:
            detail = []
            if info["english"]:
                detail.append("未翻譯英文：" + info["english"][:60])
            if info["garbled"]:
                detail.append("含亂碼字元")
            print(f"  - 第 {i + 1} 行：{'；'.join(detail)}")
        markdown, changed = repair_problem_lines(markdown, problems)
        if changed == 0:
            print("修復沒有任何變更，停止重試")
            break

    remaining_english = [(i, info) for i, info in find_problem_lines(markdown) if info["english"]]
    if remaining_english:
        i, info = remaining_english[0]
        print(f"錯誤：修復後仍偵測到未翻譯英文，不寫入檔案。第 {i + 1} 行：{info['english'][:80]}")
        sys.exit(1)

    # 亂碼無法自動還原時不擋下文章，移除該字元並在 Actions 摘要留下警告，提醒人工確認
    if GARBLED_CHAR in markdown:
        count = markdown.count(GARBLED_CHAR)
        markdown = markdown.replace(GARBLED_CHAR, "")
        print(f"::warning::仍有 {count} 個亂碼字元無法自動還原，已移除，請人工確認文章內容")

    trend_match = re.search(r"## 今日 GitHub Trend\n(.*?)(?=\n## |\Z)", markdown, re.DOTALL)
    if trend_match:
        mentioned_repos = sorted(set(re.findall(r"github\.com/([\w.\-]+/[\w.\-]+)", trend_match.group(1))))
        if mentioned_repos:
            append_history(TREND_HISTORY_FILE, mentioned_repos, TREND_KEEP_DAYS)
            print(f"記錄本次 GitHub Trend 選中：{', '.join(mentioned_repos)}")
    else:
        print("提示：本次文章沒有 GitHub Trend 段落（可能是找不到符合條件的專案），未更新歷史紀錄")

    tags_match = re.search(r'tags:\s*\[(.*?)\]', markdown)
    if tags_match:
        raw_tags = [t.strip().strip('"').strip("'") for t in tags_match.group(1).split(",")]
        specific_topics = [t for t in raw_tags if t and t.lower() not in FIXED_CATEGORY_TAGS]
        if specific_topics:
            append_history(TOPIC_HISTORY_FILE, specific_topics, TOPIC_KEEP_DAYS)
            print(f"記錄本次新聞主題：{', '.join(specific_topics)}")
    else:
        print("警告：找不到 tags 欄位，本次未更新主題歷史紀錄")

    # 檔名日期以文章 front matter 的 date 為準（沿用先前輸出、隔天才補跑時，日期才不會錯亂）
    post_date = today
    date_match = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", markdown, re.MULTILINE)
    if date_match:
        post_date = date_match.group(1)

    filename = f"content/posts/{post_date}-daily-digest.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"寫入完成：{filename}（{len(markdown)} 字元）")


if __name__ == "__main__":
    main()