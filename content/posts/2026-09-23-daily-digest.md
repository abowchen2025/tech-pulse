---
title: "Grok 4.7降臨、Salesforce AIforce搶進企業入口，機器人跨國角力仍未落幕"
date: 2026-09-23T09:00:00+08:00
description: "xAI推出Grok 4.7、Salesforce端出AIforce搶攻企業AI介面，美國機器人禁令效應仍在發酵"
tags: ["generative-ai", "ai-agent", "ai-policy", "grok"]
glossary_term: "FCC涵蓋清單（Covered List）"
draft: false
---

## 30秒看重點

- xAI於上週一（2026.09.21）推出Grok 4.7，引數量較前代大增四成，主打程式撰寫與高強度推理任務，且首波即開放API與Cursor等平臺使用。
- Salesforce在Dreamforce 2026大會端出全新介面層「AIforce」，讓Salesforce的資料與工作流程能直接嵌入Claude、Slack等外部AI工具，企業匯入agent的門檻再降一階。
- 美國FCC自今年7月底起將外國製人形機器人與機器狗列入「涵蓋清單」，禁止新機型取得進口許可，Unitree等中國廠商的既有機型不受影響，但新品進不了美國市場的僵局仍未解除。

## Grok 4.7降臨，能為AI競賽帶來什麼新意？

Elon Musk旗下的xAI在上週一（2026.09.21）正式推出新一代旗艦模型Grok 4.7。
這次發表在美東時間下午稍晚公佈，Grok 4.7的引數量來到2.1兆，較前一代Grok 4.6的1.5兆增加四成
，
xAI形容這是「在同樣的價格與速度下，相較Grok 4.6有顯著進步」的最新旗艦模型
。值得玩味的是，
這次發表前Musk至少五度將時程往後延，從最初宣稱「四週後」一路拖到「還需要幾天打磨」
，讓外界對xAI的產品節奏一直帶著半信半疑的態度。

規格之外，這次更新也把重心放在「思考深度」上。
xAI表示新模型會花更長時間處理困難問題，並比Grok 4.6更頻繁地自我檢查答案，同時強調這是他們目前為止防護機制最完善的一次
。定價則維持不變，
每百萬輸入token收費2美元、輸出token收費6美元
，等於是用同樣的價格換取更強的效能。上線方式也很直接，
這次沒有候補名單，Grok 4.7即刻在Grok App、Cursor、Grok Build與xAI API同步開放
。

> **名詞小教室**：引數量（Parameters）。可以想成模型大腦裡的「旋鈕」數量，旋鈕愈多，理論上能記住、拆解的模式就愈複雜，但不代表實際表現一定等比例變好，還要看訓練資料與訓練方法夠不夠扎實。

在跑分表現上，
Grok 4.7在專門測試長時間程式任務的CursorBench 4.0拿下46.3%，優於前代的40.4%；在DeepSWE v1.1高強度測試也從65.2%進步到71.0%
。不過放到整個競技場來看，
xAI自己公佈的七項基準測試顯示，Grok 4.7雖然全面超越Grok 4.6、也贏過GPT-5.6 Sol Max四項，但在CursorBench、Terminal-Bench等指標上仍落後Anthropic的Fable 5.1 Max
，說明這場模型競賽仍然沒有絕對贏家，比的是誰在特定任務上更划算。

## Salesforce用AIforce重新定義企業AI介面，意味著什麼？

上上週二至週四（2026.09.15–09.17），
Salesforce一年一度的Dreamforce大會在舊金山Moscone Center登場
，這次的重頭戲是全新介面層「AIforce」。
AIforce讓Salesforce的資料、工作流程與許可權可以直接嵌入Claude、Slack等外部AI工具中使用，同一場發表還包含Salesforce首個CRM推理模型Koa、Salesforce in Claude全面進入beta，以及Agentforce Coworker正式對所有客戶開放
。

這個佈局背後的邏輯,其實是把過去一年陸續推出的拼圖湊在一起。
Salesforce先前推出的Slackbot讓使用者能透過提示詞跨系統下指令，接著上線的Headless 360則把Salesforce的能力開放給第三方agent介面使用
，AIforce算是把這些線串成一張完整的網。執行長Marc Benioff把這個轉向定調為使用者不再需要透過傳統畫面操作，而是讓AI直接讀懂並執行企業內部的資料與規則。

