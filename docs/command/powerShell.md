---
title: PowerShell 指令
parent: Command
---

# PowerShell 指令


## 如何取得 JAR 檔案的 HASH 值
```
get-filehash xxx.jar -Algorithm SHA256
```

## 解壓 .jar 檔
```
jar -xvf xxx.jar
```

## 計算 JAR 所有 class 檔 hash
```
Get-ChildItem -Recurse ".\jar-old" -Include *.class |
    Get-FileHash | Sort-Object Path > old-hashes.txt
```

<br>

---

## jar 指令打包
(Ailsa：每次打包出來的 JAR，HASH 都會不一樣，因為 JAR 中會記錄打包的時間)
```
jar -cvf xxx.jar -C . .
```
