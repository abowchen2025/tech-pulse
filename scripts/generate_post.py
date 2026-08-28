import os
import re
import sys
from datetime import datetime, timezone, timedelta
import anthropic
import opencc

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")

prompt = """你是「產業脈動追蹤網站」(tech-pulse) 的每日內容產生器。

【第一步：內容蒐集】
搜尋今天全球科技產業最值得關注的動態，重點涵蓋：
(1) Physical AI/具身智慧/機器人（機器狗、人形機器人）最新進展
(2) 生成式AI/LLM產業動態（新模型發表、募資、併購、晶片/算力相關新聞）
(3) AI Agent與自動化的產業應用案例
(4) AI政策與監管動態（含中美競爭，也包含國內監管/法律行動、平台治理爭議）
每類找2-4篇當天或近3天內的新聞。

來源選擇原則：
- 優先採用國際主流媒體（如The Verge、TechCrunch、Bloomberg、Reuters、CNBC、日經等）與台灣本地媒體（如數位時代、科技報橘、iThome），單一地區來源不要超過整體來源的一半
- 避免來源集中在單一國家的內容農場或訂閱聚合平台，優先選有具名記者、有公信力的原始報導
- 報導中國相關新聞時，優先採用國際第三方媒體的報導角度，若引用中國本地媒體或企業官方發布，需保持查證與批判距離，不逕自複述業者自身的宣傳成就

另外搜尋近期 GitHub Trending 上，跟以上四大主題相關的熱門開源專案，挑2-3個。

【第二步：整理成文章】
用繁體中文台灣用語，整理成一篇 Markdown 文章，格式如下（只回傳這份 Markdown，不要加任何說明文字或程式碼框）：

---
title: "<依當日主題下的標題>"
date: {today}T09:00:00+08:00
description: "<30秒重點摘要，40字以內>"
tags: ["<從 physical-ai / generative-ai / ai-agent / ai-policy 挑1-2個，再加1-2個更具體的關鍵字如公司名或技術名詞>"]
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
（第一人稱短文，講你對這些新聞放在一起看的看法，不要用條列格式）

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
""".format(today=today)

response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=24000,
    tools=[{"type": "web_search_20250305", "name": "web_search"}],
    messages=[{"role": "user", "content": prompt}],
)

print(f"stop_reason: {response.stop_reason}")

if response.stop_reason == "max_tokens":
    print("錯誤：回應在 max_tokens 被截斷，內容不完整，不寫入檔案")
    sys.exit(1)
print(f"content block types: {[block.type for block in response.content]}")

content_blocks = response.content
last_non_text_idx = -1
for i, block in enumerate(content_blocks):
    if block.type != "text":
        last_non_text_idx = i

# 只取最後一段連續的文字內容（真正的文章本體），排除中途夾帶的旁白句子
text_blocks = [block.text for block in content_blocks[last_non_text_idx + 1:] if block.type == "text"]
markdown = "\n".join(text_blocks).strip()
markdown = re.sub(r"^```[a-zA-Z]*\n|```$", "", markdown).strip()

# 保險機制：就算旁白混進了最終文字區塊裡，也強制從第一個 --- 開始截取
match = re.search(r"^---", markdown, re.MULTILINE)
if match:
    markdown = markdown[match.start():]

converter = opencc.OpenCC('s2twp')  # 簡體轉台灣繁體，含用詞轉換
markdown = converter.convert(markdown)

if not markdown:
    print("錯誤：沒有抓到任何文字內容，不寫入檔案")
    sys.exit(1)

filename = f"content/posts/{today}-daily-digest.md"
with open(filename, "w", encoding="utf-8") as f:
    f.write(markdown)

print(f"寫入完成：{filename}（{len(markdown)} 字元）")