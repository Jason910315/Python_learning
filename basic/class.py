
class BankAccount:
    def __init__(self,balance:float = 0.0,password:str = ""):
        self.balance = balance  
        self.__password = password

    def deposit(self,amount:float):
        self.balance += amount

    def withdraw(self,amount:float):
        self.balance -= amount

    def __calculate_fee(self):
        return max(self.__balance*0.01,5)
    
    def withdraw_with_fee(self,amount:float):
        fee = self.__calculate_fee()
        self.balance -= (amount + fee)
        return amount
    
    def check_password(self):
        print(self.__password)
    
    @staticmethod
    def get_maintenance_time(): #靜態方法
        print("Sunday 4:00 ~ 5:00 AM")

#Account = BankAccount(10000,'6124nok45')
#print(Account.balance)
#ccount.check_password()

#Account.get_maintenance_time()
#BankAccount.get_maintenance_time()

#繼承概念
class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self,name,color):
        self.name = super().__init__(name)
        self.color = color
    def sound(self):
        return "旺旺"

animal = Animal("蝙蝠")
dog = Dog("小狗","咖啡色")
x = animal.sound()
y = dog.sound()
print("這隻動物名字是",animal.name,",他的叫聲是",animal.sound())
print("這隻動物名字是",dog.name,",他的叫聲是",dog.sound())

#抽象化
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "汪汪！"

class Cat(Animal):
    def sound(self):
        return "喵喵！"

# 創建動物的物件
dog = Dog("旺財")
cat = Cat("小花")

# 使用物件的方法
print(dog.name + "發出聲音：" + dog.sound())
print(cat.name + "發出聲音：" + cat.sound())
