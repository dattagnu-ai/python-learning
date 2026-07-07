student = []
total = 0
result = {}
for i in range(3):
    name = input("Enter a name:- ")
    marks = int(input("Enter a marks:- "))
    student.append((name, marks))
    total = total + marks
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "FAIL"
    result[name] = grade
average = total / len(student)
print(f"Average= {average:.2f}")
print(f"Total= {total}")
print(f"Result= {result}")
