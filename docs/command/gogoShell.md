---
title: Gogo Shell 指令
parent: Command
---

# Gogo Shell 指令

## Gogo Shell 是什麼？
- Liferay 內建的一個 OSGi 互動命令列介面（Console）。  
- 透過它，你可以：
    - 列出目前已安裝的 bundles（模組） 
    - 查詢 bundle 狀態（Active / Resolved） 
    - 查看 bundle 的實體路徑 
    - 啟動 / 停止 / 卸載 bundle 
- 介面是 文字命令列，可以在瀏覽器或 telnet/SSH 連線執行。
- 類似一個「內建的終端機」，專門用來管理 Liferay / OSGi 模組。

## 連線到 Gogo Shell：
```
telnet localhost 11311
telnet localhost 11312
```

## 用法
```
lb                 # 列出所有 bundle
lb | grep pac      # 篩選你的模組
diag 1623          # 顯示 bundle 詳細資訊（包括實體路徑）
headers 15864

uninstall 325
uninstall com.mycompany.my-module
```

## 常用命令

| 命令 | 功能 |
| --- | --- |
| lb | 列出所有已安裝的 bundle（模組） |
| grep | grep <關鍵字> |
| diag <bundleId> | 顯示 bundle 詳細資訊，包括實體路徑、狀態 |
| start <bundleId> | 啟動 bundle |
| stop <bundleId> | 停止 bundle |
| uninstall <bundleId> | 卸載 bundle |
