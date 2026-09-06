from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def Pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass

    def recept(self):
        print("Recept Generated")


class UPI(Payment):
    def Pay(self):
        print("Payment Through UPI")

    def refund(self):
        print("Refund Through UPI")


class Card(Payment):
    def Pay(self):
        print("Payment Through Card")

    def refund(self):
        print("Refund Through Card")


class Cash(Payment):
    def Pay(self):
        print("Payment Through Cash")

    def refund(self):
        print("Refund Through Cash")


upi = UPI()
card = Card()
cash = Cash()

upi.Pay()
upi.refund()
upi.recept()
print("--------------------")
card.Pay()
card.refund()
card.recept()
print("--------------------")
cash.Pay()
cash.refund()
cash.recept()
