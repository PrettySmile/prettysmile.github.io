---
title: Python 基礎語法學習
parent: Python
nav_order: 1
---

# Python 基礎語法學習

## 基本概念
- Python 是一種
    1. 直譯式
    2. 高階
    3. 動態型別 (變數不用先宣告型別，Python 會自動判斷)
    4. 簡潔易讀 (靠縮排，不靠 {})
- 的語言。

## 常見資料型別
- int
- float
- str
- bool
- list
- dict 字典：```{"name": "Alice", "age": 33}```

```python
name = "Alice"
age = 33
height = 1.65
is_student = false
```

## 運算
### 數學運算
```python
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b) # 除法
print(a // b) # 除法，只取整數
print(a % b) # 除法，只取餘數
print(a ** b) # 次方
```
## 流程控制
```python
# if
age = 20
if age >= 18:
    print("成年")
else:
    print("未成年")
    
# for
for i in range(5):
    print(i)
    
# while
count = 0
while count < 5:
    print(count)
    count += 1
    
```

## Function
```python
def greet(name):
    return f"Hello, {name}"
    
print(greet("Alice"))
```

## list & dict
```python
# list
fruits = ["apple","banana","cherry"]
fruits.append("orange")
print(fruits)
fruits.remove("banana")
print(fruits)
print(fruits[0])

# dict
person = {"name": "Alice", "age": 33}
print(person["name"])
person["age"] = 34
person["city"] = "Taipei"
print(person)
```

## 模組匯入
```python
import math
from datatime import datetime

# 自訂模組
## 例如 app 資料夾，底下有 database.py
from app.database import connect_db
```

## 例外處理
```python
try:
    age = int("abc")
except (ValueError, TypeError):
    print("轉換失敗，或是類型錯誤")
except Exception as e:
    print("其他錯誤", e)
```

## 檔案讀寫
```python
# with：用完自動關閉檔案。
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello")
```

## 推導式
```python
# list
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares) # [1, 4, 9, 16, 25]

# dict
data = {"a": 1, "b": 2, "c": 3}
new = {k: v * 10 for k, v in data.items()}
print(new) # {'a': 10, 'b': 20, 'c': 30}
```

## class 類別
```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hi, I'm {self.name}"

u = User("Alice", 33)
print(u.greet()) # Hi, I'm Alice
```

## Decorator 裝飾器
一種在函式外面加功能的語法糖。
```python
# exam 1
@app.get("/users")
def get_users():
    return ["A", "B"]


# exam 2
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")

say_hi()
# Before
# Hi!
# After
``` 

## 繼承
self: 代表該 class 產生的「實體」（instance）。

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

a = Animal()
print(a.speak()) # 等於呼叫 Animal.speak(a)
b = Dog()
print(b.speak())
```

## Instance Method & Class Method & Static Method
```python
# Instance Method
class A:
    def foo(self):
        print(self)

a = A()
a.foo() # self = 實體


# Class Method
class A:
    @classmethod
    def foo(self):
        print(self)

a = A()
a.foo() # self = 類別A


# Static Method
class A:
    @staticmethod
    def foo(x, y):
        return x + y

print(A.foo(1, 2)) # 沒有 self，不會自動帶入實體或是類別。
```

## Generator 生成器
- 一種特殊 function。
- 一次回傳一個值，用多少才生多少。
- 用於節省記憶體，和處理大量資料流。
- 用 ```yield```，讓 function 變成 特殊function(generator)。

```python
def count_to_three():
    yield 1 # yield: 回傳後暫停，下次再繼續。
    yield 2
    yield 3

g = count_to_three()
print(next(g))
print(next(g))
print(next(g))

for number in count_to_three():
    print(number)



# 通常，陣列會產生全部資料
numbers = [n for n in range(100)]
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# generator，需要才產生
## 注意，這裡用 () 括號
numbers = (n for n in range(100))
print(next(numbers)) # 0
print(next(numbers)) # 1
print(next(numbers)) # 2
```

## 讀大檔案時，使用 yield
```python
# 錯誤方式
with open("big.log") as f:
    lines = f.readlines()

# 正確方式
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line # 一次只讀一行，超省記憶體

for line in read_lines("big.log"):
    print(line)
```

## 有狀態的迭代器，使用 yield
yield 會暫停整個函式，下一次迭代才會從 yield 下一行繼續。
```python
def countdown(n):
    print("Start")
    while n > 0:
        print("run")
        yield n
        n -=1
    print("End")

for x in countdown(3):
    print(x)

# 第一次迭代：
## Start
## run
## 3

# 第二次迭代：
## run
## 2

# 第三次迭代：
## run
## 1

# 第四次迭代：(for 迴圈，會一值呼叫 next()，直到不符合為止，所以會有 4 次迭代)
## End
```

## 繼承 + generator + yield
一旦函式裡出現 yield，整個函式就變成 generator function，所以 crawl() 是 generator。
```python
class BaseSpider:
    def fetch(self, url):
        print("Fetching", url)
        return "<html>...</html>"

class MySpider(BaseSpider):
    def crawl(self):
        urls = ["a.com", "b.com", "c.com"]
        for u in urls:
            content = self.fetch(u)
            yield content

spider = MySpider()
for page in spider.crawl():
    print("Page:", page)

# Fetching a.com
# Page: <html>...</html>
# Fetching b.com
# Page: <html>...</html>
# Fetching c.com
# Page: <html>...</html>
```

## 抽象類別
子類別，需要實作所有抽象方法。
```python
from abc import ABC, abstractmethod

class Animal(ABC): # 抽象類別，一定要繼承 ABC，只有繼承 ABC 才會被當作正式的抽象類別。
    @abstractmethod
    def speak(self):
        pass # 不寫實作

class Dog(Animal):
    def speak(self):
        return "Woof!"

# a = Animal() # 會報錯，因為 抽象類別 無法被建立實體。
b = Dog()
print(b.speak())
```
