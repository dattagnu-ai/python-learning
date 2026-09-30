for i in range(1, 10):
    print(i)

for i in range(10, 1, -1):
    print(i)

for i in range(1, 50, 2):
    print(i)

students = {"Dattu": 85, "Rahul": 42, "Priya": 76, "Amit": 38, "Sneha": 91}
student_name = list(students.keys())
for index in range(len(students)):
    r = index + 1
    score = students[student_name[index]]
    print(f"{r}.{student_name[index]} - {score}")
