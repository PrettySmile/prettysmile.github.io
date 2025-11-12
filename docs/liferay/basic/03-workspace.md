---
title: Liferay Workspace?
parent: Basic 教學
nav_order: 3
---

# Liferay Workspace?


Liferay Workspace 是 Liferay 官方建議的專案開發結構，用來統一管理與開發 Liferay 模組（modules）、主題（themes）、佈署設定（configs）、以及 Liferay 自身的 bundle（伺服器執行環境）。它主要是基於 Gradle 來建立與管理的。

<br>

## 主要特色：

1. 統一專案結構
    - modules/：放你的 OSGi 模組（Portlet、Service、API 等）。  
    - themes/：放 Liferay 前端主題。  
    - wars/：傳統 war 包專案（如果還有需要）。  
    - configs/：不同環境的設定檔（開發、測試、正式）。  
    - bundles/：自動下載或放置 Liferay Portal 的伺服器 bundle。    
2. Gradle 為核心
    - 提供 task 來建立模組、部署、啟動伺服器。 
    - 例如：gradlew build、gradlew deploy。    
3. 方便部署與管理
    - 你可以在 workspace 裡同時管理 Liferay 的核心（bundle）以及所有自己開發的模組。 
    - Workspace 內建自動下載 Liferay bundle 的功能（免去手動安裝）。 
4. 跨環境設定
    - configs/ 內可以區分 dev、uat、prod，方便不同環境部署。    

<br>

## 為什麼要用 Liferay Workspace？
以前開發 Liferay Plugin 時，需要安裝 Liferay IDE 或 SDK，結構比較複雜。
現在 Liferay 推 Workspace，就是要統一開發方式：
- 更符合 OSGi 模組化。 
- 使用標準化的 Gradle build。 
- 減少開發人員在「專案結構」與「環境設定」上的混亂。 

<br>

👉 可以把 Liferay Workspace 理解成：Liferay 官方提供的一個「專案母框架」，
所有 Liferay 開發（Portlet、Service Builder、Theme 等）都放進這個框架中，並由它統一管理。
