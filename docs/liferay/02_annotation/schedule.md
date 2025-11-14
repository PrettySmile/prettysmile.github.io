---
title: '@Schedule'
parent: 註解
---

# @Schedule


## 🧩 整體概念：OSGi Component Lifecycle
在 OSGi 中，每個 @Component 都是獨立的模組。

當系統啟動或 bundle 被安裝時，OSGi 會：

1. 啟動 (Activate) → 建立元件實例、注入依賴（@Reference）  
2. 修改 (Modified) → 當設定檔（Configuration Admin）更新時觸發  
3. 停用 (Deactivate) → 元件卸載、bundle 停止、或系統關閉時觸發  

|  | 時機 | 作用 |
| ---- | ---- | ------ |
| doReceive(Message message) | scheduler 被觸發時執行的主要邏輯。 |  |
| @Activate | - 元件被第一次啟動時（例如 Liferay 啟動、模組被部署）。 <br> - 所有 @Reference 相依服務都注入完成之後執行。 | 通常用來做「初始化」： <br><br> - 設定 Scheduler <br> - 建立預設資料 <br> - 開啟定時任務 <br> - 註冊事件 Listener |
| @Modified | - 當元件的設定（properties）在運行中被修改時觸發。 <br> - 例如在 Liferay System Settings 或 Config Admin Console 改變設定。 <br><br> 不會重新建立物件，而是「重用同一個實例」去更新設定。 | 可用來「熱更新」元件設定，例如： <br><br> - 改變排程時間（cron expression）<br> - 重新註冊新的 scheduler <br> - 改變內部變數或外部服務連線資訊 |
| @Deactivate | - 當元件被停用、卸載、或伺服器關閉時。 <br> - 所有相依服務（@Reference）都將被解除綁定。 | - 用來釋放資源、清理狀態、取消註冊。 <br> - 如果不釋放，Liferay Scheduler 可能仍會嘗試呼叫已不存在的 listener。 |