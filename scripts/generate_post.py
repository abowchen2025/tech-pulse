import os
import re
import sys
from datetime import datetime, timezone, timedelta
import anthropic

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")

prompt = """你是「產業脈動追蹤網站」(tech-pulse) 的每日內容產生器。

【第一步：內容蒐集】
搜尋今天全球科技產業最值得關注的動態，重點涵蓋：
(1) Physical AI/具身智慧/機器人（機器狗、人形機器人）最新進展
(2) 生成式AI/LLM產業動態（新模型發表、募資、併購、晶片/算力相關新聞）
(3) AI Agent與自動化的產業應用案例
(4) 中美科技競爭/政策動態
每類找2-4篇當天或近3天內的新聞。

【第二步：整理成文章】
用繁體中文台灣用語，整理成一篇 Markdown 文章，格式如下（只回傳這份 Markdown，不要加任何說明文字或程式碼框）：

---
title: "<依當日主題下的標題>"
date: {today}T09:00:00+08:00
description: "<30秒重點摘要，40字以內>"
tags: ["<從 physical-ai / generative-ai / ai-agent / us-china-tech 挑最相關的1-2個>"]
glossary_term: "<這篇挑的名詞小教室用詞，沒有適合的則留空字串>"
draft: false
---

## 30秒重點摘要
## 主要新聞內容
## 名詞小教室
## 潛在意涵
（視新聞內容涵蓋以下角度，沒有對應角度不強寫）
- 對台灣營建業/智慧工地的應用意涵：
- SA 視角重點：
- PM 視角重點：
## 來源連結
""".format(today=today)

response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=8000,
    tools=[{"type": "web_search_20250305", "name": "web_search"}],
    messages=[{"role": "user", "content": prompt}],
)

# 除錯資訊：印出結束原因跟各內容區塊類型，方便之後排查
print(f"stop_reason: {response.stop_reason}")
print(f"content block types: {[block.type for block in response.content]}")

text_blocks = [block.text for block in response.content if block.type == "text"]
markdown = "\n".join(text_blocks).strip()
markdown = re.sub(r"^```[a-zA-Z]*\n|```$", "", markdown).strip()

if not markdown:
    print("錯誤：沒有抓到任何文字內容，不寫入檔案")
    sys.exit(1)

filename = f"content/posts/{today}-daily-digest.md"
with open(filename, "w", encoding="utf-8") as f:
    f.write(markdown)

print(f"寫入完成：{filename}（{len(markdown)} 字元）")