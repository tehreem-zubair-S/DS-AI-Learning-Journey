from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class Cash(Payment):
    def pay(self, amount):
        print(f"Paid {amount} in Cash")

p1 = CreditCard()
p2 = Cash()

p1.pay(500)
p2.pay(300)
