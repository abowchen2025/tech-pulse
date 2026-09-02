# Tech Pulse 產業脈動快報

每日自動更新的科技產業新聞快報靜態網站，追蹤 Physical AI、生成式 AI/LLM、AI Agent、AI 政策與監管四大領域的最新動態，支援個人 Physical AI 學習計畫的產業前瞻追蹤需求。

🔗 **網站**：https://abowchen2025.github.io/tech-pulse/

## 技術架構

- **靜態網站產生器**：[Hugo](https://gohugo.io/)（extended 版本）+ [PaperMod](https://github.com/adityatelange/hugo-PaperMod) 主題
- **部署**：GitHub Pages，透過 GitHub Actions 自動 build
- **內容產生**：Anthropic API（Claude Sonnet 5，含 web search 工具）
- **排程觸發**：外部 cron-job.org 每日呼叫 GitHub Actions API（`workflow_dispatch`），避開 GitHub 免費方案內建排程不穩定的問題
- **簡繁轉換**：OpenCC（`s2twp`）

## 運作流程

1. 每日固定時間，cron-job.org 觸發 `daily-post.yml`
2. `scripts/generate_post.py` 呼叫 Anthropic API，搜尋當日科技新聞並整理成符合站內格式的 Markdown 文章
3. 自動 commit 新文章到 `content/posts/`
4. 觸發 Hugo build + 部署到 GitHub Pages

## 本機開發

```bash
hugo server -D
```

## 內容說明

文章內容由 AI 根據當日搜尋結果自動整理產生，包含新聞摘要、名詞解釋、編輯觀點、GitHub 開源趨勢等段落，每篇文末皆附上原始新聞來源連結。

---

個人學習支援專案，非商業用途。