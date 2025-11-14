---
title: 內建 Table
parent: 執行與部署
nav_order: 2
---

# 內建 Table

Organization, Site, User Group，雖然都能「分群使用者」或「控制存取權限」，但用途與層級完全不同。

| table name | 主鍵 | 說明 | 其他欄位 | 關聯表 |
| ---- | ---- | ------ | ------ | ------ |
| organization_ | organizationId <br> ctCollectionId | 一種階層式的使用者分組（不同於 Site 或 User Group），通常代表公司部門、子公司、團隊等層級關係。 <br><br> - 建立「公司/部門」階層，例如： Raritan Taiwan <br> ├── QA Dept <br> └── RD Dept <br>  - 組織底下可以有 使用者、角色(Role)、甚至 專屬的 Site。  <br> - 可用於權限控管（Organization Role）。 | - parentOrganizationId 父組織 ID <br> - name 組織名稱 <br> - type_ 組織類型 <br> - recursable 是否可遞迴 <br> - statusId ?? | - users_orgs <br> 使用者與組織的關聯（多對多）<br> - group_ <br> 每個組織都會有一個對應的 Group（Site）|
| group_ <br><br> 在 Liferay 中，「Site」實際上是用  group_ 表來表示的。 | groupId <br> ctCollectionId | 「Site」就像「網站或社群」一樣，有自己的頁面、內容、權限設定。 <br><br> 沒有階層關係。 <br><br> 一個 group_ 可以代表： <br> - 一個 Organization 的 Site <br> - 一個 User 的個人 Site <br> - 一個 User Group 的 Site <br> - 一個 獨立建立的 Site <br> <br><br> 主要用途： <br> - 為不同的部門或用途建立不同網站。 <br><br> 例如： <br> - 公司內部網站（Intranet） <br> - 供應商網站（Vendor Portal） <br> - 產品展示網站（Product Portal） <br> <br> 擁有者：某個organization 或某個 usergroup | - companyId 所屬公司 <br> - classNameId / classPK 對應來源，例如：Organization、User、LayoutSetPrototype <br> - name 站點名稱 <br> - friendlyURL 站點網址 <br> - site 是否為 Site（true/false）|  |
| usergroup | userGroupId <br> ctCollectionId | 只是單純地「把一群人歸在一起」，方便管理權限或加入網站。 <br><br> 沒有階層關係。 <br><br> 批次管理一群使用者的 Site 存取。 | - companyId 所屬公司 <br> - name 群組名稱 <br> - description 群組描述 | - users_usergroups <br> 使用者與 User Group 的關聯（多對多） <br> - group_ <br> 每個 User Group 也會對應一個 Group（Site） |

<br>

---

<br>

> 先記得一件最重要的事情：在 Liferay 中所有的權限都只能賦予在角色 (Role) 身上。

跟權限最有關係的的 table 為 ResourceAction 及 ResourcePermission。


## ResourceAction

| 欄位 | 說明 |
| ---- | ---- |
| name | 資料 |
| actionId | 權限動作。 |
| bitwiseValue | 對於每個動作，有其代表的值。 |

## ResourcePermission

| 欄位 | 說明 |
| ---- | ---- |
| primKey | 該種資料的 primary key |
| roleId | 與哪個角色的對應 |
| scope | 代表的權限影響的範圍，數值對應如下 <br> 1 = 入口網，也就是整個 portal 範圍 <br> 2 = 站台，只在某個站台 <br> 3 = 站台範本 <br> 4 = 單一資料，只影響該資料 |
| actionIds | 參考 ResourceAction 表。 <br> 把所有權限的數字(bitwiseValue)相加。 |

## 在 Liferay 裡，role_ 表的 type_ 欄位定義了角色類型：

| 值 | 名稱 | 說明 |
| ---- | ---- | ------ |
| 0 | Regular Role（全域角色） | 一般角色，授權細節由資源決定，全域可用 |
| 1 | Site Role（網站角色） | 只在特定 Site 生效 |
| 2 | Organization Role（組織角色） | 只在特定組織生效 |
| 3 | Administrator  | 系統管理員，最大權限角色，全域有效 |