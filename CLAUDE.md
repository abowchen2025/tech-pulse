# CLAUDE.md

本檔案提供 Claude Code 在這個 repo 工作時需要的專案脈絡。完整規劃背景（目標、範圍決策、與 Oscar 的關聯）見 Claude.ai「Physical AI 學習計畫」project 的《Side Project 規劃：產業脈動追蹤網站》文件，這裡只放跟寫程式直接相關的規範。

## 專案概述

每日自動更新的科技產業新聞快報靜態網站，繁體中文台灣用語。讀者：ABow 本人，支援 Physical AI 學習計畫的產業前瞻追蹤需求。MVP 階段，不做搜尋、社群分享、FAQ 結構化資料、相關文章推薦、贊助連結。

## 技術架構

- 靜態網站產生器：Hugo
- 部署：GitHub Pages
- 內容格式：Markdown + Hugo front matter

## 目錄慣例

```
content/posts/YYYY-MM-DD-slug.md      每日新聞文章
content/posts/glossary-{term}.md      獨立名詞解釋文章（若某詞值得獨立成篇）
```

slug 用英文小寫連字號，例如 `2026-08-25-generative-ai-funding-shift`。

## 文章 Front Matter 欄位規範

```yaml
title: string
date: YYYY-MM-DDTHH:MM:SS+08:00
summary: string        # 30秒重點摘要，作為列表頁與 SEO description
tags: [string]          # 對應四大類：physical-ai / generative-ai / ai-agent / us-china-tech
glossary_term: string   # 這篇挑的名詞小教室用詞，沒有則留空
```

## 內容結構（每篇文章內文順序）

1. 30 秒重點摘要
2. 主要新聞內容（依當日蒐集的新聞分段，各段標明來源）
3. 名詞小教室（挑一個生疏專有名詞，白話解釋）
4. 潛在意涵——視新聞內容涵蓋以下角度，沒有對應角度不強寫：
   - 對台灣營建業/智慧工地的應用意涵
   - SA 視角重點（系統整合、資料流設計、需求變化的啟示）
   - PM 視角重點（專案管理、資源調度、風險層面的啟示）
5. 來源連結列表

## 名詞解釋頁

用 Hugo 標籤（tag）功能聚合，不另外開發獨立頁面。有 `glossary_term` 的文章自動出現在對應標籤頁。

## 開發指令

（第一次建站後由 `hugo new site` 產生，待補上實際指令：本地預覽、build、部署腳本）

## 待確認事項

- Hugo 主題：尚未選定，骨架站階段先挑一個免費主題
- 每日自動化：Cowork Scheduled Task 產生內容後如何寫入 `content/posts/` 並觸發 build+部署，串接方式待第一次實作時確認
