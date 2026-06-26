# Printing values only

fruits = {"apple": 10, "banana": 5, "mango": 20}

for key, value in fruits.items():
    print(value)

# printing key and value
fruits = {"apple ": 10, "banana": 5, "mango": 20}

for key, value in fruits.items():
    print(f"{key} Costs {value} Rupees")

# Marks

students = {"Dattu": 85, "Lokesh": 42, "shreya": 76, "Dikesh": 38}
for key, value in students.items():
    if value > 50:
        print(key, value)


# Converting keys to list for indexing
students = {"Dattu": 85, "Rahul": 42}
keys = list(students.keys())
print(keys)
print(keys[0])
print(keys[1])


# Accessing key and value using direct index

students = {"Dattu": 85, "Rahul": 42}
keys = list(students.keys())
print(students[keys[0]])
print(students[keys[1]])


# Looping dict using range() and index

students = {"Dattu": 85, "Rahul": 42, "Priya": 76}
keys = list(students.keys())
for index in range(len(students)):
    r = index + 1
    name = keys[index]
    score = students[keys[index]]
    print(f"{r}. {name} - {score}")


# Numbered list from dict using range() and keys

products = {"laptop": 50000, "phone": 20000, "tablet": 30000, "earphones": 5000}
key = list(products.keys())
for i in range(len(products)):
    r = i + 1
    item = key[i]
    price = products[item]
    print(f"{r}. {item} - {price}")
