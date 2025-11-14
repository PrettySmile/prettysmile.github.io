---
title: 如何快速看專案
parent: Basic 教學
nav_order: 6
---

# 如何快速看專案

## 環境
1. 確認 Liferay Portal 版本?（DXP? Community?） 
2. 部署的 Liferay Portal 位置?

## 專案結構
- Liferay 專案通常用 Liferay Workspace 框架撰寫。  
- 主要有幾類模組：
    - Portlet Module（主要功能模組，像小程式） 
    - Service Builder Module（資料庫實體 + 服務層） 
- 程式碼理解
    - 大部分是 Java + JSP。
    - Service Builder 負責 ORM 與 Service，產生資料表與 API。 
    - Portlet 類似 MVC Controller，決定顯示什麼內容。 
- 資料庫與設定
    - 先確認 portal-ext.properties 中的 DB 設定。 
    - 知道專案用的是 MySQL / Oracle / PostgreSQL。
- 部署與調試
    - 如何在本地跑起來：
        1. 執行 ```gradlew deploy```
        2. 啟動 Liferay Portal 的 Tomcat。
        3. 透過 瀏覽器 登入。 
    - 知道 如何看 Log。 
    - 知道 專案怎麼上線。（CI/CD？ 手動deploy到Portal？） 
