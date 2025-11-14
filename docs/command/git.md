---
title: GIT 指令
parent: Command
---

# GIT 指令

還原所有 ```異動的檔案``` 到 ```乾淨的分支```。
```
git restore .
git clean -fd
```

專案指到哪個 repo
```
git remote -v
```

刪除本地所有 tag
```
git tag | foreach-object -process { git tag -d $_ }
```