class Car:
    def drive(self):
        print("Car is driving")


class Bus:
    def drive(self):
        print("Bus is driving")


class Bike:
    def drive(self):
        print("Bike is driving")


car = Car()
bus = Bus()
bike = Bike()

vehicles = [car, bus, bike]
for vehicle in vehicles:
    vehicle.drive()