真正值得關注的是採用數字。
Salesforce表示Salesforce in Claude已經過Deloitte、GitLab、Legora等客戶試用後進入全客戶beta，而Agentforce Coworker上線35天內就衝到10萬名啟用使用者，Fulton Bank更在短短數週內從零建置出橫跨約3,000名員工、20多個上線場景的應用
。這些數字說明企業匯入AI agent，已經從概念驗證階段真正走向規模化部署。

> **名詞小教室**：介面層（Interface Layer）。簡單說就是把後端龐大複雜的資料與規則，包裝成一層讓AI工具能「看得懂、用得動」的橋樑，使用者不用再學習企業系統原本的操作邏輯。

## 美國祭出機器人「涵蓋清單」，對中國機器人供應鏈意味著什麼？

這是一則時序稍早、但效應持續延燒的政策動態。
美國聯邦通訊委員會（FCC）在今年7月28日更新其「涵蓋清單」，新增「先進機器人裝置」這個類別，定義為人形機器人、四足機器狗等移動式機器人，凡是外國製造的相關產品都被納入
。
這項規定禁止新的外國製人形、四足或其他移動式機器人型號取得在美國進口、行銷或銷售所需的裝置核准
。

> **FCC涵蓋清單（Covered List）**：美國政府認定「對國家安全構成不可接受風險」的通訊與科技裝置清單，一旦被列入，新產品就很難拿到在美國合法銷售所需的許可證，等於是把新品擋在門外，但不會強制回收已經在市面上流通的舊產品。

值得注意的是，這項規定並非全面封殺。
凡是在2026年7月27日以前已經取得FCC裝置核准的機型都不受影響，例如Unitree的G1、R1、H2、Go2與A2全數過關，只要是在禁令生效前核准的產品都能繼續合法進口、銷售與使用
。真正卡關的是還沒申請過認證的新機型，
除非由美國戰爭部（Department of War）核發「有條件核准」，否則新品或先前未經授權的機型都無法取得裝置核准
。而截至今年8月初，
美國戰爭部尚未核發任何一件有條件核准，也沒有任何一家廠商公開遞出申請
，等於這扇「後門」目前形同虛設。

FCC提出的理由並非空穴來風。
公告中特別引用了2025年9月一起針對Unitree機器人的資安漏洞事件，攻擊者能藉此接管機器人並掃描鄰近裝置，引發外界對「人形機器人殭屍網路」的疑慮
。與此同時，中國機器人廠商的資本市場動作卻毫無減速跡象——
Unitree已在8月19日完成中國大陸首宗純機器人業務的上海科創板掛牌，股價掛牌後大漲，反映其上半年出貨量與後續目標的市場信心
。一邊是美國築起的進口高牆，一邊是中國廠商在資本市場高歌猛進，這場拉鋸短期內看不到收尾的跡象。

## 編輯觀點

把這三則新聞放在一起看，其實可以看到同一個主題的三種切面：模型端在拚引數與跑分、應用端在拚企業匯入的規模、政策端則在拚供應鏈的控制權。Grok 4.7的故事很典型，跳票五次終於上線，這種「demo很炫、交付一直延」的節奏，做過專案的人應該都不陌生，需求沒變，但時程一直在滑動，最後端出來的東西通常比預期晚,但也不會差太多。

Salesforce這次的AIforce反而讓我比較在意的是「介面」這個詞本身的份量。過去談企業AI,焦點多半放在模型能力夠不夠強,但AIforce想解決的其實是另一個更務實的問題:資料、許可權、流程這些「地基」夠不夠穩,能不能讓外部的AI工具安全地接進來用。這比拚模型分數務實得多,也更貼近實際匯入時真正卡關的地方——很多agent專案卡住,往往不是模型不夠聰明,而是許可權、資料治理這些基本功沒做好。

