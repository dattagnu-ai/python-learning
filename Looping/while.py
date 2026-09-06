# num = 1

# while num < 5:
#     print(num)
#     num = num + 1

# num = 1

# while num < 11:
#     print(num)
#     num = num + 1

# num = 1

# while num < 10:
#     if num % 7 == 0:
#         print(num)
#     num = num + 1

# num = int(input("Enter a number:- "))
# while num <= 0:
#     num = int(input("Enter a number:- "))
# print(f"positive number:- {num}")


products = {
    "laptop": 50000,
    "phone": 20000,
    "tablet": 30000,
    "earphones": 5000,
    "charger": 1500,
}
index = 0
total = 0

key = list(products.keys())

while index < len(key):
    total = total + products[key[index]]
    index += 1
average = total / len(key)
index = 0

while index < len(key):
    name = key[index]
    price = products[name]
    if average < price:
        print(name, price)
    index += 1
