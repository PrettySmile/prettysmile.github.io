# 預測檔

# predict_model.py
import torch
import torch.nn as nn
from water_model import WaterModel  # 只匯入模型類別

# 2️⃣ 建立模型
model = WaterModel()

# 3️⃣ 載入已存好的權重
model.load_state_dict(torch.load("water_model.pth"))

# 4️⃣ 切換到評估模式（只做預測，不計算梯度）
model.eval()

# 5️⃣ 丟新資料進去預測
x_new = torch.tensor([[28.0]], dtype=torch.float32)  # 新的氣溫
y_pred = model(x_new)

print("28 度喝水量預測:", y_pred.item())
