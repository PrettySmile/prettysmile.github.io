---
title: 存儲
parent: AWS
---


## 存儲

### Elastic Block Store (EBS)

- volume，塊級存儲。
- 存儲在 1 個可用區中。

### Simple Storage Service (S3)

- storage，對象存儲。
- S3 Standard
    
    存儲在至少3個可用區中。
    
- S3 Standard-IA
    
    不頻繁訪問的數據。
    
- S3 One Zone-IA
    
    只存儲在1個可用區中。
    
- S3 Intelligent-Tiering
    
    監控並自動移動到 Standard 或 Standard-IA。
    
- S3 Glacier Instant Retrieval
    
    幾毫秒內，完成檢索。
    
- S3 Glacier Flexible Retrieval
    
    幾分鐘到幾小時內，完成檢索。
    
- S3 Glacier Deep Archive
    
    12小時內，完成檢索。
    
- S3 Outposts
    
    為本地AWS Outposts提供對象存儲。
    

### Elastic File System (EFS)

- 可擴展的文件存儲。
- 存儲在多個可用區中。
- 多個實例同時讀寫
- 區域性資源

---

## 關係型數據庫

### Relational Database Service (RDS)

- 託管性高；關係型數據庫。
- 支持：MySQL, PostgreSQL, Oracle, Microsoft SQL Server, MariaDB, Amazon Aurora。
- 「自動修補」、「備份」、「冗餘」、「故障轉移」、「災難恢復」。

### Amazon Aurora

- 託管性最強；關係型數據庫。
- 支持：MySQL, PostgreSQL。
- 「跨設施恢復數據」、「佈署15個只讀副本」、「備份放到S3，隨時還原」、「恢復特定時間點數據」。

---

## 非關係型數據庫 (NoSQL)

### Amazon DynamoDB

- 無伺服器數據庫。(免安裝、維護、管理)
- 自動擴展。
- 專用場景、毫秒級響應。

### Amazon DynamoDB Accelerator (DAX)

專為 DynamoDB 設計的，**原生緩存層**，可大幅縮短讀取時間，從毫秒縮到微秒。

---

## 數據倉庫

### Amazon Redshift

- 數據倉庫
- 適用**歷史分析**，數據不會再發生變化。
- 可大規模擴展
- 大數據分析，從多個源收集數據。
- 婷：像ELK的DB吧？

---

## 遷移服務

### Amazon Database Migration Service (DMS)

- 本地DB遷移到AWS。
- 同構遷移 (本地與AWS是同DB)
    
    MySQL → Amazon RDS for MySQL
    
    MySQL → Amazon Aurora
    
- 異構遷移
    
    Step1: AWS Schema Conversion Tool 進行，轉換構架和代碼。
    
    Step2: DMS 數據遷移。
    
- 開發或測試生產數據：
根據生產數據，測試應用程序，不會影響生產用戶。
一次性遷移或持續性遷移。
- 數據庫整合：
將多個DB，整合成 1 個中心數據庫。
- 持續複制：
持續將數據副本發送目標源，而非一次性遷移。
用於災難恢復，或進行地理位置的分割。

---

## 特定業務需求數據庫

### Amazon DocumentDB (with MongoDB compatibility)

內容管理系統 (文檔數據庫服務)，適用於目錄和用戶資料的內容管理。

支持 MongoDB (文檔數據庫程序)

### Amazon Neptune

圖形數據庫

專為社交網絡、推薦引擎、欺詐檢測。

### Amazon Managed Blockchain

分布式，分類賬系統。

在沒有中央授權的情況下運行交易和共享數據。

需要跟蹤並確保沒有任何內容丟失，或**內容完全保持不變**。

可解決部分問題，但也會添加一個巨大的分散化組件。

### Amazon Quantum Ledger Database (Amazon QLDB)

分類賬數據庫。

**不可變記錄系統**，所有條目都不可刪除。

應用程序，所有更改的，完整歷史記錄。

---

## 緩存解決方案

### Amazon ElastiCache

數據庫**添加緩存層**，將讀取時間從毫秒縮到微秒。

支持：Memcached 和 Redis