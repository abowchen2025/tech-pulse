---
title: "人形機器人IPO狂潮、GLM-5.3延後開源、AI Agent能不能真的賺錢？"
date: 2026-08-31T09:00:00+08:00
description: "Unitree暴漲近500%、FCC禁機器人進口卻買機器狗、GLM-5.3延遲開源、企業AI Agent的真實ROI"
tags: ["physical-ai", "ai-policy", "unitree", "fcc"]
glossary_term: "FCC Covered List"
draft: false
---

## 30秒看重點
- 中國人形機器人龍頭Unitree（宇樹科技）在上海科創板掛牌首日暴漲近500%，市值一度衝上600億美元，凸顯中美在具身智慧賽道的資本熱度差異。
- 美國FCC禁止新款外國製人形機器人與機器狗進口，但同一時間國土安全部卻打算花200萬美元採購美製波士頓動力SPOT機器狗用於移民執法，政策矛盾浮現。
- Z.ai的GLM-5.3把開源權重延後兩週釋出，理由是模型意外具備強大的資安攻防能力，凸顯中國開源模型「先快速迭代、後補安全審查」的新模式。
- 企業匯入AI Agent的真實投報率浮出水面：JPMorgan、Salesforce等案例顯示效益確實存在，但Gartner也警告市場上大量「agent washing」灌水案例。

## Unitree首日暴漲近500%，人形機器人IPO為何意義非凡？
中國人形機器人指標廠商Unitree Robotics（宇樹科技）於8月19日在上海科創板掛牌，
股價在上海交易首日暴漲460%，公司透過首次公開發行募得人民幣61億元（約9.04億美元），成為中國大陸首家掛牌的人形機器人製造商
。
股價一度盤中衝高近630%，最終收在845元人民幣
，
收盤市值約達500億美元
。值得一提的是，
這次IPO的投資人名單中包括中國AI公司深度求索（DeepSeek），出資約1.408億元人民幣，騰訊則是既有投資人
，顯示中國AI與機器人產業鏈的資本連動已相當緊密。

這波熱潮並非單一事件。就在Unitree掛牌前後，
中國於8月19日在北京開幕2026世界機器人大會，主辦單位表示這五天展期將展出約3000項產品，各企業藉此展現中國持續擴張的機器人產業，目標是把技術從展示推向工廠等真實應用場景
。不過現場也顯露出技術落差：
有攤位讓機器人嘗試摺一件襯衫這種看似簡單的家務，結果試了好幾分鐘還是摺不好
，說明「能表演」與「能幹活」之間仍有明顯距離。

> **名詞小教室**：STAR Market（科創板） 是上海證券交易所專門提供給科技創新企業掛牌的板塊，類似臺灣的創新板，門檻較寬鬆但波動也常更劇烈，Unitree這類尚未大規模獲利的硬體新創也能藉此籌資。

## 一邊禁機器人進口、一邊採購機器狗抓人？美國政策的矛盾在哪？
美國聯邦通訊委員會（FCC）在7月底出手，
於7月27日禁止進口新款外國製人形機器人、四足機器狗與電力變流器，理由是國家安全風險
。
FCC委員Brendan Carr表示，遵循川普總統的領導方向，FCC將持續盡一份力來保護美國關鍵供應鏈，這次的行動也是配合國安機關的判斷
。這項禁令並非全面封殺——
全球人形機器人市場中國約佔85%的份額，2025年全球出貨量約1.5萬臺，Unitree與AgiBot兩家中國廠商合計就佔了逾5000臺
，禁令實際上是不核發新機型的裝置認證，
已取得認證的既有機型仍可繼續進口、行銷與販售
。
廠商仍可向國防部申請「有條件核准」的例外許可
。

