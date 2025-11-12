---
title: JSONWS URL 規則
parent: '@JSONWebService'
nav_order: 2
---

# JSONWS URL 規則

## 對應規則如下：

| 狀況 | 傳入形式 | 傳給後端的值 |
| --- | --- | --- |
| 有字串值 | /ABC123 | "ABC123" |
| 空（null） | /- | null |
| 整數 0 | /0 | 0 |
| 布林 false | /false | false |
| 布林 true | /true | true |
