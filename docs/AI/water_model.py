# 訓練檔

import torch
import torch.nn as nn
import torch.optim as optim

# -----------------------------------------------------------
# 1. 建立一個 AI 小盒子，此處只有一個線性層。
# -----------------------------------------------------------
class WaterModel(nn.Module): # nn.Module 是 PyTorch 裡的「模型基底類別」。
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1) # Linear(1, 1) 表示：輸入特徵數（氣溫只有一個數字），輸出特徵數（喝水量只有一個數字）。

    def forward(self, x): # 模型「前向傳遞」的規則  #每次我們把資料丟進模型，PyTorch 就會自動呼叫 forward(x)。
        return self.linear(x)


if __name__ == "__main__":
    # -----------------------------------------------------------
    # 2. 準備訓練資料
    #    注意：在 PyTorch 裡，資料都是「矩陣（Tensor）」，此處為 2D，是二維陣列。
    # -----------------------------------------------------------
    x = torch.tensor([[20.0], [25.0], [30.0]])  # 氣溫（input）
    y = torch.tensor([[500.0], [700.0], [900.0]]) # 喝水量（output）    # 3 筆資料，每筆資料 1 個特徵。


    model = WaterModel() # 初始化模型

    # -----------------------------------------------------------
    # 3. 設定「AI 怎麼學」：
    #    設定 損失函數 criterion
    #    設定 優化器 optimizer
    #         lr = learning rate = 學習率 → 每次修正幅度
    #         lr = 0.01, Loss = nan, 代表 AI 看到自己猜錯，一次改超大，導致離正確答案超級遠，計算 Loss 時數字爆掉了。
    #                                這叫 梯度爆炸 (Gradient Explosion) 或 模型發散 (Divergence)。
    # -----------------------------------------------------------
    criterion = nn.MSELoss() # MSE → 平方誤差平均 → 適合數值預測問題（Regression） 

    # 這裡有 2 種優化器：SGD 以及 Adam。
    # optimizer = optim.SGD(model.parameters(), lr=0.001)  # SGD = 固定大小的步伐。
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01) # Adam = 會自動調整步伐(更聰明更穩)。


    # -----------------------------------------------------------
    # 4. 開始訓練，設定學習次數
    # -----------------------------------------------------------
    for epoch in range(50001):
        # 讓模型根據「氣溫x」猜「喝水量y」。
        pred = model(x)

        # 看看猜得離正確答案，相差多少。
        loss = criterion(pred, y) # pred = AI 的猜測, y = 喝水量y (真實答案), loss = AI 的猜測距離正確答案的偏差。

        # 清空前一次的梯度，確保每一次修正都是「針對這一次輸入」。
        optimizer.zero_grad()

        # PyTorch 會自動計算每個參數（weight / bias）應該往哪個方向改，以及改多少 → 這就是梯度（gradient）。
        loss.backward()

        # 更新模型參數，optimizer 會按照梯度 + learning rate → 更新 weight / bias。
        optimizer.step()

        # 每 N 次印一次，看訓練狀況
        if epoch % 5000 == 0:
            print(f"Epoch {epoch} Loss = {loss.item():.4f}") # Loss 越小越好，越接近正確答案! 0=模型幾乎完美。


    # -----------------------------------------------------------
    # 5. 訓練完成
    # -----------------------------------------------------------
    weight = model.linear.weight.item()
    bias = model.linear.bias.item()

    print("\n===== 訓練結束 =====")
    print(f"模型學到的 weight（斜率）≈ {weight:.2f}")
    print(f"模型學到的 bias（截距）≈ {bias:.2f}")

    torch.save(model.state_dict(), "water_model.pth") # state_dict() → 取得模型所有參數（weight, bias…），並儲存。

    print("模型訓練完成並儲存！")
