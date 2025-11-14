---
title: Liferay 常見核心設定檔案
parent: Basic 教學
nav_order: 5
---

# Liferay 常見核心設定檔案


## 1️⃣ Liferay 常見核心設定檔案

| 檔案名稱 | 位置 | 作用 | 備註 |
| --- | --- | --- | --- |
| portal.properties| ROOT/WEB-INF/classes/portal.properties   | Liferay 核心預設設定檔。 | 不建議直接修改。 |
| portal-developer.properties  | 同上或 Liferay 內建   | 開發模式設定檔。 | 用 include-and-override 引入。 |
| portal-ext.properties  | Portal 根目錄   | 用來覆蓋或擴充 portal.properties 的預設值。 | 自訂 DB、session、mail、locale、開發模式等。 |
| system.properties  | WEB-INF/shielded-container-lib/portal-impl.jar!/system.properties   | JVM & 系統層級設定。 | Liferay 啟動時載入 |
| portal-setup-wizard.properties  | ROOT/WEB-INF/classes/   | 第一次安裝初始化用。 | 只在第一次啟動時使用，設定 admin user、email 等。 |
| portal-log4j-ext.xml  | 任意   | 自訂 log4j 設定。 | 覆蓋 Liferay 預設 logging。 |
| server.xml | ```tomcat/conf/``` | Tomcat server 設定，Port、Connector 等。 ||


## 2️⃣ Liferay 讀取與覆蓋順序
Liferay 啟動時會依照以下順序載入設定：

1. JVM 系統層級參數
    - 例如 -Dfile.encoding=UTF-8、-Djava.net.preferIPv4Stack=true 等。 
    - 來源：Tomcat catalina.bat 或 Gradle startBundle 的 JVM args。  
2. system.properties
    - 來源：portal-impl.jar!/system.properties。
    - 系統層級預設。
3. portal.properties
    - 核心預設設定。
    - 不建議直接修改。 
4. portal-developer.properties（可選）
    - 用 include-and-override 引入。  
    - 開發模式設定。 
    - 可被 portal-ext.properties 覆蓋。 
5. portal-ext.properties
    - 使用者自訂設定。 
    - 覆蓋上面所有相同 key 的設定。 
6. module / OSGi Config
    - osgi/configs 下的 .config 或 .cfg。  
    - 適用於特定模組或服務的設定。 
    - 最後被 OSGi 系統載入。 

> 重點：<br>
> 最終生效的設定永遠是 portal-ext.properties + OSGi Config，可以覆蓋開發模式或核心預設。




## 啟動流程
1. Tomcat 啟動 JVM。
2. Catalina 初始化。
3. Liferay Portal 初始化
    - 讀取 portal.properties。
    - 如果有 portal-ext.properties → 覆蓋前面設定。
4. OSGi Framework 啟動
    - 核心模組先啟動。（portal-core、database、web-core） 
    - 非必要模組，決定是否延遲啟動。    
5. Database 連線初始化
    - HikariCP 建立 connection pool。
    - 初始化 schema / tables。（第一次啟動） 
6. Hot Deploy / Module Deploy
    - Workspace / Deploy 資料夾模組載入。 
    - Portlet、hook、layout template、theme 等載入。 
7. Portal 完全啟動
    - Web 可訪問。

