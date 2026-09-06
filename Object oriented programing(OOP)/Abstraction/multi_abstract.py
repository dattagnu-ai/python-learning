from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass


class UPI(Payment):
    def pay(self):
        print("Payment Through UPI")

    def refund(self):
        print("Refund through UPI")


upi = UPI()
upi.pay()
upi.refund()

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("car started")


car = Car()
car.start()
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment through UPI")

    def refund(self):
        print("refund through UPI")


upi = UPI()

upi.pay()
upi.refund()

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def area(self):
        print("Circle area")


class Square(Shape):
    def area(self):
        print("Square of area")


circle = Circle()
square = Square()

circle.area()
square.area()
