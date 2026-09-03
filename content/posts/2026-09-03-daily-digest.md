---
title: "Nvidia砸重金繫結聯發科、Cisco全員配AI助理，還有歐盟開始真罰款了"
date: 2026-09-03T09:00:00+08:00
description: "Nvidia投資聯發科35億美元卡位客製晶片，Cisco讓9萬員工人手一個AI Agent，歐盟AI法開始開罰。"
tags: ["generative-ai", "ai-agent", "nvidia", "eu-ai-act"]
glossary_term: "NVLink Fusion"
draft: false
---

## 30秒看重點
- Nvidia宣佈投資聯發科35億美元購買可轉換公司債，換來聯發科匯入NVLink Fusion技術打造客製AI晶片，合作範圍橫跨雲端、PC與車用三大領域
- Cisco把自研AI助理「MyAgent」推廣到全公司近9萬名員工，強呼叫「便宜的模型做簡單的事」而非每次都動用最貴的前沿模型
- 歐盟AI法（EU AI Act）今年第一季就開出50張罰單、總額2.5億歐元，顯示這部法規已經從紙上規範進入實際執法階段
- 三則新聞放在一起看，反映的是同一件事：AI產業正從「秀技術」轉向「算成本、扛責任」的務實階段

## Nvidia為什麼要砸35億美元投資聯發科？


2026年8月31日，Nvidia和聯發科大幅擴充套件合作關係，Nvidia投資35億美元購買聯發科可轉換公司債，臺灣晶片設計公司則計畫採用NVLink Fusion作為打造客製AI加速器的基礎
，而
這筆投資金額也獲得路透社獨立證實
。這不是單純的財務入股，
NVLink Fusion讓客戶有了打造客製加速器晶片的基礎，整合NVLink連線技術、高頻寬記憶體、先進封裝與機櫃級整合，讓工程資源可以專注在差異化運算本身
。

> **名詞小教室**：NVLink Fusion，簡單說就是Nvidia把自家用來串接GPU、CPU、記憶體的高速連線技術「開放」給第三方晶片使用。原本這條高速公路只給Nvidia自己的晶片跑，現在其他公司設計的客製AI晶片（業界簡稱XPU）也能上這條路，直接接進Nvidia的資料中心生態系，不用重新蓋一條路。

值得玩味的是雙方合作範圍：
這筆投資將以可轉換為聯發科股份的債券形式進行，作為聯發科在資料中心自研客製AI晶片野心的一部分，未來會採用NVLink Fusion與新宣佈的NVHBM技術
，而目標市場不小——
聯發科的目標是在明年估計800億美元的資料中心晶片市場中拿下多達15%的份額，並預期今年AI晶片營收約20億美元
。

放在更大脈絡看，這其實延續了Nvidia近年的一貫打法。
這筆交易凸顯了Nvidia近幾年融資策略的迴圈性質，這家晶片巨頭經常投資那些最終會迴流到自家生態系的公司
，而且不只這一樁——
上週Nvidia才剛宣佈與AWS的類似合作（雖然沒有直接投資），AWS將在基礎設施中額外部署200萬顆Nvidia GPU，同時整合NVLink Fusion
。換句話說，當愈來愈多大型客戶想自己設計晶片，Nvidia選擇的策略不是硬碰硬阻止，而是想辦法讓「自己設計晶片」這件事也離不開Nvidia的基礎設施。

## Cisco讓9萬名員工人手一個AI Agent，這代表什麼？

企業匯入AI Agent的討論已經吵了兩年多，但大多停留在小規模試點。Cisco這次動作不小：
Cisco執行副總裁Thimaya Subaiya宣佈將自研AI助理MyAgent推廣到全公司9萬名員工，這套系統建立在Cisco安全、受治理、多模型通用的AI平臺Circuit之上，讓員工能存取經核准的大型語言模型、代理人與企業資料
。功能面上，
MyAgent能在Outlook、Webex、Jira、SharePoint等應用程式中執行受監督的自主工作流程，讓員工只需設定目標，系統就能協調完成所需步驟並跨系統串連
。

比起「全員配一個AI助理」這個headline數字，真正值得留意的是背後的設計邏輯。
Cisco這套系統的架構不會每個任務都預設呼叫最強大的前沿模型：簡單的公司政策查詢會導向輕量模型，複雜的財務分析則會轉給能力更強的模型，且大部分基礎設施跑在自家機房內，讓Cisco能直接掌控成本與資料安全
。這種「先算成本再談能力」的做法，跟多數企業「先用最好的模型，帳單問題以後再說」的預設心態正好相反。

> **名詞小教室**：模型路由（Model Routing），指的是系統依照任務難度自動挑選要呼叫哪一顆AI模型，而不是每次都用最貴、最強的那顆。原理有點像叫車軟體依照距離配車：短程用經濟型，長途才配大車，避免每趟都叫最貴的車。

實際效益上，
Cisco財務長Mark Patterson表示，公司財務部門目前已經有80%到90%的公開監理檔案MD&A章節初稿由AI完成，原本分析師需要花上數天的工作，現在幾分鐘就能產出草稿，人力則轉為審閱與修改
。這代表AI Agent的價值不再只是聊天機器人式的問答，而是真的接手了具體的文書產出流程。

## 歐盟AI法真的開始開罰了，代表監管進入「有牙齒」階段？

