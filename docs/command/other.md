---
title: 指令
parent: Command
---


## 透過終端機，發送 HTTP 請求
- curl
    - Linux / macOS / Windows 都能用的命令行工具。
- ```-d```
    - 表示要傳送 POST 請求的資料。
- ```-H```
    - Header。

```bash
curl -d "{\"token\":\"JPqNOMuKF7QT8VURzcSav1Aj080L1ggt\",\"save\":\"force\"}" \
     -H "Content-Type:application/json" \
     http://spb-api/sp/baseball/v1/source/test

```