---
title: pm2 指令
parent: Command
---

# pm2 指令

| cd /root/.pm2/logs/ | 看LOG |
| --- | --- |
| pm2 start .\epgs.js -i 2 | 平行拓展成2個 |
| pm2 start <app-name> |  |
| pm2 stop xx | 注意，有cron restart(定期重啟)的要delete，不然會重啟。 |
| pm2 delete xx | 注意，有cron restart(定期重啟)的要delete，不然會重啟。 |
| pm2 show xx |  |
| pm2 logs |  |
| pm2 log xx |  |
| pm2 save | 機器重啟，會叫起所有的服務，若有start或delete等，需儲存狀態。 |
| pm2 list |  |
| pm2 restart xx | 不論是否運作中，重啟 |
| pm2 reload 18
pm2 reload match-epg-api | 會等request結束，才重啟
(API要注意，需使用這個，並只啟用一台測試，沒問題再全部的平行拓展都重啟) |
| pm2 exec <app-name> |  |