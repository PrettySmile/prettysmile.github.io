---
title: Liferay Portal + Tomcat?
parent: Basic 教學
nav_order: 2
---

# Liferay Portal + Tomcat?


## 1. Liferay Portal 是什麼？

- Liferay Portal 是一個 企業級的內容管理系統 (CMS) + 入口網站 (Portal) 平台。  
- 它可以讓公司快速建立 企業官網、內部知識庫、員工入口網站、客戶服務平台 等。  
- Liferay 本身是一個 Java 應用程式，所以需要一個 Java Application Server 來運行。  


## 2. Tomcat 是什麼？

- Apache Tomcat 是一個 輕量級 Java Web Application Server，能跑 Java Servlet 與 JSP。  
- Liferay 官方提供的「bundle」通常是 Liferay Portal + Tomcat 打包好的版本。  
- 這樣你下載回去後，解壓縮就能直接啟動，不用自己再去安裝 Tomcat 再部署 Liferay war。  


## 3. 為什麼需要下載 Liferay Portal Tomcat bundle？
你需要它的原因有幾個可能：

1. 啟動 Liferay 本地環境
    - 你要在自己電腦上跑 Liferay，就需要下載 bundle，裡面已經整合了 Tomcat。 
    - 啟動後你可以在瀏覽器進入 http://localhost:8080 使用 Liferay Portal。    
2. 開發或測試專案
    - 如果公司/專案要開發 Liferay module、portlet 或整合功能，本地必須有一個 Liferay Portal 運行環境。 
3. 快速體驗 Liferay
    - 下載 bundle 就能跑起 demo，不用額外設定太多。 


## ✅ 簡單來說：

- Liferay Portal = 平台本體  
- Tomcat = 跑 Liferay 的伺服器  
- Liferay Portal Tomcat bundle = 官方打包好的「一解壓就能跑的」版本，方便開發與測試
