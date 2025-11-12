---
title: Liferay 的「模組來源」有兩種
parent: Basic 教學
nav_order: 8
---

# Liferay 的「模組來源」有兩種

<br>

## 先釐清核心概念：Liferay 的「模組來源」有兩種
Liferay Portal 啟動時會載入模組（bundles），主要有兩個來源：

| 類型 | 說明 | 實際載入來源 |
| ---- | ---- | ------ |
| 靜態模組（Static Bundles）| Portal 內建的，例如 portal-kernel、frontend-theme-* 等。 | liferay-ce-portal-7.4.3.31-ga31/osgi/static |
| 動態模組（Dynamic Bundles） | 你自己開發的 module，例如 com.example.foo.api、service、web。 | 由 Felix OSGi Framework 載入，實際位置在： <br> 👉 liferay-ce-portal-7.4.3.31-ga31/osgi/state 裡的 cache（或 hidden 資料夾）|



Studio (IDE) 第一次 deploy 時，並沒有把 jar 丟進 osgi/modules，
而是透過 Liferay Gradle Plugin 的 remote deploy 機制，
把 module 丟到 portal 的 osgi/state 資料夾中（或 cache）。

<br>

## 為什麼 osgi/modules 會是空的？
原因是：

> osgi/modules 只是「Auto Deploy」的監聽資料夾，只有當你手動或 CI 流程把 jar 放進去時才會生效。


Studio deploy（或 gradlew deploy）使用另一套 API（BundleContext.installBundle），它直接把 module 丟進 OSGi runtime 裡面，並且快取在 osgi/state 中。

所以看起來 modules 是空的，但實際上已經裝進去了。


.manager 就是 OSGi 的 runtime cache。


OSGi 設計就是「把 jar 解壓縮到 runtime cache」，不直接放在你看的 modules 資料夾。


## 原理以及解析：
- 每個modules裡面有 bin 以及 build 資料夾。
    - bin：撰寫程式碼存檔後，會自動編譯成 .class 存在這。(不論 studio 或 vscode 都一樣)
    - build：下指令 gradlew build 後，會存在這。(studio是start server時)
- 部屬：
    - studio：啟動 start server 時，進行程式碼編譯，產生 modules/xxx/build 資料夾(包含 classes 以及 libs)，然後自動部屬到 portal/osgi/state 中。
    - vscode：下指令 gradlew build 進行程式碼編譯，產生 modules/xxx/build 資料夾(包含 classes 以及 libs)，然後手動複製 libs 內的 jar 檔，到 portal/deploy，tomcat會進行即時掃描，進行熱部屬。tomcat 會將檔案搬移至 osgi/modules 然後更新 osgi/state。
    - Tomcat 會出現如下提示：

![alt text](../../../assets/images/liferay/image.png)

    - 手動刪除 osgi/module 會影響 bundle stop

