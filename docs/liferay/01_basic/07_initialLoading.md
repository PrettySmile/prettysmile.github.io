---
title: Tomcat 啟動過久
parent: Basic 教學
nav_order: 7
---

# Tomcat 啟動過久

## 1️⃣ Liferay 初始化流程重
Liferay 啟動時會做很多事情，包括：
- 讀取配置：portal.properties、portal-ext.properties、模組配置等。
- 模組化 OSGi 系統啟動：Liferay 7+ 用 OSGi，每個模組都要加載、初始化。  
- 資料庫檢查/建表：即使本地空 DB，也會跑建表、檢查 schema。  
- 初始化內建 portlet：例如 Document Library、User 等  
- 掃描 classpath：Tomcat 會載入 webapps/ROOT 下所有 jar。 

所以即使「空模組」，也要花時間啟動整個 Liferay 平台。


## 4️⃣ OSGi bundle 啟動
- Liferay 的每個模組都是 OSGi bundle，Tomcat 啟動後，Liferay 還要逐個 bundle 啟動。
- 日誌中會看到類似： 
    ```
    INFO [main][BundleStartLevel:123] Starting bundle com.liferay.xxx
    ```
- 這過程可能幾分鐘。（甚至超過 10 分鐘） 
- 第二次啟動會快很多，因為 bundle 已經緩存、DB schema 已建立。


## 🔹 建議

1. 第一次啟動耐心等，通常 10~20 分鐘屬正常。
2. 確認 JVM 記憶體足夠。  
3. 觀察日誌，可看到進度。

