---
title: 如何快速看 Liferay 專案
parent: Basic 教學
nav_order: 6
---

# 如何快速看 Liferay 專案

## 環境
1. 確認 Liferay 版本（DXP？Community？7.3、7.4？） 
2. 專案是部署在 Liferay Bundle（Tomcat 內建版）? <br> 還是 Docker / Kubernetes?

## 專案結構
- Liferay 專案通常用 Liferay Workspace（Gradle/Maven）組織  
- 主要有幾類模組：
    - Portlet Module（主要功能模組，像小程式） 
    - Service Builder Module（資料庫實體 + 服務層） 
    - Theme/Fragment（前端樣式） 
    - Ext / Hook / Config（擴充點與設定）   
- 程式碼理解
    - 大部分是 Java + JSP/React（依專案而定） 
    - Service Builder 負責 ORM 與 Service，產生資料表與 API 
    - Portlet 類似 MVC Controller，決定顯示什麼內容 
- 資料庫與設定
    - 先確認 portal-ext.properties 或 Docker Compose 中的 DB 設定 
    - 知道專案用的是 MySQL / Oracle / PostgreSQL 
- 部署與調試
    - 如何在本地跑起來：gradlew deploy → Liferay server → 登入 Portal 
    - 知道 如何看 Log（catalina.out / console） 
    - 知道專案怎麼上線（CI/CD？手動 deploy？） 
