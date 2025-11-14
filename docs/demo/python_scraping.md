---
title: python 爬蟲練習
parent: DEMO
---

# python 爬蟲練習

1. 下載 python
    <br>
    到 python 官網下載
    ```bash
    python3 --version
    pip3 --version
    ```

2. 安裝套件
    ```bash
    pip3 install requests beautifulsoup4
    # BeautifulSoup4 套件的主要功能就是可以全面解析HTML
    ```    
    
3. 安裝 Selenium
    ```bash
    pip3 install selenium
    # Selenium 能啟動一個真實瀏覽器，等網頁跑完 JavaScript 後，把完整 HTML 抓下來。
    ```

4. 安裝 chromedriver
    
    1. 檢查當前本機 chrome 版本，網址輸入：```chrome://version/```。
    <br>
    顯示：```137.0.7151.120 (正式版本) (arm64) ```

    2. 下載最相近的版本 ```137.0.7151.119```
    <br>
    網址：
    https://developer.chrome.com/docs/chromedriver/downloads

    3. 解壓縮後，放到 ```/usr/local/bin/``` 目錄，即可測試 ```chromedriver --version```。