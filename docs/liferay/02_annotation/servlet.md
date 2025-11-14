---
title: '@Servlet'
parent: 註解
---

# @Servlet

在 Liferay 中，/o 前綴其實是 Liferay 為 OSGi Servlet 自動加上的全局上下文前綴，並不是你在模組裡寫的。詳細說明如下：


## /o 的來源
- Liferay 7+ 採用 OSGi HTTP Whiteboard 標準註冊 Servlet。  
- 為了區分傳統 Portlet/JSF 等 URL 路徑，Liferay 統一給 OSGi Servlet 加上 /o 前綴。  
- /o = OSGi 模組前綴，所有通過 @Component(service=Servlet.class) 註冊的 Servlet 都會自動加上。