耐人尋味的是，就在FCC剛築起這道牆的同時，美國移民及海關執法局（ICE）卻反向採購外國名稱聽起來相反、但其實是美系機器狗的裝備。
ICE計畫編列最多200萬美元預算，採購波士頓動力製造的四足機器狗SPOT協助移民執法行動，相關訊息來自國土安全部公佈的採購規劃系統檔案
。
國土安全部一名高層官員向NBC News證實這項計畫，並說明這些機器人不會被用來執行逮捕任務
。
SPOT配備360度攝影機與感測器，可偵測震動、氣體與輻射，並具備可伸縮機械臂，但不具備如警犬般的攻擊能力
。這一來一往顯示，美國對「外國機器人」的疑慮其實高度聚焦在中國供應鏈，而非機器人這項技術本身。

> **名詞小教室**：FCC Covered List（受管制清單） 是美國聯邦通訊委員會列出「不得核發裝置認證」的產品清單，最初用來針對華為等電信裝置商，如今擴大納入人形機器人與機器狗，等於變相築起產業准入的高牆。

## 為什麼Z.ai要把GLM-5.3的開源權重延後兩週才放出？
中國AI實驗室Z.ai（前身為智譜AI）在8月14日發布新款開源模型GLM-5.3，主打程式碼與代理任務能力。
GLM-5.3沿用與GLM-5.2相同的743B引數基礎模型，所有能力提升都來自擴大後訓練規模——包括更多工環境與更長的訓練時間，在最長時程的Terminal-Bench 3.0測試上，分數從4.6大幅躍升至28.3
。但真正引人注意的是一個意外副作用：
模型的資安能力進步幅度超出Z.ai原本預期，CyberGym漏洞探測測試達到84.5%的成績
，
目前僅透過Z.ai自家API、GLM Coding Plan與ZCode平臺提供服務，開源權重尚未釋出，官方表示會在安全評估與強化措施完成後、約發布兩週後才釋出權重
。

這個「先評測資安風險、再決定是否開源」的做法後來也真的兌現：
截至8月28日，GLM-5.3的開源權重已在Hugging Face上（zai-org/GLM-5.3）正式釋出，經過兩週的安全審查後，Z.ai將其稱為「我們在代理式程式設計與網路防禦上最強大的模型」
。對比GLM-5.2當初幾乎是發布API的同一週就同步開源，
這次GLM-5.3採取分階段釋出，正是因為Z.ai公開承認這款模型發展出超出預期的攻擊性資安能力，是GLM系列首次因安全考量而延後開源的版本
。

## 8月AI基礎建設狂潮：晶片、資料中心募資為何再創新高？
如果說今年AI投資的關鍵字是「軟體」，8月的資金流向已經明顯轉向硬體。
單月統計顯示，Databricks的50億美元策略輪、Firmus的20億美元募資、Castelion的10億美元C輪，加上Etched的7億美元增資，四筆交易合計就讓AI基礎建設與相鄰重資本領域在8月單月吸金87億美元
。其中最大手筆是
Databricks以1900億美元估值完成的50億美元策略輪募資，投資人包括Coatue、Blackstone、MGX與T. Rowe Price，這筆交易就佔了當月基礎建設資金的57%；另外原本是比特幣礦商的Firmus則從Blackstone、Coatue與Nvidia處募得20億美元，用於在亞太地區興建AI資料中心，估值達105億美元
。

這股資金浪潮也延伸到晶片新創本身：
AI晶片與半導體新創在2026年迄今已募得約41.6億美元的揭露資金，最大單筆交易來自Etched，其7月完成的3億美元C輪讓公司估值達到103億美元，據TechCrunch報導
。整體而言，
創投巨頭Andreessen Horowitz也將旗下最新一檔專注於「AI實體骨幹」的基金規模定案在11億美元，命名為Machine Age Fund，鎖定晶片、記憶體、網路硬體與儲存系統，以及資料中心、機器人與聯網家電等領域
，顯示資本市場的敘事正從「哪個模型最聰明」轉向「誰能撐起運算與電力的底層供應鏈」。

