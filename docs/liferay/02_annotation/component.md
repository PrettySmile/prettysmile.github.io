---
title: '@Component'
parent: 註解
---

# @Component

@Component 註解是 Liferay 7+ OSGi Portlet 模組註冊的核心設定。
```
@Component(
    immediate = true
    , property = { 
        "com.liferay.portlet.display-category=category.aaa.Vendor"
        , "com.liferay.portlet.header-portlet-css=/css/main.css"
        , "com.liferay.portlet.instanceable=true"
        , "javax.portlet.display-name=bbb"
        , "javax.portlet.init-param.template-path=/"
        , "javax.portlet.init-param.view-template=/view.jsp"
        , "javax.portlet.name=" + ccc
        , "javax.portlet.resource-bundle=content.Language" 
        , "javax.portlet.security-role-ref=administrator"
        } 
        , service = Portlet.class)
public class xxxPortlet extends MVCPortlet {
}
```


## 🧷 immediate = true
- 📘 意思：
代表這個 OSGi 元件（Portlet）在系統啟動時立即啟動與註冊，
而不是等到第一次被呼叫才啟動。
- 📍通常對 Portlet 這種服務建議設為 true，確保系統啟動後馬上可用。


## 📦 com.liferay.portlet.instanceable=true
- 📘 意思：
決定這個 Portlet 是否「可重複使用」。
- ✅ true：同一個 Portlet 可以被加到多個頁面或同一頁面多次（每個都有獨立設定）。
- ❌ false：全站只能存在一個實例。


## 🏷️ javax.portlet.display-name=xxx
- 📘 意思：
這是顯示在 Liferay 後台 Widget 清單中的「顯示名稱」。
- 🖥️ 例如在「新增 Widget」清單裡會看到：
xxx。
- 📍也可以被語系覆蓋（在 ```Language.properties``` 裡用 ```javax.portlet.title.[portlet-name]```）。



## 🧱 javax.portlet.name= + xxx
- 📘 意思：
這是這個 Portlet 的 唯一識別 ID。
- 🧩 在 Liferay 系統中、資料庫中、PortletPreferences 裡，
都會用這個名稱來辨識這個 Widget。

Ailsa Notes：優先權高於 ```javax.portlet.display-name=xxx```。


## 🔐 javax.portlet.security-role-ref=...
- 📘 意思：
定義「哪些角色（Role）」能夠使用這個 Portlet。
- 📍格式：
administrator,...
- 這些名稱會對應到：
    - Liferay 內建角色（Administrator 等）。 
    - 或在 ```liferay-portlet.xml``` 的 <role-mapper> 裡自訂的角色名稱。
- ✅ 只有符合這些角色的使用者，才能：
    - 存取此 Portlet。
    - 操作其中功能（例如顯示畫面、按鈕權限）。


---

| javax.portlet.title |
| ---- |
| xxx.doView() <br><br> 分類名稱：(com.liferay.portlet.display-category) <br><br> 項目名稱：(javax.portlet.name) <br><br> 功能頁簽名稱： |

---

## 建立一個 Liferay 的 SearchContainer 物件，用來包裝：
- 當前頁要顯示的資料 
- 資料總筆數 
- 分頁資訊

## 將結果放進 Request，給 JSP 用：
```
renderRequest.setAttribute(aaa, bbb);
```

JSP會用：
```
<liferay-ui:search-container
    searchContainer="${aaa}">
```



