---
title: DataSource
parent: 執行與部署
nav_order: 5
---

# DataSource
## ext-spring.xml

這是一個 Spring 的 bean 定義檔 (```applicationContext.xml``` 類型)，

用來在 Liferay 啟動時，注入（或覆蓋）系統內部的資料來源（DataSource）。

---


## 範例，xxx-Persistence
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans default-destroy-method="destroy"
    default-init-method="afterPropertiesSet"
    xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-3.0.xsd">

<!--
這個 bean 使用了 Liferay 提供的 DataSourceFactoryBean，
會根據 portal-ext.properties 裡面以 jdbc.aaa. 開頭的設定，
自動產生一個真實的 javax.sql.DataSource 物件。
-->
    <bean
        class="com.liferay.portal.dao.jdbc.spring.DataSourceFactoryBean"
        id="liferayDataSourceImpl">
        <property name="propertyPrefix" value="jdbc.aaa." />
    </bean>

<!--
這個是 Spring 的延遲連線代理，意思是：
不在 Transaction 開始前馬上打開 DB connection，而是等到第一次真正執行 SQL 時才建立連線。
-->
    <bean
        class="org.springframework.jdbc.datasource.LazyConnectionDataSourceProxy"
        id="liferayDataSource">
        <property name="targetDataSource" ref="liferayDataSourceImpl" />
    </bean>

    <alias alias="extAaaDataSource" name="liferayDataSource" />

</beans>
```

## Liferay 啟動時會讀取所有屬性：
```
jdbc.[name].driverClassName
jdbc.[name].url
jdbc.[name].username
jdbc.[name].password
```

## 並自動建立對應的 DataSource：

| Properties Prefix | 產生的 DataSource 名稱 |
| ---- | ---- |
| jdbc.default.* | liferayDataSource（主 DB） |
| jdbc.aaa.* | aaaDataSource |

承上，看上述範例程式第 16 行，```value="jdbc.aaa."```，然後在 29 行改了別名，```alias="extAaaDataSource"```。


