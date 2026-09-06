from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle stopped")


class Car(Vehicle):
    def start(self):
        print("car started")


class Bike(Vehicle):
    def start(self):
        print("Bike started")


car = Car()
bike = Bike()

car.start()
car.stop()

bike.start()
bike.stop()

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def area(self):
        print("Circle area")


class Square(Shape):
    pass


circle = Circle()
square = Square()