## 企業匯入AI Agent真的划算嗎？從JPMorgan到Salesforce怎麼算這筆帳
2026年的企業AI落地故事，已經從概念驗證走向真金白銀的財務數字。金融業龍頭的案例最具代表性：
JPMorgan的LLM Suite平臺每天服務20萬名員工，支援超過450項生產中的AI應用場景，背後是180億美元的年度技術預算
，
450個應用場景背後的教訓是：規模來自許多小型、受治理控管的應用，而不是單一個巨型代理系統
。在開發者生產力方面，
多鄰國（Duolingo）讓旗下300多名工程師使用GitHub Copilot，在陌生程式庫中的開發速度提升了25%、資深工程師也有10%提升，搭配Slack整合後把程式碼審查平均耗時從3小時砍到1小時，降幅達67%
。

另一個常被引用的案例來自Salesforce：
Salesforce用自家Agentforce平臺透過合約自動化省下約500萬美元法務成本，對外的Agentforce則已累積8000多個付費客戶、AI與Data Cloud年度經常性收入達約9億美元，像Saks Fifth Avenue這類客戶能在10天內完成上線
。跨行業調查也顯示，
企業匯入代理式AI平均能拿到171%的投報率，美國企業平均更達192%，是傳統自動化與RPA的三倍左右，各職能部門的代理系統平均約5.1個月就能回本
。

不過這波熱潮也伴隨警訊。
Gartner估計，市面上自稱是代理式AI公司的廠商中，只有約130家真正符合其對「真實代理能力」的認定標準，其餘的多數則被Gartner稱為「agent washing」（代理灌水）
。換句話說，掛上「AI Agent」招牌不代表真的具備自主規劃、執行與修正的能力，企業在評估匯入前仍須自行查證。

> **名詞小教室**：Agent Washing（代理灌水） 指廠商把傳統自動化工具或簡單聊天機器人重新包裝、貼上「AI Agent」標籤來行銷，但實際上並不具備自主判斷、多步驟執行與修正錯誤的能力。

## 歐盟AI法案透明度新規正式上路，對聊天機器人與深偽內容有何要求？
歐盟《人工智慧法案》（AI Act）的下一個重要生效日已經到來。
自8月2日起，歐盟執委會AI辦公室聯手各國主管機關開始執行AI法案，新的透明度規則也同步上路，要求特定AI系統告知使用者他們正在與AI互動、或內容是由AI生成或修改而成
。具體而言，
聊天機器人與其他互動式AI系統必須告知使用者他們面對的是AI而非真人，深偽內容（經AI編輯或生成的影像、影片或音訊）必須加註標示，AI生成或修改的內容也必須帶有機器可判讀的浮水印，以便更容易被偵測
。若企業未能遵守，
最高可面臨1500萬歐元或全球年營業額3%（以較高者為準）的罰款
。

值得注意的是，歐盟同時也對法案本身的時程做了鬆綁：
原本預定8月2日生效的高風險AI系統規則，經協商後延後適用，獨立型高風險AI系統改為2027年12月2日生效，內嵌於產品中的高風險AI系統則延到2028年8月2日
。這代表歐盟目前是「先抓透明度標示、高風險認證晚點來」的分階段執行策略，企業不能因為高風險規則延後就忽略眼前已經上路的透明度義務。

## 美國會把晶片出口管制擴大到「雲端算力」嗎？中國繞道問題浮上檯面
美中在AI晶片領域的攻防持續升級，這次戰場延伸到了「雲端」。
根據《福布斯》8月29日報導，美國政府正考慮進一步收緊對中國的人工智慧技術限制，把現行以實體晶片為主的出口管制延伸至海外資料中心與雲端運算服務，試圖堵住中國企業透過第三國遠端租用先進GPU算力的管道
。這項訊息最早由《The Information》披露，
報導引述4名知情人士指出，美國商務部內部一個小組近幾週正在制定新的晶片出口規定，重點鎖定一個日益受華府關注的漏洞：中國AI企業即便無法直接進口最先進的Nvidia晶片，仍可能透過泰國、新加坡等國的資料中心遠端呼叫這些晶片來訓練模型
。

