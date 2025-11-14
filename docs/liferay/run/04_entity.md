---
title: Entity
parent: 執行與部署
nav_order: 4
---
# Entity
## DB Table 對應的程式碼

你已知道某功能會查 DB 中，名為 ```xxx``` 的表。

在 Liferay 模組中，該資料表應該是由 ```service.xml``` 產生的。

請搜尋：
```
service.xml
```

找到：
```
<entity name="xxx" local-service="true" ...>
```

Liferay 會自動生成：
```
modules/xxx-persistence/xxx-persistence-service/src/main/java/.../service/persistence/xxxPersistence.java
modules/xxx-persistence/xxx-persistence-service/src/main/java/.../service/impl/xxxLocalServiceImpl.java
```

查詢 SQL 通常會在：
```
xxxLocalServiceImpl.java
```

裡面有方法例如：
```
public List<xxx> getByProductId(long productId)
```

## 主鍵，以及對應的 Class
當一個 ```entity``` 在 ```service.xml``` 中有多個 ```primary="true"``` 欄位時 (多主鍵時)。

Liferay 會自動產生一個 ```Primary Key``` 類別 名稱為：
```
public class aaa_bbbPK() {
}
```