---
title: 介紹
parent: Basic 教學
nav_order: 1
---

> Liferay 本身是 Java 應用程式。

## Liferay Portal 版本類型
這是程式碼運行的地方，由 Liferay 官方提供，是 Liferay Portal + Tomcat 打包好的版本，在此統稱為 <span class="bg-yellow-000">Liferay Portal</span> 。

| 版本     | 官方名稱     | 說明               |
| -------- | ----------- | ------------------ |
| 商業版    | Liferay DXP | 付費企業版，含完整功能與官方支援 |
| 免費開源版 | Liferay Portal CE | 社群版 / Community Edition <br> 只包含核心功能 |

<br>

## 開發方式
1. 專案：Liferay Workspace (官方推薦的 Source Code 框架)。 
2. 運行環境：Liferay Portal CE。
    > 此處選擇免費開源版。<br>
    > 啟動後可以在瀏覽器進入 ```http://localhost:8080``` 使用。    
3. IDE 工具：
    - Liferay Developer Studio：以 Eclipse 為基底，加上 Liferay 官方所設計的一些針對開發 Liferay 功能的一套開發工具。
    - Visual Studio Code：一套通用的開發工具。
    > 此處選擇 Visual Studio Code，因為較輕量且啟動速度快。

<br>

## 💡 Liferay Portal 是什麼？
- 一個 <span class="bg-yellow-000">企業級的內容管理系統 (CMS) + 入口網站 (Portal)</span> 平台。  
- 它可以讓公司快速建立 企業官網、內部知識庫、員工入口網站、客戶服務平台 等。  

<br>

## 💡 Tomcat 是什麼？
- Apache Tomcat 是一個 <span class="bg-yellow-000">輕量級 Java Web Application Server</span>。  

<br>

## 💡 Liferay Workspace 是什麼？
- Liferay 官方建議的專案開發結構。
- 用來統一管理與開發 Liferay 模組（modules）、主題（themes）、佈署設定（configs）。
- 主要是基於 Gradle 來建立與管理的。

### 詳細說明：

1. 統一專案結構
    - modules/：放你的 OSGi 模組（Portlet、Service、API 等）。  
    - themes/：放 Liferay 前端主題。  
    - configs/：不同環境的設定檔（開發 dev、測試 uat、正式 prod）。  
2. Gradle
    - 提供 task 來建立模組、部署、啟動伺服器。 
    - 例如：gradlew build、gradlew deploy。       

<br>

## 💡 Liferay Developer Studio (以前叫 Liferay IDE)
- 其實就是 Eclipse 的 Liferay 客製化版本。  
- Developer Studio 幫你整合了一些「圖形化工具」來操作 Workspace：
    - 建立 Liferay Workspace 專案。 
    - 建立 Service Builder、Portlet、Theme、Fragment 等模組。 
    - 一鍵部署到 Liferay Portal。 
    - 管理 Tomcat 的 啟動、停止、Debug。  

<br>

## 💡 在 Liferay 中，每個模組都是 OSGi bundle

Tomcat 啟動後，Liferay 還要逐個 bundle 啟動 日誌中會看到類似：
```
INFO [main][BundleStartLevel:123] Starting bundle com.liferay.xxx
```

<br>


## 💡 啟動 Portal 的指令：
```
Windows: bundles\tomcat-9.x\bin\startup.bat 
Linux/Mac: bundles\tomcat-9.x\bin\startup.sh
```

預設網址：http://localhost:8080

<br>

## 💡 自定義程式碼的編譯，以及部屬流程：
1. 執行指令 ```.\gradlew deploy```。
2. 這會將 Source Code 中， ```modules/``` 資料夾底下的東西，丟進 Portal 的 ```deploy/``` 資料夾中。
3. Liferay 持續掃描 ```deploy/``` 資料夾。
4. 將掃描到的檔案放進  ```osgi/modules/``` 中。
5. 該模組將自動進行熱更新，不須重啟 Tomcat。 

<br>

## 💡 其他
如果直接在 Liferay Workspace 中，執行 ```.\gradlew initBundle``` 指令，它會直接下載整個 Liferay Portal 在 ```bundles/``` 資料夾中。
