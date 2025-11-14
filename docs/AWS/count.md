---
title: 計算
parent: AWS
---

# 計算

## 消息收發和隊列

### Amazon Simple Notification Service (Amazon SNS)

- 發佈/訂閱服務。
- 訂閱者可以是：Web服務器、電子郵件、AWS Lambda等。

### Amazon Simple Quene Service (Amazon SQS)

- 消息隊列服務。
- 在軟件組件之間發送、存儲、接收消息，不會丟失。



## 其他計算服務

### AWS Lambda

上傳代碼 → 觸發事件 → 按使用時間付費。

### Amazon Elastic Container Service (Amazon ECS)

- 可擴展的容器管理系統。
- 支持：Docker。
- 借助 ECS ，可用 API 來啟動和停止 Docker

### Amazon Elastic Kubernetes Service (Amazon EKS)

- 完全託管。
- 在 AWS 上，使用 Kubernetes

### Amazon Fargate

- 用於容器的，無服務器計算引擎。
- 可與 Amazon ECS 和 Amazon EKS 一起使用。