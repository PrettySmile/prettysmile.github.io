---
title: OSGi Bundle 是什麼? 跟一般 JAR 有何不同?
parent: 執行與部署
---

# OSGi Bundle 是什麼? 跟一般 JAR 有何不同?


## 🔹 什麼是普通 JAR
- 定義：只是把 .class 檔、資源檔打包成一個 zip 格式的檔案，副檔名 .jar。  
- 特徵：
    - 可能有 META-INF/MANIFEST.MF，但通常只有很基本的資訊（版本、Main-Class）。  
    - JVM 只會把它當成 一包 class 路徑，沒有模組邊界的概念。    
- 缺點：
    - 沒辦法解決「版本衝突」問題，例如 A 模組要用 commons-io 2.6，B 模組要用 commons-io 2.11，傳統 JAR 只能選一個版本放進 classpath。 


## 🔹 什麼是 OSGi Bundle
- 定義：本質上它還是 JAR，但多了一些 OSGi 特定的 metadata（在 MANIFEST.MF 裡）。  
- 特徵：
    - Bundle-SymbolicName：唯一識別名稱（像模組 ID）。  
    - Bundle-Version：版本號（可同時存在多版本）。  
    - Export-Package：這個 Bundle 對外提供哪些 Java package。  
    - Import-Package：這個 Bundle 需要哪些 Java package，由其他 Bundle 提供。    
- 功能：
    - OSGi Runtime（像 Liferay 的 Felix、Equinox）會動態解決相依，確保「誰輸出 → 誰輸入」是正確的。 
    - 支援 模組隔離：不同版本的相同 library 可以並存，不會互相干擾。  
    - 支援 動態安裝/卸載/更新：不需要重啟整個 JVM，就能更新某個模組。    


## 🔹 舉例比較
假設你有一個 commons-lang3-3.12.0.jar：
- 普通 JAR：
    - MANIFEST.MF 很簡單，只有： 
        ```
            Manifest-Version: 1.0
        ```
    - JVM 啟動時，這個 JAR 就只是 classpath 裡的一部分。 
- OSGi Bundle JAR：
    - MANIFEST.MF 多了 OSGi metadata： 
        ```
        Bundle-SymbolicName: org.apache.commons.lang3
        Bundle-Version: 3.12.0
        Export-Package: org.apache.commons.lang3;version="3.12.0"
        Import-Package: org.osgi.framework;version="[1.3,2.0)"
        ```
- OSGi Runtime 會知道：
    - 這個 Bundle 叫 org.apache.commons.lang3，版本 3.12.0。  
    - 它提供 org.apache.commons.lang3 package。  
    - 它依賴 org.osgi.framework。      


## 🔑 總結
- 普通 JAR = 單純的 class 封裝，沒有模組化資訊。  
- OSGi Bundle = 帶有模組化 metadata 的 JAR，能在 OSGi 容器（像 Liferay）中被動態管理。  
- 👉 在 Liferay 7.4 中，如果你把一個普通 JAR 丟進 osgi/modules/，它啟動時會報錯，因為 沒有 OSGi metadata。

<br>

## 👉 這時候要嘛：
1. 把 JAR 打包進你的模組（最常見做法）。  
2. 用 bnd 工具或 Gradle 把普通 JAR 轉成 OSGi Bundle。  
3. 如果真的不需要 OSGi 化，就放到 osgi/static/ 或 tomcat/lib/ext/。  





