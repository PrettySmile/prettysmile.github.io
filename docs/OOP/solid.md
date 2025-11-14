---
title: SOLID
parent: OOP
---

# SOLID

> SOLID 是 OOP 的核心原則。

在物件導向設計上，為了讓軟體維護、開發，變得更容易的五個原則

- [**S**ingle Responsibility Principle (SRP) 單一職責原則](https://medium.com/@f40507777/%E5%96%AE%E4%B8%80%E8%81%B7%E8%B2%AC%E5%8E%9F%E5%89%87-single-responsibility-principle-7b4eb03f1fff)
- [**O**pen-Closed Principle (OCP) 開放封閉原則](https://medium.com/@f40507777/%E9%96%8B%E6%94%BE%E5%B0%81%E9%96%89%E5%8E%9F%E5%89%87-open-closed-principle-31d61f9d37a5)
- [**L**iskov Substitution Principle (LSP) 里氏替換原則](https://medium.com/@f40507777/%E9%87%8C%E6%B0%8F%E6%9B%BF%E6%8F%9B%E5%8E%9F%E5%89%87-liskov-substitution-principle-adc1650ada53)
- [**I**nterface Segregation Principle (ISP) 介面隔離原則](https://medium.com/@f40507777/%E4%BB%8B%E9%9D%A2%E9%9A%94%E9%9B%A2%E5%8E%9F%E5%89%87-interface-segregation-principle-isp-6854c5b3b42c)
- [**D**ependency Inversion Principle(DIP) 依賴反轉原則](https://medium.com/@f40507777/%E4%BE%9D%E8%B3%B4%E5%8F%8D%E8%BD%89%E5%8E%9F%E5%89%87-dependency-inversion-principle-dip-bc0ba2e3a388)


> SOLID算是寫軟體需要學會的內功，只要是物件導向語言都可以使用。


## 目的：
1. 低耦合
2. 高內聚
3. 降低程式碼壞味道

透過分離與 clean code 來提高可讀性會讓你的程式碼等同於設計文件。

## 解析：
### SRP 單一職責原則
- 修改一個類應該只為一個理由。
- 這是因為，當有很多方法在類中時，修改其中一處，你很難知曉在程式碼庫中哪些依賴的模組會被影響到。

### OCP 開放封閉原則
- 在不改變已有程式碼的情況下增加新的功能**

### LSP里氏替換原則
- 在不改變原有結果正確性的前提下父類和子類可以互換。
- 子類別應該可以替換掉父類別而不影響程式架構。
- 子類別應該可以執行父類別想做的事情。

#### 如何降低違反LSP情形？
- 避免繼承: 盡量利用組合。

### ISP介面隔離原則
- 客戶端不應該被強制去實現於它不需要的介面
- 把不同功能的從介面中分離出來。

### DIP 依賴反轉原則
- 高階的模組不應該依賴低階的模組，它們都應該依賴於抽象。
- 抽象不應該依賴於實現，實現應該依賴於抽象。
- 不要把程式碼寫死某種實作上。
