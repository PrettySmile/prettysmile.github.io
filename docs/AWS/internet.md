---
title: 聯網
parent: AWS
---

# 聯網

### Amazon Virtual Private Cloud (Amazon VPC)
- 在AWS資源周圍，建立邊界。
- 可將資源組織到子網中。
- 可附加「互聯網網關」
- 組件1：**網路訪問控制列表 (ACL)**
    - 虛擬防火牆
    - 子網級別控制入站和出站流量。
    - 無狀態；機場的護照檢查人員；默認允許入站、默認允許出站。
- 組件2：**安全組**
    - 有狀態；大樓守衛；默認拒絕入站、允許出站。


### AWS Direct Connect
- 在數據中心和 VPC 之間，建立**專用私有連接**。


### Amazon Route 53
- DNS Web服務。