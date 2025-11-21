---
title: python fastAPI 框架練習
parent: DEMO
---

> used windows system

# python fastAPI 框架練習

1. 安裝套件
uvicorn 是 ASGI 伺服器，適合用於部屬 Python Web。
> ASGI 是一種定義 Python 和伺服器之間的通訊協議。
```
    pip install fastapi uvicorn
```


# QA
## ASGI ?
- ASGI 為 Asynchronous Server Gateway Interface(非同步伺服器網關介面)。
- 一種網路伺服器（如 Apache、Nginx等）和後端應用程式間通訊的接口標準。
- 因為網頁伺服器看不懂 Python，需要一定的翻譯才能運行順暢。

| 簡稱 | ASGI | WSGI |
| --- | --- | --- |
| 全名 | Asynchronous Server Gateway Interface | Web Server Gateway Interface |
| 處理方式 | 非同步 | 同步 |
| 差異 | 允許在單個執行緒中處理多個請求。 | 每個請求在一個執行緒（Thread）或進程（Process）中處理，直到完成回應。 |
| 說明 | ASGI 可以處理多種協議（HTTP、WebSocket 等），適合現代 Web 應用，特別是需要非同步處理的應用。適合高併發場景。 | 處理 I/O 密集型任務（如資料庫查詢或與外部 API 的通信）時，可能會導致性能瓶頸（throttle），因為每個請求必須等待其他請求完成。 |

