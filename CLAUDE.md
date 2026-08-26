# CLAUDE.md

本檔案提供 Claude Code 在這個 repo 工作時需要的專案脈絡。完整規劃背景（目標、範圍決策、與 Oscar 的關聯）見 Claude.ai「Physical AI 學習計畫」project 的《Side Project 規劃：產業脈動追蹤網站》文件，這裡只放跟寫程式直接相關的規範。

## 專案概述

每日自動更新的科技產業新聞快報靜態網站，繁體中文台灣用語。讀者：ABow 本人，支援 Physical AI 學習計畫的產業前瞻追蹤需求。MVP 階段，不做搜尋、社群分享、FAQ 結構化資料、相關文章推薦、贊助連結。

## 技術架構

- 靜態網站產生器：Hugo（extended 版本，主題需要 Sass 編譯）
- 主題：PaperMod（git submodule）
- 部署：GitHub Pages（透過 GitHub Actions 自動 build + 部署，`public/` 不進版控）

## 目錄慣例

content/posts/YYYY-MM-DD-slug.md 每日新聞文章
content/posts/glossary-{term}.md 獨立名詞解釋文章（若某詞值得獨立成篇）


slug 用英文小寫連字號，例如 `2026-08-25-generative-ai-funding-shift`。

## 文章 Front Matter 欄位規範

```yaml
title: string
date: YYYY-MM-DDTHH:MM:SS+08:00
description: string    # 30秒重點摘要，對應 PaperMod 原生欄位，同時作為列表頁摘要與 SEO description
tags: [string]          # 對應四大類：physical-ai / generative-ai / ai-agent / us-china-tech
glossary_term: string   # 這篇挑的名詞小教室用詞，沒有則留空
```

> 欄位命名對齊 PaperMod 主題慣例，使用 `description` 而非自訂的 `summary`，避免列表頁摘要需要額外客製模板才能顯示。

## 內容結構（每篇文章內文順序）

1. 30 秒重點摘要
2. 主要新聞內容（依當日蒐集的新聞分段，各段標明來源）
3. 名詞小教室（挑一個生疏專有名詞，白話解釋）
4. 潛在意涵——視新聞內容涵蓋以下角度，沒有對應角度不強寫：
   - 對台灣營建業/智慧工地的應用意涵
   - SA 視角重點（系統整合、資料流設計、需求變化的啟示）
   - PM 視角重點（專案管理、資源調度、風險層面的啟示）
5. 來源連結列表

文章樣板存放於 `archetypes/posts.md`，執行 `hugo new posts/xxx.md` 會自動帶出上述五段落骨架與對應 front matter。

## 全站連結設定

`layouts/_default/_markup/render-link.html` 已設定全站連結自動加上 `target="_blank" rel="noopener noreferrer"`，來源連結會自動開新分頁，內文撰寫時不需額外加 HTML 標籤。

## 名詞解釋頁

用 Hugo 標籤（tag）功能聚合，不另外開發獨立頁面。有 `glossary_term` 的文章自動出現在對應標籤頁（`hugo.toml` 內 `[taxonomies]` 已設定 `glossary = 'glossary_term'`）。

## 開發指令

```powershell
hugo new posts/YYYY-MM-DD-slug.md   # 建立新文章（套用 archetypes/posts.md 樣板）
hugo server -D                       # 本機預覽，含草稿
hugo --minify                        # 正式 build（本機測試用，實際部署由 GitHub Actions 執行）
```

## 待確認事項

- 每日自動化：Cowork Scheduled Task 產生內容後如何寫入 `content/posts/` 並觸發 build+部署，串接方式待 Phase 3 實作時確認