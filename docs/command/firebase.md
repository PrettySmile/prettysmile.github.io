---
title: Firebase 指令
parent: Command
---

# Firebase 指令

## Hosting 託管

安裝
```bash
npm install -g firebase-tools # mac 電腦要加 sudo
```

登入
```bash
firebase login
```

在前端專案的根目錄執行
```bash
firebase init
# 選擇Hosting就好
# 注意資料夾要選擇=> dist/專案名稱
```

發佈到 Hosting 上面（公開出去）
```bash
#ng build ##若用 Angular，記得要先 build
firebase deploy
```

預覽發布（不公開出去）

```bash
firebase hosting:channel:deploy {projectId}
```