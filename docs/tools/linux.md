---
title: ngrok
parent: Tools
---

# ngrok

## 用途
- 將內部 localhost 網址，public 出去。
- 一次只能一個網址出去。

## 流程
1. 下載 ngrok

2. 執行 ngrok.exe

3. 輸入
```
ngrok http --host-header=localhost 4200
```
*後面為要 public 出去的本機 ```ip``` 與 ```port```。