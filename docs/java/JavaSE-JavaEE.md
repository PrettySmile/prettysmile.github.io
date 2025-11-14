---
title: JavaSE & JavaEE
parent: JAVA
---

# JavaSE & JavaEE

參考

https://www.ithome.com.tw/article/124269

### JavaSE

JAVA各應用平台的基礎。

可以分作四個主要的部份：JVM、JRE、JDK與Java語言。

JVM：Java虛擬機器。(JVM是Java程式唯一認識的作業系統，其可執行檔為.class檔案。)

JRE：Java執行環境。

JDK：包括JRE以及開發過程中需要的一些工具程式，像是javac、java等工具程式。

JAVA語言：標準API，提供字串處理、資料輸入輸出、網路套件、使用者視窗介面等功能。(例外（Exception）、群集（Collection）、輸入輸出、執行緒（Thread）)

### JavaEE

以Java SE為基礎。

定義了一系列的服務、API、協定等，

適用於開發分散式、多層式（Multi-tier）、以元件為基礎、以Web為基礎的應用程式，

整個Java EE的體系是相當龐大的，

比較為人熟悉的技術像是JSP、Servlet、JavaMail、Enterprise JavaBeans（EJB）等。

從學習Servlet/JSP開始，Servlet/JSP是執行於Web容器之中，

你必須知道「Web容器是Servlet/JSP唯一認得的HTTP伺服器，

是使用Java撰寫的應用程式，運行於JVM之上」