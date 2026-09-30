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
