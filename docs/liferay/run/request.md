---
title: REQUEST 入口
parent: 執行與部署
---

# REQUEST 入口

## 🔹 1️⃣ 外部請求進入 Tomcat
所有請求（HTTP Request）都先由 
Tomcat 處理。

Tomcat 對應的 WebApp 是：
```
$LIFERAY_HOME/tomcat-9.0.xx/webapps/ROOT
```

在這個 ROOT WebApp 裡有：
```
WEB-INF/web.xml
```

這裡定義了 Liferay 的主入口 Servlet：
```
<servlet>
    <servlet-name>Main Servlet</servlet-name>
    <servlet-class>com.liferay.portal.servlet.MainServlet</servlet-class>
</servlet>
<servlet-mapping>
    <servlet-name>Main Servlet</servlet-name>
    <url-pattern>/c/*</url-pattern>
</servlet-mapping>
```



➡️ 所以所有到 /c/* 的請求都會進入 MainServlet。


## 🔹 2️⃣ MainServlet：Liferay 的前端控制器（Front Controller）
這是 Liferay Portal 的核心入口點。

### 對應的類別是：
```
com.liferay.portal.servlet.MainServlet
```

### 它的主要職責：
- 初始化 Portal 環境（公司、使用者、Session） 
- 處理 URL 轉導（Friendly URL, /web/..., /group/...）  
- 分派給 PortletContainer 或 MVCCommand 

## 🔹 3️⃣ Portlet 請求的進一步分派
若 URL 是 Portlet 頁面，例如：
```
/web/guest/home?p_p_id=com_liferay_login_web_portlet_LoginPortlet
```

會交給：
```
com.liferay.portal.kernel.portlet.PortletContainer
```

進一步分派到該 Portlet 的：
```
javax.portlet.Portlet
```

（如 doView, processAction）


## 🔹 4️⃣ 模組 (Module) MVCCommand 請求的入口
在 Liferay 7+，模組化後，每個 Portlet 通常使用：
```
MVCActionCommand, MVCRenderCommand, MVCResourceCommand
```

三種 Command 作為 Portlet 內的控制器。

例如：
```
@Component(
    immediate = true,
    property = {
        "javax.portlet.name=my_portlet",
        "mvc.command.name=/my/action"
    },
    service = MVCActionCommand.class
)
public class MyActionCommand implements MVCActionCommand {
    @Override
    public boolean processAction(ActionRequest request, ActionResponse response) throws PortletException {
        ...
        return true;
    }
}
```

### 前端呼叫方式：
```
/c/portal/my_portlet?p_p_id=my_portlet&p_p_lifecycle=1&p_p_state=normal&_my_portlet_mvcActionCommandName=/my/action
```





## 🧭 小結 — Liferay 接收 Request 的路徑
```
Browser
   ↓
Tomcat
   ↓
MainServlet (/c/*)
   ↓
PortalRequestProcessor
   ↓
PortletContainer
   ↓
Portlet (MVCActionCommand / MVCRenderCommand)
```

## 💡 如果你想自訂 Request 接收點
你有幾個安全作法：

| 目的 | 建議方式 |
| ---- | ---- |
| 處理自訂 REST API | 建立 Liferay module，使用 JAX-RS（javax.ws.rs.*），部署於 /o/my-api |
| 攔截所有請求 | 撰寫一個 Filter 模組（javax.servlet.Filter）並註冊 OSGi Component |
| 攔截 Portlet request | 使用 MVCCommand 或 PortletFilter |