至於FCC的機器人禁令,拉長時間看反而更耐人尋味。政策工具的目的是想擋住新機型進入美國市場,但既有機型完全不受影響,等於是在存量市場上開了一個大洞。這種「新品卡關、舊品照跑」的設計,某種程度上跟很多產業的法規調整很像——規則永遠是為了未來設計的,但市場的既有格局已經先跑在前面了。

## 臺灣視角

FCC這項規定對臺灣供應鏈最直接的意涵,在於機器人零元件（致動器、感測器、控制晶片）的認證與供貨佈局。當美國對「外國製造」機器人設下裝置核准的高牆,臺灣廠商若能切入這些機型的關鍵零元件供應,或協助美系品牌完成在地化生產,反而可能是轉單效應的受益者;但若既有客戶名單裡有仰賴中國品牌出貨美國的環節,則需要提前評估認證卡關的風險。

另一方面,Salesforce AIforce這類「企業AI介面層」的興起,對臺灣的系統整合與接案開發生態也有實務意涵。過去SI業者的價值多半在客製化串接與流程開發，如果企業客戶未來能直接透過Claude、Slack這類工具存取後端系統，中間層的整合工作量勢必會被壓縮，SI業者可能需要更早思考如何往「治理、許可權設計」這類更高附加價值的服務轉型，而不是單純比拚串接速度。

## 明天值得關注

接下來值得留意的，是美國戰爭部是否會在近期核發第一件機器人「有條件核准」——一旦開了先例，後續會有多少廠商跟進申請、又會設下哪些附加條件，將決定這道禁令實際上是「暫時卡關」還是「長期封鎖」。此外，隨著Grok 4.7與Salesforce AIforce相繼上線，接下來幾週市場的焦點可能會轉向：企業客戶實際匯入後,這些新工具究竟能不能兌現發表會上的承諾,還是又淪為叫好不叫座的展示品。

## 常見問題 FAQ

### Grok 4.7跟其他前沿模型比起來真的比較強嗎？
不一定全面領先。xAI公佈的跑分顯示Grok 4.7在多數指標上超越自家前代與部分對手，但在程式撰寫、長情境任務等專案上，Anthropic的Fable 5.1 Max仍略勝一籌，選擇哪個模型更多要看實際任務型別與成本考量。

### FCC的機器人禁令等於全面禁止Unitree等中國機器人在美國銷售嗎？
不是。這項規定只封鎖「新」或「先前未經授權」的外國製機型申請裝置核准，在禁令生效（2026年7月28日）之前已取得核准的既有機型仍可合法進口、銷售與使用，屬於「擋新不擋舊」的設計。

## 來源連結
- [xAI Launches Grok 4.7. It's Bigger, But Late to the AI Frontier Party](https://tech.yahoo.com/ai/gemini/articles/xai-launches-grok-4-7-171603280.html)
- [xAI Launches Grok 4.7, Its Most Capable Coding Model Yet](https://sqmagazine.co.uk/xai-launches-grok-4-7-coding-model/)
- [Salesforce Launches AIforce at Dreamforce '26: 'AI Replaces the UI'](https://www.salesforceben.com/salesforce-launches-aiforce-at-dreamforce-26-ai-replaces-the-ui/)
- [AIforce: Salesforce's Big Dreamforce 2026 Announcement](https://www.concret.io/blog/salesforce-aiforce-dreamforce-2026)
- [FCC Adds Foreign-Produced Advanced Robotic Devices to the Covered List](https://www.sidley.com/en/insights/newsupdates/2026/08/fcc-adds-all-foreign-produced-advanced-robotic-devices-to-the-covered-list)
- [FACT SHEET: FCC Updates Covered List to Include Foreign-Produced Advanced Robotic Devices](https://docs.fcc.gov/public/attachments/DOC-423682A1.pdf)
- [Humanoid Robots Legal in the US: What You Can Still Buy](https://blog.robozaps.com/b/humanoid-robots-legal-in-us)
- [Dongfeng to trial-produce humanoid robots by year-end](https://cnevpost.com/2026/09/20/dongfeng-trial-produce-humanoid-robots-year-end/)

---

> 這份快報由 AI 根據上方引用來源整理，每日 08:00 自動釋出。