---
title: Gradle 指令
parent: Command
---

# Gradle 指令
撰寫自定義指令，透過寫 build.gradle 得到：
```bash
.\gradlew syncConfigsToPortal
```

刪除 build 產出的資料夾：
```bash
# 移除 workspace/build
# 移除 workspace/modules/:xxx/:xxx/build
# 移除 workspace/modules/:xxx/build 
./gradlew clean
```

編譯：
```bash
# 全部模組 build
# 產生 workspace/build
# 產生 workspace/modules/:xxx/:xxx/build
# 產生 workspace/modules/:xxx/build 
./gradlew build

# 單一模組 build
./gradlew :modules:xxx:build

# 不 build 指定模組
./gradlew build -x :modules:xxx:build
```

部屬：
```bash
# 全部模組，部屬到 Portal
./gradlew deploy

# 單一模組，部屬到 Portal
./gradlew :modules:my-service:deploy
./gradlew :modules:my-web:deploy
```

告訴 Gradle 忽略快取，重新檢查和下載所有依賴
```bash
./gradlew build -x :modules:xxx:build --refresh-dependencies
```


查看完整清單，依分類顯示所有 Gradle + Liferay 插件提供的任務。
```
./gradlew tasks
```
 
<br>

---

<br>

## ✅ Gradle 原生指令
- assemble, build, clean, test, check  
- javadoc  
- dependencies, dependencyInsight, projects, properties  
- wrapper, init  
- eclipse, idea
- components, model …

## ✅ 由 Liferay Gradle Plugin / Workspace 提供的 Gradle 指令
### Module / Plugin 任務相關
- deploy：打包並丟到 deploy/ 資料夾（熱部署用）。
- deployFast：直接把資源丟到工作目錄，比較快的熱部署方式。  
- watch：監控檔案變更，自動 redeploy。  
- buildLang：跑 Liferay Lang Builder，處理 Language.properties。  
- buildService：跑 Liferay Service Builder 產生 -api, -service。  
- buildREST：產生 REST Builder API。  
- buildUpgradeTable：產生 upgrade SQL。  
- buildWSDD：產生 SOAP 相關的描述檔。  
- buildSoy / replaceSoyTranslation / transpileJS / configJSModules：前端資源編譯。  
- cleanServiceBuilder：清掉 Service Builder 的 table。  

## Bundle / Portal 任務相關
- initBundle：下載 + 解壓 Liferay bundle。  
- distBundleZip\*, distBundleTar\*：把 workspace 打包成完整的 Liferay bundle（支援 dev / local / prod / uat profile）。

## Docker 任務相關
- buildDockerImage, pullDockerImage  
- createDockerfile*, createDockerContainer, dockerDeploy  
- startDockerContainer, stopDockerContainer, logsDockerContainer, removeDockerContainer  

## 格式化任務相關
- formatSource：Liferay Source Formatter  
- checkSourceFormatting  
- formatJavadoc, formatTLD  

## 驗證 / 測試相關
- compileJSP：把 JSP compile 起來檢查錯誤。  
- startTestableTomcat, stopTestableTomcat：本地 bundle 測試用。  

