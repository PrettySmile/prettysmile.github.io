---
title: GIT 指令
parent: Command
---

# GIT 指令

### 還原所有 ```異動的檔案``` 到 ```乾淨的分支```。
```
git restore .
git clean -fd
```

### 專案指到哪個 repo
```
git remote -v
```

### 刪除本地所有 tag
```
git tag | foreach-object -process { git tag -d $_ }
```

### 整合成一個 commit
```bash
# step 1:
# N=要壓縮的commit數量
git rebase -i HEAD~N

# step 2:
# 除了第一個commit，其他commit 從 pick 改成 squash

# step 3:
# 修正 commit 訊息

# step 4:
git push origin feat/live-video --force
```

請注意，如果分支有 merge 到 dev 的話。

那 dev 的程式會是舊的!!!!!!!!!!! 曾經在 rebase 前的一些爛 code，已經被合上 dev 了!!!!!!!!!!


### 徹銷 commit (保留程式碼)
```bash
git reset --soft HEAD~1
```

### 查看目前所在 commit
```bash
git log --oneline -1
```

若已 push，想撤回
(注意，遠端強制回滾，可能影響他人!)
```bash
# 先做上述「徹銷commit(保留程式碼)」
git push --force
```

---

### 目前分支，回復到先前的版本

```bash
git reset --hard dd6e8d5
⚠️ --hard 這個操作會遺失所有未提交的變更！
```

(注意，遠端強制回滾，可能影響他人!)

```bash
git push --force
```

---

如果我無法commit的話，可以用 -n 忽略告警，提交commit

例如：想跳過commit發生ESLint錯誤

```bash
git commit -n -m "你的提交資料"
```

---

### merge 遇到衝突，想取消 merge 怎麼辦

```bash
git merge --abort
```

### 看分支的歷史

```bash
git log
```