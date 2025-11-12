---
title: Liferay Workspace with Dev Studio?
parent: Basic 教學
nav_order: 4
---
# Liferay Workspace with Dev Studio?

<br>

## 1. Liferay Workspace
就是我前面說的 專案結構與 Gradle 環境，用來管理模組、主題、設定、Liferay bundle。

👉 這是 後端/專案管理層。

<br>

## 2. Liferay Dev Studio (以前叫 Liferay IDE)

- 其實就是 Eclipse 的客製化版本（在 Eclipse 基礎上加上 Liferay 插件）。  
- Dev Studio 幫你整合了一些「圖形化工具」來操作 Workspace：
    - 建立 Liferay Workspace 專案。 
    - 建立 Service Builder、Portlet、Theme、Fragment 等模組。 
    - 一鍵部署到 Liferay bundle。 
    - 管理伺服器（啟動、停止、Debug）。 
    - GUI 介面操作，不需要全部手寫 Gradle 指令。 

<br>

## 3. 兩者結合的意思
當你用 Liferay Dev Studio 時，它會要求你建立一個 Liferay Workspace。
所以整個流程是：

1. 安裝 Liferay Dev Studio（Eclipse 版本）。  
2. 在 Dev Studio 裡「New → Liferay Workspace Project」。 
3. Dev Studio 幫你自動生成 Workspace 的目錄結構（modules/、themes/、configs/...）。  
4. 在 Dev Studio 裡建立/編輯模組，實際上就是往 Workspace 的 modules/ 裡丟東西。  
5. 點右鍵 → Deploy，就會透過 Gradle 把模組部署到 Workspace 內的 Liferay bundle。 

<br>

## ✅ 簡單理解：

- Liferay Workspace：就是「程式碼和環境的骨架」。專案結構 + Gradle 設定，不是一個軟體。
- Liferay Dev Studio：就是「IDE + GUI 工具」，幫你更輕鬆操作 Workspace。一個 IDE 工具，內建了 建立/管理 Liferay Workspace 的功能。

