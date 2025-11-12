---
title: '介紹'
parent: '@JSONWebService'
nav_order: 1
---

# 介紹

@JSONWebService 是 Liferay Portal 提供的一個註解，用來將某個服務（Service）或方法暴露為 JSON Web Service，讓外部系統可以透過 HTTP 調用它，並得到 JSON 格式的回應。

簡單來說，它就是一個內建的 REST-like API 功能，但是 Liferay 自己的方式實現的。




程式範例：
```java

@Component(
    property = { 
        "json.web.service.context.name=aaa", 
        "json.web.service.context.path=bbb" 
    }, 
    service = AopService.class)

@JSONWebService
public JSONObject ccc(String param01, String param02, String param03) {
    /// 方法內容
}

```

Liferay 會自動生成類似這樣的 URL：
```http://localhost:8080/api/jsonws/aaa.bbb/ccc/param01/value01/param02/value02/-param03/```

> 後方參數參考：[JSONWS URL 規則](./h.html)

## 進入 Liferay 的 JSONWS 介面
- ```http://localhost:8080/api/jsonws```