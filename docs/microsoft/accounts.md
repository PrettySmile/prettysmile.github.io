---
title: 帳號類型
parent: Microsoft
---

- `UserMailbox` → 個人信箱
- `SharedMailbox` → 共用信箱
- `GroupMailbox` → Microsoft 365 群組信箱

## 🏷️ Microsoft 帳號類型比較

| 類型 | 是否有 AD 身分 (能登入) | 需要授權 (License) | 是否能收發郵件 | 能否單獨登入 (Outlook/Teams) | 常見用途 |  |
| --- | --- | --- | --- | --- | --- | --- |
| **User Account (使用者帳號)** | ✅ 有 | ✅ 要授權 (E3/E5, Business Standard 等) | ✅ 有獨立信箱 | ✅ 可以 | 員工日常帳號 | 密碼會過期 |
| **Service Account (服務帳號)** | ✅ 有 | ✅/❌ 視需求 (通常會買最便宜的 License 或只開郵件) | ✅ 可設定信箱 | ✅ 可以 (但常限制互動) | 系統整合、自動化 (Power Automate, API) | 特殊 User，用來跑流程、API、Power Automate。 <br> 只能登入主機用，申請時會詢問要用哪個主機。 |
| **Shared Mailbox (共用信箱)** | ❌ 沒有 (需掛在使用者底下) | ❌ 不需授權（<50GB），大於需授權 | ✅ 可收發，但不能獨立登入 | ❌ 不行，只能透過有權限的 User 使用 | 共用信箱，如 hr@company.com, it-support@ | 不需授權，不能自己登入，必須透過使用者掛載。 <br> 不能綁授權。 <br> CIPortal |
| **Resource Mailbox (資源信箱)** | ❌ 沒有 | ❌ 不需授權 | ✅ 可收會議邀請，有限制 | ❌ 不行 | 預約用，例如會議室、設備 | 專門給會議室、設備預約。 |
| **Group Mailbox (M365 Group)** | ❌ 沒有 | ❌ 不需授權 (包含在群組服務裡) | ✅ 有群組收件匣 | ❌ 不行，僅能透過群組成員存取 | Microsoft 365 群組收件匣，團隊協作 | 綁 Microsoft 365 群組，常見於「When a new email arrives in a group」的 Power Automate 是群組型態，不會單獨擁有權限。 |
| **Guest Account (來賓帳號)** | ❌ 沒有 (外部使用者) | ❌ 不需授權 (由邀請方付費) | ❌ 沒有信箱 | ✅ 可登入 Teams/SharePoint | 外部協作（合作廠商、顧問） | 外部人員，被邀請進 Teams/SharePoint |
| **Personal Microsoft Account (MSA)** | ✅ 有 (但非公司 AD) | ❌ 免費 (Hotmail, Outlook.com) | ✅ 有個人信箱 | ✅ 可以 (Outlook.com, OneDrive) | 個人帳號，不屬於公司環境 | 個人帳號，不在公司控制範圍 |