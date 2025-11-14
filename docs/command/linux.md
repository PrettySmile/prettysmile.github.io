---
title: Linux 指令
parent: Command
---

### 查詢哪個程式正在使用 3000 port
```sh
lsof -i :3000
```
- lsof = List Open Files 列出所有被程式打開的「檔案」。
- -i = Internet 查網路連線、port 等資訊。


### 把文字，編碼成 Base64。
```
echo xxx | base64
```

### 把 Base64 編碼，還原回原始文字。
```
echo xxx | base64 -d
```


## |

管道

管道是Linux，Unix都有的概念，是非常基礎，也是非常重要的一個概念。它的作用是將｜（左邊）命令的輸出作為後（右邊）的命令的輸入()。

```
ls | grep all
```

## ;

多個語句放在同一行時，可使用分隔號，亦可連續指令。

```
# 查看aaa及bbb文件的後幾行
tail aaa.txt; tail bbb.txt
```

## ;;

在使用case選項的時候，作為每個選項的終結符。

## .

一個點代表當前目錄，兩個點代表上層目錄。

## <<

將後繼的內容重定向到左側命令的輸入中。