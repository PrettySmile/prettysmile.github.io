---
title: 安裝
parent: Docker
---
# Docker 安裝

## 安裝

1. 安裝 docker <br> https://www.docker.com/products/docker-desktop
2. 安裝 WSL2 Linux 核心 <br> https://docs.microsoft.com/zh-tw/windows/wsl/wsl2-kernel

## 步驟

1. 先確認本機 docker 環境正常運行，開啟 PowerShell，建入 docker。
    - 指令
    ```
    docker
    ```
2. 登入docker hub。
    - 指令
    ```
    docker login --username account password
    ```

---

### 步驟

1. 切到本機專案資料夾下。
2. 把本機的專案資料夾，打包成 images。(會依據 Dockerfile 檔案執行)
    - 指令
        
        ```
        docker build -t {packageName}/{imageName}:latest .
        ```
        
    - 解釋
        - t 為 image 加上 tag。
3. 列出本機全部的 docker image。
    - 指令
        
        ```
        docker images
        ```
        
4. 將打包完成的 docker，丟上 docker hub。
    - 指令
        
        ```
        docker push {packageName}/{imageName}:latest
        ```
        
5. 登入 VM 機器。
    
6. 從 docker hub上，將剛剛丟上去的最新的 images，拉取下來。
    - 指令
        
        ```
        docker pull {packageName}/{imageName}:latest
        ```
        
7. 查看目前的機器執行狀態。
    - 指令
        
        ```
        docker ps -a
        ```
        
8. 停止指定 container。
    - 指令
        
        ```
        docker stop {imageName}
        ```
        
9. 移除指定container。
    - 指令
        
        ```
        docker rm {imageName}
        ```
        
10. 產生 container，產生完畢後會自動運行。
    - 指令
        
        ```
        docker run --name {imageName} -p 94:94 -p 9100:9100 -v /etc/localtime:/etc/localtime:ro -v /home/xxx/tools/syncData/syncConfig:/home/webserver/tools/syncData/syncConfig --add-host='db:00.00.00.00' --add-host='xx:00.00.00.00' --network zzz -d -it {packageName}/{imageName}:latest
        ```
        
    - 解釋
        - name 替 Container取一個別名。
        - p 將主機的 Port 綁定到 Container 的 Port。
        - v 掛載目錄，意指把本機的目錄掛載到 Container 的目錄，達到共享目錄的效果。
        - d 背景執行。
        - i -t 可合併成 ```-it```, 意指給 Container 標準輸出輸入的能力。
    - 備註：
        
        此階段如果要除錯，則建入。
        
        差異在於：字尾後段加 sh，並且拿掉 -d(背景執行)。
        
        ----------分隔線----------
        
        ```
        docker run --name {imageName} -p 94:94 -p 9100:9100 -v /etc/localtime:/etc/localtime:ro -v /home/xxx/tools/syncData/syncConfig:/home/webserver/tools/syncData/syncConfig --add-host='db:00.00.00.00' --add-host='xx:00.00.00.00' --network zzz -it {packageName}/{imageName}:latest sh
        ```
        
11. 進入運行中的container。
    - 指令
        
        ```
        docker exec -it {imageName} sh
        ```
        
12. 將專案跑起來。
    - 指令
        
        ......etc如本機流程。
        
        ```
        pm2 start
        ```
        
13. 回到dev機，建入exit。
    - 指令
        
        ```
        exit
        ```
        
14. 回到本機，再次建入exit。
    - 指令
        
        ```
        exit
        ```
        

### 小備註

- 過程中若有任何找不到檔案/無法執行的問題，注意編碼，以及換行格式。

---

---

---
## 問題：
我用 docker 啟了一個 mysql 的 container。
我想要再那個 container 裡面，也有一個 docker 可以用?
還是我應該要把 docker 和 mysql 包在一起變 images?

## 解法：
1. 可以到 container 裡面裝你要的，然後再包成自己獨特的 image。
2. 用 dockerfile 的方式，寫個腳本在運行的時後依照自己的需求生成特定的 image。