如果說前兩則新聞是產業端的攻防，這一則則是規則制定者出手的訊號。
目前全球已有超過75個國家正在積極制定或追蹤AI立法
，而歐盟走得最前面。
歐盟AI法自2025年2月起分階段實施，其餘大部分條文已於2026年8月2日生效，這個日期涵蓋了多數高風險AI義務，適用於招聘、信貸、教育、關鍵基礎設施與執法等領域的系統
。

更關鍵的是，這不再只是紙上規範。
單是2026年第一季，歐盟成員國就開出了50張罰單，總額達2.5億歐元，主要針對通用型AI（GPAI）不合規行為，其中愛爾蘭因為是多數科技公司歐洲總部所在地，就處理了六成案件
。

相較之下，美國的路線明顯不同。
美國目前沒有一部全面性的聯邦AI法律，有的只是一份框架檔案、一系列行政命令，以及在選舉年裡爭論不休的政治環境
。而中國則走另一條路——
中國的AI監管方式結合積極推動AI發展與針對AI生成內容、演演算法推薦、合成媒體的特定規則，法規要求AI系統必須符合「社會主義核心價值觀」，並強制要求向監管機構提供演演算法透明度
。三種路線放在一起看，正好是當前AI地緣政治的縮影：歐盟選擇強監管換信任，美國選擇鬆綁換速度，中國則是監管與扶植並行、服務於國家戰略目標。

## 編輯觀點

把這三則新聞擺在一起看，我覺得有個共同的主題正在浮現：AI產業正在從「能不能做到」進入「劃不划算、誰來負責」的階段。Nvidia砸錢繫結聯發科，聽起來像是財大氣粗的收購式操作，但骨子裡其實是一種防禦性佈局——當愈來愈多大客戶想自己設計晶片，與其硬擋，不如把自己變成所有人都繞不開的那條高速公路。這跟接案圈子裡常見的「先卡住基礎架構，客製化需求再怎麼變化，都要走你的管線」邏輯，其實有點像。

Cisco的案例則讓我想到系統整合常遇到的老問題：demo跟量產永遠是兩回事。把AI助理發給9萬人用很容易變成一場公關秀，但Cisco特別強調的成本路由設計，反而透露出他們是真的把這當一個要長期維運的系統在做，而不是做完發布會就結束的展示品。這種務實的態度，在AI agent一片喧囂的宣傳聲量裡其實不常見。

至於歐盟的開罰數字，我覺得比起「歐盟又立新法」這種老調重彈的敘事更值得注意——2.5億歐元的罰款代表這部法規真的開始長出牙齒了。經典議題又浮上檯面：當監管開始有實質約束力，接下來考驗的就是各家公司的合規團隊夠不夠快跟上腳步，還是繼續把AI治理當成公關文案來寫。

## 明天值得關注

隨著聯發科與Nvidia的合作細節逐步公開，接下來值得留意的是有沒有具體的產品時程或客戶名單浮出檯面——目前雙方都還沒鬆口任何確切的產品代號或上市時間，這會是判斷這樁合作究竟是長期佈局還是短期媒體效應的關鍵。另外，Cisco這類大規模企業級AI Agent部署案例如果持續增加，企業對「代理人治理」（agent governance）的需求也可能跟著升溫，值得觀察是否有更多資安或治理框架廠商趁勢推出對應方案。

## 常見問題 FAQ

### NVLink Fusion跟Nvidia自家GPU有什麼差別？
NVLink Fusion本身不是一顆晶片，而是一套連線技術規格。它讓其他公司設計的客製AI加速器（XPU）能用高速方式接進Nvidia的機櫃與資料中心繫統，等於是把原本封閉的「Nvidia專屬高速公路」部分開放給第三方晶片使用，但運算核心本身仍由客戶或聯發科這類夥伴自行設計。

### Cisco的MyAgent會不會取代員工的工作？
從目前揭露的設計來看，MyAgent走的是「受監督的自主工作流程」模式，也就是員工設定目標、系統協調執行步驟，但仍保留人在迴圈中審核的機制，例如財務部門的檔案草稿仍需人力審閱修改。目前公開資訊尚未提及以此大規模裁減人力的計畫。

## 來源連結
- [Nvidia’s $3.5B MediaTek bet reveals its plan for tackling Big Tech's AI chip buildout](https://techcrunch.com/2026/08/31/nvidias-3-5b-mediatek-bet-reveals-its-plan-for-tackling-big-techs-ai-chip-buildout/)
- [Qualcomm rival MediaTek jumps 10% after $3.5 billion Nvidia AI chip deal](https://www.cnbc.com/2026/09/01/nvidia-deal-mediatek-shares.html)
- [Nvidia Invests $3.5 Billion in MediaTek](https://www.theglobeandmail.com/investing/markets/stocks/NVDA/pressreleases/4363866/nvidia-invests-35-billion-in-mediatek/)
- [Cisco Deploys Custom AI Agent to Entire 90,000-Person Workforce](https://www.pymnts.com/news/artificial-intelligence/2026/cisco-deploys-custom-ai-agent-to-entire-90000-person-workforce)
- [Cisco's AI Agent Rollout: 90000 Employees, One Playbook](https://enterprisedna.co/resources/news/cisco-ai-agents-90000-employees-enterprise-playbook-2026/)
- [AI Regulation News Today: The US, EU, UK, Japan, and China Frameworks Reshaping the Industry in 2026](https://theaiforest.com/ai-regulation-news-2026-us-eu-global-updates/)
- [AI Regulation in 2026: Comparing US, EU, and China Policy Approaches](https://qverlabs.com/blog/ai-regulation-2026-us-eu-china-policy)

---

> 這份快報由 AI 根據上方引用來源整理，每日 08:00 自動釋出。