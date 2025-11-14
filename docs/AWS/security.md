---
title: Security
parent: AWS
---

# 安全性
### Multi-Factor Authentication (MFA)

- 多重驗證

### AWS Identity and Access Management (AWS IAM)

- 創建 IAM 帳戶；默認沒有任何權限。
- IAM 策略，是一個 JSON 文檔。
    - 規定用戶，可以執行、不可以執行的API。
    - 可關連到 IAM 用戶，或 IAM 組。
- IAM 用戶
    - 一個身份。
    - 與 AWS 服務和資源交互的人員，或應用程序。
- IAM 組
    - IAM 用戶的集合。
    - 組內的所有用戶，都會獲得一樣的權限。
- IAM 角色
    - 對服務或資源，臨時授序權限。
    - 沒有用戶名和密碼。
    - 會放棄之前角色的全部權限，僅擁有新角色的權限。

### AWS Organizations 組織

- 集中管理多個 AWS 帳戶
- 服務控制策略 (SCP)
    - 指定組織中成員帳戶的最大權限。
    - 應用於：組織根帳戶、單個成員帳戶、組織單位 (OU)。
    - 影響：所有 IAM 用戶、組、角色，包括 AWS 根用戶。
- 組織單位 (OU)
    - 管理類似業務或安全性的帳戶。
    - 將帳戶放入 OU ，仍可以通過 IAM 繼續為用戶、組、角色提供權限。

---

### Amazon WAF

- Web 應用程序防火牆，過瀘流量且發現攻擊者的簽名。
- 具有機器學習功能，可以識別新威脅並防禦。

### AWS Shield Standard

- 免費服務
- 分析並檢測惡意流量，自動阻止惡意流量。

### AWS Shield Advanced

- 付費服務
- 可與 Amazon CloudFront, Amazon Route 53, Elastic Load Balancing 集成，通過編寫自定義規則，將 AWS Shield 和 AWS WAF 集成，緩解 DDoS 攻擊。