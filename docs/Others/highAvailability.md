---
title: 高可用性
parent: Others
---


# 高可用性

即使某些部分出現故障，整個應用仍然能夠提供服務。

### **📌 如何實現高可用性？**

1. **無單點故障（No Single Point of Failure, SPOF）**
    - 任何一個服務或伺服器掛掉，不會影響整體系統。
    - **解法**：使用多個副本（Replica）、負載均衡（Load Balancer）。
2. **自動故障轉移（Failover）**
    - 當某個服務掛掉時，流量會自動轉移到健康的節點。
    - **解法**：Kubernetes（K8s）自動調度、HAProxy、Nginx 反向代理。
3. **數據冗餘與備份（Data Redundancy & Backup）**
    - 防止數據丟失，確保即使發生災難也能快速恢復。
    - **解法**：
        - 資料庫高可用（MySQL 主從複製、MongoDB Replica Set）
        - 物理備份（每日快照）
        - 分散式存儲（如 AWS S3、Google Cloud Storage）
4. **負載均衡（Load Balancing）**
    - 讓請求均勻分配到多個伺服器，避免單一節點過載。
    - **解法**：Nginx、AWS ELB、Kubernetes Service。
5. **異地多活（Multi-Region Deployment）**
    - 應用部屬在多個地區，防止單個地區故障影響整體。
    - **解法**：CDN（Cloudflare）、全球流量管理（AWS Route 53）。
