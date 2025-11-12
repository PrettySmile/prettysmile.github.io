---
title: 如何使用 DB
parent: 執行與部署
---

# 如何使用 DB

## 🧩 一、Liferay 使用 DB 的方式有三層（依你目的選擇）

| 層級 | 用法 | 適合用途 |
| ---- | ---- | ------ |
| ① Service Builder | 官方推薦，Liferay 生成 Service、Persistence、Model | 開發模組的正式業務邏輯 |
| ② 直接使用 Liferay DB API | 使用 DBManagerUtil, DataAccess, SqlUpdateFactoryUtil | 快速執行 SQL（例如批次、維運） |
| ③ 直接連接 JDBC | 取得 Liferay DataSource 自己跑 SQL | 臨時工具、特殊查詢（不推薦常態使用） |

## 🚀 二、Service Builder（官方推薦方式）
這是 Liferay 最完整的 ORM 機制。

你在 module 裡建立一個 service.xml：
```
<service-builder package-path="com.example.myapp">
    <namespace>MyApp</namespace>

    <entity name="UserInfo" local-service="true" remote-service="false">
        <column name="userId" type="long" primary="true" />
        <column name="email" type="String" />
        <column name="age" type="int" />
    </entity>
</service-builder>
```

執行：
```
gradlew buildService
```

它會自動生成：
- UserInfo model  
- UserInfoPersistence  
- UserInfoLocalServiceUtil / UserInfoLocalServiceImpl  

之後你就可以在程式中直接用：
```
import com.example.myapp.model.UserInfo;
import com.example.myapp.service.UserInfoLocalServiceUtil;

UserInfo user = UserInfoLocalServiceUtil.createUserInfo(0);
user.setEmail("test@example.com");
user.setAge(20);
UserInfoLocalServiceUtil.addUserInfo(user);
```

這會自動操作資料庫，不需自己寫 SQL。

👉 Liferay 底層用 Hibernate + C3P0。


## 🧠 三、手動 SQL（有時維運會用）
如果你只是想執行一段 SQL，不想建整個 Service Builder，

你可以直接這樣寫：

### ✅ 使用 Liferay 的 DataAccess：
```
import com.liferay.portal.kernel.dao.jdbc.DataAccess;

Connection con = null;
PreparedStatement ps = null;
ResultSet rs = null;

try {
    con = DataAccess.getConnection();

    ps = con.prepareStatement("SELECT userId, screenName FROM User_ WHERE active_ = ?");
    ps.setBoolean(1, true);

    rs = ps.executeQuery();

    while (rs.next()) {
        long userId = rs.getLong("userId");
        String name = rs.getString("screenName");
        System.out.println(userId + " - " + name);
    }
}
finally {
    DataAccess.cleanUp(con, ps, rs);
}
```

📍 優點：
- 使用 Liferay 的 connection pool（與 portal 同一個 transaction） 
- 不用自己設定 DataSource 


## 🧩 四、如果要執行非查詢 SQL（insert / update / delete）
可以使用：
```
import com.liferay.portal.kernel.dao.jdbc.SqlUpdate;
import com.liferay.portal.kernel.dao.jdbc.SqlUpdateFactoryUtil;
import com.liferay.portal.kernel.exception.SystemException;

Connection con = null;
try {
    con = DataAccess.getConnection();
    SqlUpdate sqlUpdate = SqlUpdateFactoryUtil.getSqlUpdate(
        con, "UPDATE User_ SET comments = ? WHERE userId = ?", new int[] { java.sql.Types.VARCHAR, java.sql.Types.BIGINT }
    );
    sqlUpdate.update(new Object[] { "Hello World", 20199L });
}
catch (Exception e) {
    throw new SystemException(e);
}
finally {
    DataAccess.cleanUp(con);
}
```





## 🧩 五、使用 Liferay 的 Finder（Service Builder 延伸）
如果你用 Service Builder，可以再加上 
 \<finder> 自動產生自訂 SQL，例如：
```
<finder name="Email" return-type="Collection">
    <finder-column name="email" />
</finder>
```

這樣會自動生成：
```
UserInfoLocalServiceUtil.findByEmail("test@example.com");
```





## 🧭 小結 — 選擇建議

| 情境 | 建議方式 |
| ---- | ---- |
| 你要建模、CRUD | ✅ 用 Service Builder |
| 你只是要查資料（Read-only | ⚙️ 用 DataAccess |
| 你要維護 Portal 內建資料（如 User_） | ⚠️ 用 DataAccess 小心操作 |
| 你要開 REST API 對外 | 用 Service Builder + REST Builder |
