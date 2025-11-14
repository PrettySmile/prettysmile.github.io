---
title: build.gradle 說明 與 bnd.bnd 說明
parent: 執行與部署
---

# build.gradle 說明 與 bnd.bnd 說明

## build.gradle 說明
```build.gradle``` 是 Gradle 的建置腳本，告訴 Gradle，怎麼編譯、打包、處理依賴，編譯成 bundle。
```groovy
dependencies {
    compileOnly group: "com.liferay.portal", name: "release.portal.api"

    cssBuilder group: "com.liferay", name: "com.liferay.css.builder", version: "3.0.2"

    compile group: 'com.itextpdf', name: 'layout', version: '7.2.4'
    compile group: 'org.slf4j', name: 'slf4j-api', version: '1.6.1'

    compileOnly project(":modules:xxx-Persistence:xxx-Persistence-api")
    compileOnly project(":modules:xxx-Persistence:xxx-Persistence-service")
}
```

- ```compileOnly group```: 只需要在編譯時使用，不會打包進 bundle。
- ```cssBuilder group```: 用來編譯 ```SCSS/CSS``` 文件，產生最終的 ```CSS```。
- ```compile group```: 
    - 需要打包進 bundle 的第三方 library。
    - 例如 HTTP client, JSON parser 或是 iText PDF 庫的各個模組，打包進 bundle，用於 PDF 生成/簽章/條碼等功能。
- ```compileOnly project```: 只需要在編譯時使用，不會打包進 bundle，引用同一 workspace 下其他模組的 api 或 service。
- ```runtime group```: 只在執行時需要，編譯時不必有。



## bnd.bnd 說明
```bnd.bnd``` 是 bundle 的配置。告訴 OSGi，bundle 的 metadata、Import/Export/Include-Resource 等。
```properties
Bundle-Name: xxx-xxx
Bundle-SymbolicName: com.xxx.xxx.xxx
Bundle-Version: 1.0.0
Export-Package: com.xxx.xxx.xxx.constants
  
Include-Resource:\
    @aaa.jar,\
    @bbb.jar,\
    
Import-Package: \
    !com.ccc.api.ddd.*,\
```

- ```bnd.bnd``` 是 OSGi Bundle 的核心描述檔。
- 它告訴 OSGi 容器：
    - ```Bundle-Name```：Bundle 名稱。
    - ```Bundle-SymbolicName```：唯一識別符號。
    - ```Bundle-Version```：版本號。
    - ```Export-Package```：這個 bundle 導出了哪些 package，而這些 package 可以被其他 bundle 使用。
    - ```Import-Package```：這個 bundle 需要哪些外部 package，容器會自動在 runtime 解決這些依賴。
        - 典型用途：
            - 你不打算把某些依賴打包進 bundle，而是希望由容器提供。 
            - 避免 jar 冗餘或版本衝突。
            - ```
                Import-Package: \
                    !com.ccc.api.ddd.*, \
                    *
              ```
            - 解釋：
            - ```!com.ccc.api.ddd.*``` → 排除這些 package，不從容器導入（可能自己包含或不需要）。  
            - \* → 自動導入 bundle 用到的其他 package。
    - ```Include-Resource```：包含哪些資源或 jar，可把外部 jar 或資源打包進 bundle 裡。
        - 典型用途：
            - 你的 bundle 需要一些第三方 jar，但不想依賴 OSGi 容器去提供它。 
            - 你的 bundle 有靜態資源（如配置文件、圖片）需要隨 bundle 一起發布。
            - ```
                Include-Resource: \
                    @aaa.jar,\
                    config/settings.xml
              ```
            - 解釋：
            - ```@aaa.jar``` → 把 aaa.jar 的內容整合到 bundle 的根目錄。  
            - ```config/settings.xml``` → 把本地檔案加入 bundle。  

            💡 注意：這個只是把 JAR 或檔案放進 bundle，並不自動幫你把裡面的 class 導出或導入，仍需要在 ```Import-Package``` 指定哪些 class 可以被使用。


## 執行流程
假設你執行 ```gradlew build```：

1. Gradle 讀取 ```build.gradle``` 解析 plugins、dependencies、tasks 等，設定編譯路徑、依賴的第三方 jar 或其他模組。 
2. Gradle 編譯原始碼 將 ```src/main/java``` → ```build/classes/java/main```，使用 compileOnly、compile、runtime 等依賴決定 classpath。    
3. Gradle 打包成 OSGi bundle
    - 這時 Gradle 會讀取 ```bnd.bnd```。  
    - 根據 ```bnd.bnd```：
        - 生成 ```MANIFEST.MF```（包含 ```Bundle-Name```、```Import-Package```、```Export-Package``` 等）。 
        - 將 ```Include-Resource``` 指定的 JAR/資源整合進 bundle。    
    - 最終產生 .jar bundle 放在 ```build/libs/```。   
```
# bundle 的結構大概像這樣：
mymodule-1.0.0.jar
├─ META-INF/
│   └─ MANIFEST.MF       <-- bnd.bnd 內容轉成 manifest，給 Tomcat的 Liferay OSGi 容器閱讀用的
├─ com/example/mymodule/  <-- 你的 class
└─ lib/external.jar       <-- Include-Resource 打包進來
```
- 部署/執行
    - 將 .jar 放到 Liferay/Tomcat deploy 目錄。  

<br>

---

<br>

在 Liferay Workspace 專案裡，每個 ```modules/...``` 都是一個獨立的 OSGi bundle (就是 .jar)。

當你執行 ```gradlew build``` 的時候，每個 module 都會在自己的 ```build/libs/``` 底下產生 .jar。



