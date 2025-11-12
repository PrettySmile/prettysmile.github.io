---
title: configs 說明
parent: 執行與部署
---

# configs 說明


## 1️⃣ Portal 的配置檔案
在 Liferay 安裝目錄下，一些配置檔會直接影響 Portal 的運行：

| 專案檔案位置 | 對應 Liferay 位置 | 說明 |
| ---- | ---- | ------ |
| configs/common/portal-setup-wizard.properties | liferay-ce-portal-7.4.3.31-ga31/ | 可選。只在第一次啟動時影響 Wizard 設定，設定 admin user、email 等。 |
| configs/dev/portal-ext.properties | liferay-ce-portal-7.4.3.31-ga31/ | Portal 的主要配置，建議用 portal-ext.properties 覆蓋預設。 |
| configs/dev/system-ext.properties | liferay-ce-portal-7.4.3.31-ga31/ | 系統層級的擴展屬性，可選，會被 Portal 載入。 |
| configs/dev/server.xml | liferay-ce-portal-7.4.3.31-ga31/tomcat-9.0.56/conf/ | Tomcat server 設定，Port、Connector 等。 |
| configs/dev/web.xml | 依需求放入各自 Webapp | 若有自訂 web.xml 需要放在對應 webapp 的 WEB-INF。 |
