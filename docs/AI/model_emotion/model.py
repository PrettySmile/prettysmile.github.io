import torch
import torch.nn as nn
import torch.optim as optim

# ----------------------------------------------------------
# 1. 建立文字轉數字
# ----------------------------------------------------------
def build_vocab(sentences): # 把所有出現的單字對應到整數索引
    vocab = {}
    idx = 0
    for s in sentences:
        for w in s.lower().split(): # 以空白拆單字
            if w not in vocab:
                vocab[w] = idx
                idx += 1
    return vocab


def sentence_to_vector(sentence, vocab): # 把句子變成數字向量
    vec = torch.zeros(len(vocab))
    for w in sentence.lower().split():
        if w in vocab:
            vec[vocab[w]] += 1
    return vec


# ----------------------------------------------------------
# 2. 建立模型（線性 + Sigmoid）
# ----------------------------------------------------------
class TestModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.linear = nn.Linear(vocab_size, 1)  # 輸入 vocab_size(字典長度)，輸出 1。
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        return self.sigmoid(self.linear(x)) # Sigmoid（二分類） # 把向量映射到 0~1 的機率


# ----------------------------------------------------------
# 3. 開始訓練
# ----------------------------------------------------------
if __name__ == "__main__":
    # 3-1 訓練資料
    training_data = [
        ("I love this movie", 1),
        ("This is amazing", 1),
        ("I hate this", 0),
        ("This is terrible", 0),
    ]

    # 3-2 取出所有句子建立字典
    sentences = [s for s, _ in training_data]
    vocab = build_vocab(sentences)

    print("字典內容：", vocab) # 字典內容： {'i': 0, 'love': 1, 'this': 2, 'movie': 3, 'is': 4, 'amazing': 5, 'hate': 6, 'terrible': 7}

    # 3-3 建模型
    model = TestModel(len(vocab)) # 字典長度，決定向量的長度。
    criterion = nn.BCELoss() # BCELoss = 二元分類常用的損失函數，用來衡量二分類預測（輸出在 0~1）和真實標籤（0 或 1）間的差距。
    optimizer = optim.Adam(model.parameters(), lr=0.1)

    # 3-4 訓練迴圈
    for epoch in range(2000):
        total_loss = 0
        for sentence, label in training_data:
            x = sentence_to_vector(sentence, vocab)
            # x = "I love this movie" = tensor([1., 1., 1., 1., 0., 0., 0., 0.])
            # x = "This is amazing" = tensor([0., 0., 1., 0., 1., 1., 0., 0.])
            y = torch.tensor([label], dtype=torch.float32)

            pred = model(x)
            loss = criterion(pred, y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        if epoch % 200 == 0:
            print(f"Epoch {epoch}, Loss={total_loss:.4f}")

    # 3-5 儲存模型 + 字典
    torch.save({
        "model": model.state_dict(),
        "vocab": vocab
    }, "sentiment_model.pth")

    print("\n訓練完成，模型已儲存！")
