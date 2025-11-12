---
title: liferay Portal
parent: 執行與部署
---

# 知識: liferay Portal


```$LIFERAY_HOME/data/document_library/```


## 目錄用途
- 存放 所有透過 Portal 上傳的檔案（文件、圖片、PDF、影片…）  
- 每個檔案都有 唯一 UUID 對應資料庫的 DLFileEntry 或 Document 表格紀錄  
- Liferay 會依照公司/群組/資料夾自動建立子目錄來分類檔案  
- 目錄結構通常長這樣： 
```$LIFERAY_HOME/data/document_library/<companyId>/<repositoryId>/<folderId>/<uuid>``` 
- 舉例： 
```/data/document_library/101/201/36520/a3eba684-4b16-a302-e796-0661801a7131 ```
    - 101 → 公司 ID  
    - 201 → repositoryId (通常是本地儲存)  
    - 36520 → folderId  
    - a3eba684-4b16-a302-e796-0661801a7131 → 檔案 UUID

## 檔案如何放進去
檔案不建議直接放進該資料夾，因為 Liferay 會依照資料庫紀錄管理檔案：
1. 透過 Portal 前端上傳
    - 使用「文件與媒體」或「文檔庫」介面 
    - 系統會：
        - 在資料庫 (DLFileEntry、DLFileVersion) 建立檔案紀錄  
        - 依照公司/資料夾/UUID 自動生成路徑，將檔案存放到 ```data/document_library/```   
2. 透過 Liferay API 上傳
    - Java API 或 REST API 可以上傳檔案 
    - 系統同樣會處理資料庫紀錄與實體檔案存放 
3. 不建議直接在檔案系統放檔案
    - 如果你直接放進 ```data/document_library/```，Liferay 無法認得它  
    - 需要有對應的 DLFileEntry 與 DLFileVersion 才能被 Portal 使用

## 注意事項
- 檔案和資料庫是 一對一 關係  
- 移動、刪除、複製檔案最好用 Portal 或 API，不要直接操作檔案系統 
- 若你要備份檔案，建議同時備份：
    - ```data/document_library/``` 目錄  
    - 相關資料庫表 (DLFileEntry、DLFileVersion)


