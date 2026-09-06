# 🔴 Project: Student Grade Manager
# Problem:
# एक program बनव जो:

# User कडून 3 students चे नाव आणि marks (0-100) input घेईल — input() वापर
# सगळ्या marks एका list मध्ये store कर
# Loop वापरून total आणि average काढ
# Average नुसार grade assign कर:

# 90+ → A
# 75-89 → B
# 60-74 → C
# 60 खाली → Fail


# Result एका dictionary मध्ये store कर — {name: grade}
# सगळ्या students चे result print कर

# student = []
# total = 0
# result = {}
# for i in range(3):
#     name = input("Enter a name:- ")
#     marks = int(input("Enter a marks:- "))
#     student.append((name, marks))
#     total = total + marks
#     if marks >= 90:
#         grade = "A"
#     elif marks >= 75:
#         grade = "B"
#     elif marks >= 60:
#         grade = "C"
#     else:
#         grade = "FAIL"
#     result[name] = grade
# average = total / len(student)
# print(f"Average= {average:.2f}")
# print(f"Total= {total}")
# print(f"Result= {result}")


# Question: Ek list nums = [4, 7, 2, 9, 5, 1, 8] ahe. Loop lihi
# je pratyek number check karel, ani jasach number 9 peksha jast
# asel tithe loop thaम्बव (stop), pan number 5 asel tar to skip kar
# (print na karता) ani pudhe ja. Baki sagळe numbers print kar.

nums = [5, 5, 9, 5, 3]
for i in nums:
    if i > 9:
        break
    elif i == 5:
        continue
    print(i)
