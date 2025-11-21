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