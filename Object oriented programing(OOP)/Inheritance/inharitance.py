# Vehicle मध्ये start() method असावा.
# Vehicle.start() → "Vehicle started" print करावा.
# Car ही Vehicle ची child class असावी.
# Car मध्ये स्वतःचा start() method बनव.
# Car.start() मध्ये आधी parent चा start() चालला पाहिजे.
# त्यानंतर "Car started" print झालं पाहिजे.
# शेवटी Car object तयार करून start() call कर.


class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):

    def start(self):
        super().start()
        print("Car started")


car = Car()
car.start()
