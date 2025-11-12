---
title: 初始化過久
parent: Basic 教學
nav_order: 7
---

# 初始化過久

## 1️⃣ Liferay 初始化流程重
Liferay 啟動時會做很多事情，包括：
- 讀取配置：portal.properties、portal-ext.properties、模組配置等  
- 模組化 OSGi 系統啟動：Liferay 7+ 用 OSGi 模組化，每個模組都要加載、初始化  
- 資料庫檢查 / 建表：即使本地空 DB，也會跑建表、檢查 schema  
- 初始化內建 portlet：例如 Journal、Document Library、User 等  
- 掃描 classpath：Tomcat 會載入 webapps/ROOT 下所有 jar，Liferay jar 很多 → 掃描很久  

所以即使「空模組」，也要花時間啟動整個 Liferay 平台。


## 4️⃣ OSGi bundle 啟動
- Liferay 的每個模組都是 OSGi bundle，Tomcat 啟動後，Liferay 還要逐個 bundle 啟動 
- 日誌中會看到類似： 
    ```
    INFO [main][BundleStartLevel:123] Starting bundle com.liferay.xxx
    ```
- 這過程可能幾分鐘（甚至超過 10 分鐘） 
- 第二次啟動會快很多，因為 bundle 已經緩存、DB schema 已建立


## 🔹 建議

1. 第一次啟動耐心等，通常 10~20 分鐘屬正常  
2. 使用本地 MySQL，比遠端 Azure 快很多  
3. 確認 JVM 記憶體足夠，避免 swap 或 GC 過多  
4. 日誌觀察：catalina.out 或 liferay.log 可看到進度

## 💡 小結：

- 空專案 → Liferay 啟動慢 ≠ Tomcat 問題 
- 主要是 Liferay 本身要初始化模組 + DB schema + OSGi bundle 
- 第二次啟動會快很多 


