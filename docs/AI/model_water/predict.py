# 預測檔
import torch
import torch.nn as nn
from model import TestModel  # 只匯入模型類別

# 2️⃣ 建立模型
model = TestModel()

# 3️⃣ 載入訓練結果
model.load_state_dict(torch.load("result.pth"))

# 4️⃣ 切換到評估模式（只做預測，不計算梯度）
model.eval()

# 5️⃣ 丟新資料進去預測
x_new = torch.tensor([[28.0]], dtype=torch.float32)  # 新的氣溫
y_pred = model(x_new)

print("28 度喝水量預測:", y_pred.item())
