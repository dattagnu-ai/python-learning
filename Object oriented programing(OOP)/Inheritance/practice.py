class Device:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} is started")


class Phone(Device):
    def __init__(self, name, brand, model):
        super().__init__(name, brand)
        self.model = model

    def start(self):
        print("Congrats")
        Device.start(self)


class Laptop(Device):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

    def start(self):
        print("Laptop boot sequence initiated..")
        Device.start(self)


class Ram(Phone, Laptop):
    def __init__(self, name, model, brand):
        super().__init__(name, model, brand)

    def start(self):
        Phone.start(self)
        Laptop.start(self)


ram = Ram("ASUS", "ROG", "ASUS Gaming")

print("Brand:", ram.brand)
print("Model:", ram.model)
print("Name:", ram.name)
print("\n--- Starting Sequence ---")
ram.start()
print(Ram.mro())
