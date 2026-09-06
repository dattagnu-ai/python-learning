class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

    def __add__(self, other):
        total_name = f"{self.name} + {other.name}"
        total_price = self.price + other.price
        return Product(total_name, total_price)


class DigitalProducts:
    def display(self):
        print("Digital product")


class PhysicalProduct:
    def display(self):
        print("Physical product")


p1 = Product("Laptop", 50000)
p2 = Product("Phone", 30000)


print(p1)
print(p2)
result = p1 + p2
print(f"Total:- {result}")
print(f"Total cost:- {result.price}")
result = p1 == p2
print(f"Equal price:- {result}")
result = p1 > p2
print(result)
products = [DigitalProducts(), PhysicalProduct()]
for product in products:
    product.display()
