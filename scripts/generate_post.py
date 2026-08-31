import os
import re
import sys
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta, date
import anthropic
import opencc

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
today_date = date.fromisoformat(today)

TREND_HISTORY_FILE = Path("scripts/github_trend_history.json")
TREND_DISPLAY_DAYS = 14
TREND_KEEP_DAYS = 30

TOPIC_HISTORY_FILE = Path("scripts/topic_history.json")
TOPIC_DISPLAY_DAYS = 4
TOPIC_KEEP_DAYS = 14
FIXED_CATEGORY_TAGS = {"physical-ai", "generative-ai", "ai-agent", "ai-policy"}


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

prompt = """你是「產業脈動追蹤網站」(tech-pulse) 的每日內容產生器。

【第一步：內容蒐集】
搜尋今天全球科技產業最值得關注的動態，重點涵蓋：
(1) Physical AI/具身智慧/機器人（機器狗、人形機器人）最新進展
(2) 生成式AI/LLM產業動態（新模型發表、募資、併購、晶片/算力相關新聞）
(3) AI Agent與自動化的產業應用案例
(4) AI政策與監管動態（含中美競爭，也包含國內監管/法律行動、平台治理爭議）
每類找2-4篇當天或近3天內的新聞。{topic_avoid_note}

來源選擇原則：
- 優先採用國際主流媒體（如The Verge、TechCrunch、Bloomberg、Reuters、CNBC、日經等）與台灣本地媒體（如數位時代、科技報橘、iThome），單一地區來源不要超過整體來源的一半
- 避免來源集中在單一國家的內容農場或訂閱聚合平台，優先選有具名記者、有公信力的原始報導
- 報導中國相關新聞時，優先採用國際第三方媒體的報導角度，若引用中國本地媒體或企業官方發布，需保持查證與批判距離，不逕自複述業者自身的宣傳成就

另外搜尋今天實際的 GitHub Trending 頁面（https://github.com/trending，可加上 since=daily 或 since=weekly 參數），找出真正當前上榜、跟以上四大主題相關的開源專案。務必實際查證每個候選專案「近期是否有新版本發布、功能更新、或star數在近期明顯增長」，不要只憑專案知名度或印象挑選——例如專案本身很有名但近期沒有新動態，就不符合「trending」的定義，不該入選。如果查證後只找到1個真正符合的專案，就只列1個；如果完全找不到任何真正當前上榜且相關的專案，這個段落可以整段省略，不要為了湊數勉強放進不符合條件的專案。{trend_avoid_note}

【第二步：整理成文章】
用繁體中文台灣用語，整理成一篇 Markdown 文章，格式如下（只回傳這份 Markdown，不要加任何說明文字或程式碼框）：

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
（2-4段敘述，適時用引言框就地嵌入名詞小教室，格式：`> **名詞小教室**：<名詞> ... <白話解釋>`）

## <第二則新聞的標題，用問句>
（同上，依實際蒐集到的新聞數量重複）

## 編輯觀點
（第一人稱短文，講你對這些新聞放在一起看的看法，不要用條列格式。風格要求：
- 口語化、平實，避免生硬的書面語
- 可以善用比喻幫助理解，但每段最多用一個主要比喻，講完就收，不要在同一句/同一段疊加多個比喻
- 可以借用SA、系統整合、接案開發等技術工作圈常見的泛用概念類比（例如demo與量產的落差、技術債、需求變化），但絕對不可以捏造具體的「我曾經...」「我自己看過...」這種第一人稱親身經歷、發言或評論——這是硬性規則
- 長短句混搭，帶有自然的轉折，避免全篇都是同一種節奏
- 避免自我肯定式的俏皮轉折用語（例如「無聊但要命」「看似A其實B」這種帶有『我來點破你』姿態的說法），改用平實沉穩的措辭（例如「經典議題」）
- 避免過度熟絡、鄉民化的語氣，不要像PTT或個人網誌）

## 明天值得關注
（一段前瞻性內容）

## 今日 GitHub Trend
（2-3個相關開源專案，每個項目格式：**[專案完整名稱](GitHub連結網址)** — 星數與近期成長幅度，接著1-2句說明為何入選/值得關注。星數與成長數字須來自實際搜尋結果，不要憑空估計）

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

with client.messages.stream(
    model="claude-sonnet-5",
    max_tokens=24000,
    tools=[{"type": "web_search_20250305", "name": "web_search"}],
    messages=[{"role": "user", "content": prompt}],
) as stream:
    for event in stream:
        pass
    response = stream.get_final_message()

print(f"stop_reason: {response.stop_reason}")
print(f"content block types: {[block.type for block in response.content]}")

if response.stop_reason == "max_tokens":
    print("錯誤：回應在 max_tokens 被截斷，內容不完整，不寫入檔案")
    sys.exit(1)

content_blocks = response.content
last_non_text_idx = -1
for i, block in enumerate(content_blocks):
    if block.type != "text":
        last_non_text_idx = i

text_blocks = [block.text for block in content_blocks[last_non_text_idx + 1:] if block.type == "text"]
markdown = "\n".join(text_blocks).strip()
markdown = re.sub(r"^```[a-zA-Z]*\n|```$", "", markdown).strip()

match = re.search(r"^---", markdown, re.MULTILINE)
if match:
    markdown = markdown[match.start():]

converter = opencc.OpenCC('s2twp')
markdown = converter.convert(markdown)

if not markdown:
    print("錯誤：沒有抓到任何文字內容，不寫入檔案")
    sys.exit(1)

trend_match = re.search(r"## 今日 GitHub Trend\n(.*?)(?=\n## |\Z)", markdown, re.DOTALL)
if trend_match:
    mentioned_repos = sorted(set(re.findall(r"github\.com/([\w.\-]+/[\w.\-]+)", trend_match.group(1))))
    if mentioned_repos:
        append_history(TREND_HISTORY_FILE, mentioned_repos, TREND_KEEP_DAYS)
        print(f"記錄本次 GitHub Trend 選中：{', '.join(mentioned_repos)}")
else:
    print("警告：找不到「今日 GitHub Trend」段落，本次未更新歷史紀錄")

tags_match = re.search(r'tags:\s*\[(.*?)\]', markdown)
if tags_match:
    raw_tags = [t.strip().strip('"').strip("'") for t in tags_match.group(1).split(",")]
    specific_topics = [t for t in raw_tags if t and t.lower() not in FIXED_CATEGORY_TAGS]
    if specific_topics:
        append_history(TOPIC_HISTORY_FILE, specific_topics, TOPIC_KEEP_DAYS)
        print(f"記錄本次新聞主題：{', '.join(specific_topics)}")
else:
    print("警告：找不到 tags 欄位，本次未更新主題歷史紀錄")

filename = f"content/posts/{today}-daily-digest.md"
with open(filename, "w", encoding="utf-8") as f:
    f.write(markdown)

print(f"寫入完成：{filename}（{len(markdown)} 字元）")