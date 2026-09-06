# # total

marks = [45, 78, 23, 90, 56]
total = 0
for i in marks:
    total = total + i
print(total)


# # highest

scores = [11, 45, 100, 54, 1, -1, 2]
highest_num = scores[0]
lowest_num = scores[0]

for number in scores:
    if highest_num < number:
        highest_num = number

    if number < lowest_num:
        lowest_num = number
print(f"Highest Score { highest_num} \nlowest Score {lowest_num}")

# Highest marks

students = {"Dattu": 85, "Rahul": 42, "Priya": 76, "Amit": 38, "Sneha": 91}

highest_name = ""
highest_marks = list(students.values())[0]

for name in students:
    if students[name] > highest_marks:
        highest_marks = students[name]
        highest_name = name


print(highest_name, highest_marks)
