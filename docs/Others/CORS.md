---
title: CORS
parent: Others
---

# CORS
當你在 **開發環境** 使用 **React 前端** 和 **Express 後端** 進行 API 請求時，通常會遇到 **CORS (Cross-Origin Resource Sharing) 限制**。

### **1. 為什麼會有 CORS 問題？**

- **React 開發伺服器** 預設在 `http://localhost:3000`
- **Express 伺服器** 預設在 `http://localhost:5000`
- 當 React 發送請求到 Express 時，這屬於「跨域請求」（不同的 port），瀏覽器會阻擋請求，導致 **CORS 錯誤**。

例如，如果 React 嘗試這樣請求 Express：

```
fetch("http://localhost:5000/api/hello")
  .then((res) => res.json())
  .then((data) => console.log(data))
  .catch((err) => console.error(err));
```

**錯誤訊息**：

```
Access to fetch at 'http://localhost:5000/api/hello' from origin 'http://localhost:3000' has been blocked by CORS policy.
```

這是因為瀏覽器保護機制，不允許前端對 **不同來源 (different origin)** 進行 API 請求。

---

### **2. 如何解決？**

有兩種方法：

### ✅ **方法 1：在 Express 允許 CORS（手動設定 CORS）**

這是最直接的方法，在 `backend/app.js` 加入：

```
const cors = require("cors");

app.use(cors()); // 允許所有跨域請求
```

這樣，Express 會允許來自任何來源（`*`）的請求。

⚠️ **但這個方式只適合開發環境，不適合正式環境，因為它允許來自任何來源的請求，可能帶來安全風險！**

---

### ✅ **方法 2：設定 React** **`proxy`（推薦）**

為了 **避免手動設定 CORS**，你可以在 React 的 `package.json` 設定 `proxy`：

```
"proxy": "http://localhost:5000"
```

這樣，當 React 內部發送請求時：

```
fetch("/api/hello")
```

React 會自動將請求 **代理** 到 `http://localhost:5000/api/hello`，就像是它們在同一個伺服器上運行，因此不會觸發 CORS 限制。

### **🔹 Proxy 設定步驟**

1️⃣ **在** **`frontend/package.json`** **加入**：

```
"proxy": "http://localhost:5000"
```

2️⃣ **修改** **`frontend/src/App.js`，不要寫完整 URL**：

```
fetch("/api/hello")
```

**不要寫**

```
fetch("http://localhost:5000/api/hello")
```

3️⃣ **重新啟動 React 開發伺服器**：

```
cd frontend
npm start
```

---

### **3. Proxy vs. 手動 CORS，哪個比較好？**

| 方式 | 優點 | 缺點 |
| --- | --- | --- |
| **Express** **`cors()`** | 快速解決 CORS 問題 | 需要手動設定，正式環境不安全 |
| **React** **`proxy`** | 開發時更方便，不會有 CORS 問題 | 只適用於 `npm start`（開發環境），部署後無效 |

✅ **開發環境建議使用** **`proxy`**，避免 CORS 問題。

🚀 **正式環境應該透過 Nginx 反向代理或設定正確的 CORS 規則**。

這樣可以讓你的 Express + React 全棧開發體驗更流暢！😉