如果新規最終定案，這代表美國出口管制的邏輯出現重大轉折——
監管物件不再只是「晶片運到哪裡」，還可能進一步追蹤「誰在使用這些晶片的算力」，即使晶片實體上留在境外
。這也呼應川普政府先前的政策軌跡：
川普總統第二任期開始後，美國政府一度撤回拜登時期制定的《AI擴散框架》，商務部工業與安全域性2025年5月宣佈不執行該規定，但後續明確表示會制定關於「安全出口先進AI晶片」的新規則，2026年也已調整部分對華半導體政策，讓Nvidia H200、AMD MI325X等晶片改為滿足安全條件後逐案審查出口許可
。對臺灣的雲端服務業者與晶片供應鏈而言，若規則延伸到雲端算力層級，勢必得重新盤點自家客戶名單與資料中心的地緣曝險。

## 編輯觀點
把這一週的新聞攤開來看，最有意思的不是任何單一事件，而是「矛盾感」本身。美國一邊用FCC禁令把中國機器人擋在門外，一邊自己的移民執法單位卻在採購同型別的機器狗；一邊高喊晶片出口管制，一邊還在煩惱中國企業透過第三國雲端繞道使用算力，管制的邊界永遠追不上技術與資本流動的速度。中國那邊也不是鐵板一塊——Z.ai寧願延後兩週開源GLM-5.3，就是因為連自己人都被模型意外冒出的資安攻擊能力嚇到，這說明「開源、快速迭代」的策略也開始碰到安全這道現實的牆。至於企業AI Agent的落地情況，我認為JPMorgan和Salesforce的案例值得參考，但Gartner那句「agent washing」的警告更值得放大檢視——當投資人和媒體都在追逐代理式AI的敘事時，能不能先分清楚哪些是真正解決問題的系統、哪些只是換了個名詞的舊自動化，可能比追新模型分數更重要。

## 明天值得關注
接下來幾天可以留意兩條主線的後續發展：一是美國商務部針對「雲端算力出口管制」的內部草案是否會正式對外公佈細節，這將牽動包括新加坡、泰國在內的亞太資料中心業者，以及間接受影響的臺灣雲端服務供應鏈；二是中國人形機器人陣營的下一步動作，包括BYD首款人形機器人在「迪空間」的正式亮相時程，以及Unitree掛牌後續是否有更多中國機器人廠商跟進赴滬深、港股掛牌的效應。此外，GLM-5.3開源權重釋出後，開發者社群對其資安能力的實際測試結果，也將是觀察中國開源模型下一步走向的重要指標。

## 今日 GitHub Trend
**[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)** — 累計星數已成長至約6萬顆（今年6月中旬約3.5萬、7月初約5萬），持續出現在GitHub每日/每週熱門榜單上。這是一款可跨平臺安裝於Claude Code、Codex、Cursor、Gemini CLI等多種AI Agent環境的「技能」（Skill），能同時檢索Reddit、X、YouTube、Hacker News、Polymarket等來源，彙整成一份附引用來源的近30天趨勢摘要，反映當前AI Agent生態系「技能化」（Agent Skills）正在取代單純聊天機器人的走向，值得關注其作為AI Agent基礎設施的代表性案例。

## 常見問題 FAQ

### FCC禁止外國機器人進口，代表現有的Unitree機型也不能在美國買了嗎？
不是。這項禁令
只針對尚未取得FCC裝置認證的「新機型」，已經取得認證的既有機型仍可繼續合法進口、行銷與販售
，消費者手上已購買的機型也能持續使用與更新韌體。

### GLM-5.3現在可以下載開源權重了嗎？
可以。雖然Z.ai在8月14日發布時表示要延後兩週才釋出權重，但
截至8月28日，GLM-5.3的開源權重已在Hugging Face上正式釋出
，經歷了為期兩週的安全評估與強化程式。

