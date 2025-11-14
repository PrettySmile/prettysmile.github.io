---
title: Docker 指令
parent: Command
---

# Docker 指令

取得映像：
```
docker pull [image]
docker pull mysql:5.6
```

列出本地所有映像
```
docker images
```

映像詳細資訊
```
docker inspcect [image]:[tag]
```

刪除本地映像
```
docker rmi [image]:[tag]
```

映像移植
```
docker save [image]:[tag] > file
docker save xxx:latest > xxx.tar //會產出 xxx.tar 檔案。
```

執行
```shell
docker run

docker run -itd --name mysql -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 mysql:5.6
/*
-it   基本輸入輸出功能
-d    背景運行
-name Container名稱
-e    設置環境變入，設定 MySQL 密碼 MYSQL_ROOT_PASSWORD
-p    將 Container 的 port 對應本機的 port
最後  選擇 images 與版本
*/
```

查詢所有目前 Container 狀態
```
docker ps -a
```


關閉 Container
```
docker stop [Container 名稱]
```


啟動 Container
```
docker start [Container 名稱]
```

進入 Container 內部
```
docker exec -it [Container 名稱] sh
```


