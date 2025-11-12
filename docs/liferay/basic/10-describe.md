---
title: 說明
parent: Basic 教學
nav_order: 10
---

# 說明
修改 Java Home
```
gradle.properties org.gradle.java.home=C:\\Program Files\\Eclipse Adoptium\\jdk-8.0.462.8-hotspot
```

<br>

執行指令，下載整個 Tomcat + Liferay Portal（幾百 MB）

 → Gradle 會使用 Java 8 去下載 Liferay 7.4 ga31 bundle → 成功會在專案生成 bundles/ 資料夾
```
.\gradlew initBundle
```


<br>

啟動Liferay Windows: 
```
Windows: bundles\tomcat-9.x\bin\startup.bat 
Linux/Mac: bundles\tomcat-9.x\bin\startup.sh
```
預設網址：http://localhost:8080


<br>


- 執行指令，部屬模組 ```.\gradlew deploy``` → 這會把 ```modules/``` 下的東西丟進 ```bundles/deploy/``` ，Liferay 會自動載入。
- 設定環境變數，並測試： ```echo $env:CATALINA_HOME```
- 啟動專案，並 ```$env:CATALINA_HOME\bin\startup.bat```
- 打開瀏覽器： ```http://localhost:8080```


<br>


```portal-ext.properties``` 是 Liferay Portal 的擴充設定檔，用來覆蓋或擴充 ```portal.properties``` 的預設值。

Liferay 啟動時會讀取 ```portal.properties``` → 再讀 ```portal-ext.properties``` 覆蓋設定 可以用它來設定：
- session
- 時間 	
- 上傳檔案限制 	
- 資料庫連線資訊 	
- 郵件設定 	
- LDAP / 密碼政策 	
- 模組行為等


<br>


OSGi bundle 啟動 Liferay 的每個模組都是 OSGi bundle，Tomcat 啟動後，Liferay 還要逐個 bundle 啟動 日誌中會看到類似： ```INFO [main][BundleStartLevel:123] Starting bundle com.liferay.xxx``` 這過程可能幾分鐘（甚至超過 10 分鐘）。

第二次啟動會快很多，因為 bundle 已經緩存、DB schema 已建立。


<br>

---


<br>


Liferay 版本：portal-7.4-ga31 表示專案要用 Liferay CE Portal 7.4 GA31 Liferay 7.4 官方建議的 JDK 是 Java 11 或 Java 17 你現在設定的是 JDK 8 → 不符合版本要求 ✅


<br>

portal-ext.properties 建議：不要在公開檔案裡存明文密碼，開發時可先用，生產環境建議加密或使用環境變數
