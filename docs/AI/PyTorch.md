---
title: PyTorch
parent: AI
---

# PyTorch

## 介紹
- 目前最流行、學界與業界主流的<span class="bg-yellow-000">機器學習</span>框架。
- 讓工程師能更快寫出神經網路。
- 我們只需專注在模型本身，而不是底層矩陣計算。
- 大部分 LLM（GPT）都是基於 PyTorch。
- PyTorch 只是一個框架，幫你處理 AI 模型的工具，就像程式套件一樣。


### AI 模型 以及 訓練? 
> AI 模型只是一個會自動猜答案的小盒子。<br>
> 需要給它大量問題以及正確答案，去訓練他。<br>
> 讓它知道，它每次猜測的答案，距離正確答案有多遠。<br>
> 然後它會自己去調整，讓自己下一次猜測時，能越靠近正確答案(這就是變聰明的過程)。

> 例如：<br>
> 小明每次說「這張圖片是狗」，然後 AI 猜錯了 → 它就改答案。<br>
> 猜錯 → 修改<br>
> 猜錯 → 修改<br>
> 猜錯 → 修改<br>
> 猜對 → 修改很少<br>
> 
> 這就是 AI 訓練。（就是這麼簡單）

<br>

---

<br>

## 安裝步驟
1. Python 3.10+。

2. 確認 python 可運行。
  - windows：
    ```bash
      py --version
    ```
  - mac：
    ```
      python3 --version
    ```

3. 確認 pip 可運行
  - windows：
    ```bash
      pip --version
    ```
    不行的話，需加入環境變數 ```C:\Users\{使用者}\AppData\Local\Programs\Python\Python314\Scripts```。
  - mac：
    ```
      pip3 --version
    ```

4. 安裝套件
    ```bash
      pip install torch
    ```

---

## PyTorch 專案的標準做法：
訓練 → 儲存 → 預測。

> 一支程式：只負責 ```訓練模型及儲存結果```。<br>
> 另一支程式：只負責 ```載入模型及預測```。<br>

<br>

---

<br>

## 🤖 手動實作，讓 AI 學會：<br>「依照不同溫度，自動判斷喝水量」


### 2️⃣ 準備資料(問題以及正確答案)：

| 氣溫 | 喝水量 |
| ---- | ---- |
| 20 度 | 500 ml |
| 25 度 | 700 ml |
| 30 度 | 900 ml |

預期 AI 會學到：
```👉 喝水量 ≈ 氣溫 x 某個數字```

> AI 會自己找出那個數字，不用我們教它數學，它會自己找答案。


## 3️⃣ 執行「訓練」檔案 (water_model.py)
```bash
  py .\model.py
```
![alt text](../../assets/images/AI/image-01.png)

> 結果解讀：<br>
> 模型學到的 weight（斜率）≈ 40.00 <br>
> 模型學到的 bias（截距）≈ -300.00 <br>
> 這代表 AI 學到的公式是：```👉 喝水量 ≈ 氣溫 × 40 + -300``` <br>
> 可以看到 AI 已經成功「學會」了規律。


## 4️⃣ 執行「預測」檔案 (predict_model.py)
```bash
  py .\predict.py
```
![alt text](../../assets/images/AI/image-02.png)

> 結果解讀：<br>
> 氣溫 28 度 → 喝水量 ≈ 28 × 40 + (-300) ≈ 820 ml
