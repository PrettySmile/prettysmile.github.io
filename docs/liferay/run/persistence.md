---
title: api 和 service 差別
parent: 執行與部署
---

# api 和 service 差別

這兩個目錄：
```
modules/
└── xxx-persistence/
    ├── xxx-persistence-api/
    └── xxx-persistence-service/
```



其實是 Service Builder 自動生成的兩個模組，分別扮演「介面層」與「實作層」的角色。

我幫你用實務開發角度，完整地拆解👇：


## 🧩 一、整體結構：Service Builder 會生成兩個 module
在你有 service.xml 的 module 下執行：
```
gradlew buildService
```
Liferay 會自動產生這兩個子模組：

| 模組 | 名稱範例 | 功能 |
| ---- | ---- | ------ |
| API 模組| xxx-persistence-api | 定義介面（LocalService, RemoteService, Model, Util 類） |
| Service 模組 | xxx-persistence-service | 實作所有業務邏輯（*LocalServiceImpl, *PersistenceImpl），也包含 SQL、OSGi Component 註冊 |


## 🧠 二、具體內容差異
📁 xxx-persistence-api 包含：

| 檔案類型 | 範例 | 功能說明 |
| ---- | ---- | ------ |
| Model | UserInfo.java | 對應資料表的 Java Bean（Liferay Model） |
| Local Service Interface | UserInfoLocalService.java | 定義方法介面（不含實作） |
| Remote Service Interface | UserInfoService.java | 給外部（JSON WS / REST）使用的介面 |
| Util 類 | UserInfoLocalServiceUtil.java | 提供靜態呼叫介面（方便其他模組使用） |
| Exception | NoSuchUserInfoException.java | 自動產生的例外類別 |
| Persistence Interface | UserInfoPersistence.java | 定義查詢與儲存邏輯介面 |


## 📦 結論：
這個 module 不含實作，只有「介面」與「model 定義」。

因此它是可以被其他 module 引用的。

在 build.gradle 中你常會看到其他 module 有：
```
compileOnly project(":modules:xxx-persistence:xxx-persistence-api")
```

## 📁 xxx-persistence-service 包含：

| 檔案類型 | 範例 | 功能說明 |
| ---- | ---- | ------ |
| Impl 實作 | UserInfoLocalServiceImpl.java | 實際的業務邏輯寫在這裡 |
| Persistence Impl | UserInfoPersistenceImpl.java | Hibernate 產生的實際資料操作程式 |
| Upgrade | UpgradeProcess 類別 | 資料庫 schema 更新邏輯 |
| ServiceWrapper | UserInfoLocalServiceWrapper.java | 可用於 AOP 攔截或覆寫 Service |
| META-INF/sql | tables.sql, indexes.sql | 由 service.xml 生成的 DB 結構 |
| META-INF/resources | JSP (若有) | UI 檔案或 REST JSON 配置 |
| OSGi 組件宣告 | @Component | 自動註冊到 OSGi Runtime |

## 📦 結論：
這個 module 負責實作並在 OSGi 啟動時註冊成真正的服務。

是整個 Service Builder 機制的執行核心。


## ⚙️ 三、它們在 OSGi 環境下如何互動？

| 流程 | 說明 |
| ---- | ---- |
| xxx-persistence-service 啟動時註冊 UserInfoLocalService 服務 | 透過 @Component 自動完成 |
| 其他模組若 import 了 xxx-persistence-api，即可透過 OSGi 注入 | 因為它只依賴 API，不需關心實作 |
| Liferay 在運行中，會自動把 service impl 綁定到 util 類別 | 例如 UserInfoLocalServiceUtil.addUserInfo() 背後實際呼叫的是 impl |

## 🧩 四、實務開發建議

| 目的 | 建議做法 |
| ---- | ---- |
| 你要在其他 module 使用這個 service | 只依賴 xxx-persistence-api |
| 你要修改 CRUD 或業務邏輯 | 改 xxx-persistence-service 下的 *Impl.java |
| 你要新增 finder 方法 | 改 service.xml 再執行 gradlew buildService |
| 你要修改 SQL schema | 改 service.xml → 自動生成 tables.sql |


## 🔍 五、舉例：一個簡單的 Liferay Service Builder 模組
```
modules/
└── user-data/
    ├── user-data-api/
    │   ├── com/example/user/model/UserInfo.java
    │   ├── com/example/user/service/UserInfoLocalService.java
    │   └── com/example/user/service/util/UserInfoLocalServiceUtil.java
    │
    └── user-data-service/
        ├── com/example/user/service/impl/UserInfoLocalServiceImpl.java
        ├── META-INF/sql/tables.sql
        ├── META-INF/resources/init.jsp
        └── service.xml
```


## 🧭 六、總結對照表

| 模組 | 主要角色 | 是否包含實作 | 是否可被其他模組依賴 |
| ---- | ---- | ------ | ------ |
| xxx-persistence-api | 對外公開的 API (介面 + model) | ❌ 否 | ✅ 是 |
| xxx-persistence-service | 實際邏輯實作 (CRUD, finder) | ✅ 是 | ❌ 不應直接依賴 |

