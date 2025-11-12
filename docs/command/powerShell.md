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
(Ailsa：不需要打包，因為包出來的JAR HASH不會一樣，差異在打包的時間記錄)
```
jar -cvf xxx.jar -C . .
```
