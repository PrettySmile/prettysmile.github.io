---
title: '@JSONWebService'
parent: 註解
---

# @JSONWebService

## 說明
- @JSONWebService 是 Liferay Portal 提供的一個註解。
- 將某個服務（Service）或方法暴露為 JSON Web Service。
- 讓外部系統可以透過 HTTP 調用它，並得到 JSON 格式的回應。
- 簡單來說，它就是一個內建的 REST-like API 功能。


## 程式範例：
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

## Liferay 會自動生成類似這樣的 URL：
```http://localhost:8080/api/jsonws/aaa.bbb/ccc/param01/value01/param02/value02/-param03/```

> 後方參數參考：```JSONWS URL 規則``

## 進入 Liferay 的 JSONWS 介面
- ```http://localhost:8080/api/jsonws```

<br>

# JSONWS URL 規則

## 對應規則如下：

| 狀況 | 傳入形式 | 傳給後端的值 |
| --- | --- | --- |
| 有字串值 | /ABC123 | "ABC123" |
| 空（null） | /- | null |
| 整數 0 | /0 | 0 |
| 布林 false | /false | false |
| 布林 true | /true | true |

## 範例 URL：
```http://localhost:8080/api/jsonws/{name}.{path}/{function name}/order-type/ailsa/order-number/1111111/-item-number/```