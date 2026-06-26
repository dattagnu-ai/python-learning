
for i in range(1, 20):
    if i == 13:
        break
    print(i)

for i in range(1, 20):
    if i % 3 == 0:
        continue
    print(i)

students = {"Dattu": 85, "Rahul": 42, "Priya": 76, "Amit": 38, "Sneha": 91}

for name in students:
    # marks check

    if students[name] < 50:
        print(name, students[name])
        break
