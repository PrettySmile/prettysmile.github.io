import torch
from model import TestModel, sentence_to_vector

# 載入模型與字典
saved = torch.load("result.pth")

vocab = saved["vocab"]
model = TestModel(len(vocab))
model.load_state_dict(saved["model"])
model.eval()

# 要測試的句子
text = "I love it"

# 文字轉向量（注意：如果句子裡有 vocab 沒有的字，會被忽略）
x = sentence_to_vector(text, vocab)

# 預測
pred = model(x).item()

if pred >= 0.5:
    print(f"句子：{text}\n情緒：正向 😀 ({pred:.2f})")
else:
    print(f"句子：{text}\n情緒：負向 😠 ({pred:.2f})")