### 企業匯入AI Agent的投資報酬率真的有171%這麼高嗎？
這個171%的數字來自業界調查機構的統計，
但這是「已經成功匯入」的企業樣本平均值，並非所有嘗試匯入AI Agent的企業都能達到
。考量到
Gartner估計市場上僅約130家廠商真正符合代理式AI的能力門檻
，企業在評估時仍須自行驗證供應商的實際技術能力，而非只看行銷數字。

## 來源連結
- [Unitree Robotics Surges 460% After $904 Million Shanghai IPO - Bloomberg](https://www.bloomberg.com/news/articles/2026-08-18/unitree-robotics-set-to-debut-after-904-million-shanghai-ipo)
- [China's backflipping robot maker Unitree pops 542% in Shanghai debut - CNBC](https://www.cnbc.com/2026/08/19/china-backflipping-robot-maker-unitree-jumps-shanghai-ipo.html)
- [From robot dogs to helpers, China puts robotics ambitions on display at world conference - Washington Times](https://www.washingtontimes.com/news/2026/aug/19/robot-dogs-helpers-china-puts-robotics-ambitions-display-world/)
- [In the Doghouse: FCC Bans New Foreign-Made Humanoid, Quadruped Robots - ASIS International](https://www.asisonline.org/security-management-magazine/latest-news/today-in-security/2026/august/FCC-Bans-Humanoid-Quadruped-Robots/)
- [FCC bans imports of foreign-made humanoid robots - Quartz](https://qz.com/fcc-bans-foreign-humanoid-robot-imports-national-security-072926)
- [ICE explores purchasing robot dogs in enforcement tech push - Fortune](https://fortune.com/2026/08/29/ice-contract-robot-dogs-trump-immigration-crackdown-deportation/)
- [Z.ai Ships GLM-5.3 Without Retraining the Base Model - MarkTechPost](https://www.marktechpost.com/2026/08/14/z-ai-ships-glm-5-3-without-retraining-the-base-model-better-at-complex-coding-and-long-horizon-tasks/)
- [GLM-5.3 Launch: Benchmarks, Pricing & Access (Aug 2026) - explainx.ai](https://www.explainx.ai/blog/glm-5-3-launch-cyber-defense-benchmarks-august-2026)
- [GLM-5.3: Z.ai Coding Model, Benchmarks & Weights - Eigent.ai](https://www.eigent.ai/blog/glm-5-3-coding-cyber-model)
- [AI infrastructure funding August 2026: $8.7B tracker - Value Add Pulse](https://valueaddvc.com/pulse/pulse-analysis-ai-infrastructure-funding-8-7-billion-2026)
- [AI chip startups raise $4.16B in 2026 funding rounds - Value Add Pulse](https://valueaddvc.com/pulse/ai-chip-startup-funding-4-16-billion-2026)
- [August 2026 Startup News Recap - TodaysStartupNews](https://www.todaysstartupnews.com/news/august-2026-startup-funding-acquisitions-recap)
- [7 enterprise AI agent use cases in production (2026) - ecorpit](https://ecorpit.com/enterprise-ai-agents-production-use-cases-2026/)
- [Enterprise AI Agent Adoption in 2026: Stats, ROI & Case Studies - Trixly AI](https://www.trixlyai.com/blogs/enterprise-ai-agent-adoption-in-2026-stats-roi-case-studies)
- [Commission starts enforcing AI Act rules and new transparency requirements on 2 August - European Commission](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [EU AI Act: Transparency Obligations Take Effect 2 August 2026 - Cooley](https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026)
- [Artificial Intelligence: Council gives final green light to simplify and streamline rules - Consilium](https://www.consilium.europa.eu/en/press/press-releases/2026/06/29/artificial-intelligence-council-gives-final-green-light-to-simplify-and-streamline-rules/)
- [美擬封堵中國海外AI算力 管制或延伸至「雲端」- 看中國新聞網](https://www.secretchina.com/news/b5/2026/08/30/1104154.html)

---

> 這份快報由 AI 根據上方引用來源整理，每日 08:00 自動釋出。