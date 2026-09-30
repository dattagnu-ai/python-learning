# string = "dattu learning python"

# print(string.capitalize())
# print(string.replace("python", "AI ML"))
# print(len(string))
# print("learning" in string)


# 🔵 Operators — Code लिही:
# pythona = 15
# b = 4
# हे दोन variables वापरून:

# a ला b ने divide केल्यावर फक्त remainder print कर
# a च्या power 2 print कर
# a > 10 and b < 3 — output काय येईल?
# # not (a == b) — output काय येईल?

# a = 15
# b = 4

# print(a % b)
# print(a**2)
# print(a > 10 and b < 3)
# print(not (a == b))


# fruits = ["apple", "banana", "mango", "orange"]

# "mango" ला "grapes" ने replace कर
# शेवटचा element remove कर
# List sort कर
# "banana" कितव्या index वर आहे ते print कर

fruits = ["apple", "banana", "mango", "orange"]

fruits[2] = "graphs"
print(fruits)
fruits.pop()
print(fruits)
fruits.sort()
print(fruits)
print(fruits.index("banana"))


# t = (10, 20, 30, 40, 50)

# तिसरा element print कर
# Last element print कर — negative indexing वापर
# Tuple मध्ये 20 किती वेळा आहे ते print कर
# Tuple च्या एकूण elements

# t = (10, 20, 30, 40, 50)

# print(t[2])
# print(t[-1])
# print(t.count(20))
# print(len(t))


# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# Union print कर
# Intersection print कर
# a मधून b चे elements काढून टाक (difference)
# a मध्ये 10 add कर आणि print कर

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# print(a | b)
# print(a & b)
# print(a - b)
# a.add(10)
# print(a)

# student = {
#     "name": "Dattu",
#     "age": 20,
#     "course": "Python"
# }

# "age" ची value print कर
# "city" key add कर — value "Alapalli"
# "course" ची value "AI/ML" ने update कर
# सगळ्या keys print कर

# student = {"name": "dattu", "age": 20, "course": "python"}


# print(student["age"])
# student["city"] = "Alapalli"
# print(student)
# student["course"] = "AI ML"
# print(student)

# print(student.keys())

# एक number n = 75 घे आणि:

# n 90 पेक्षा जास्त असेल तर "A grade" print कर
# 75 ते 90 मध्ये असेल तर "B grade" print कर
# 60 ते 75 मध्ये असेल तर "C grade" print कर
# बाकी सगळ्यांसाठी "Fail" print कर

# n = 91
# if n > 90:
#     print("A grade")
# elif n >= 75:
#     print("B grade")
# elif n >= 60:
#     print("C grade")
# else:
#     print("Fail")

# numbers = [3, 7, 1, 9, 4, 6, 2]

# Loop वापरून सगळ्या numbers चा total काढ
# Highest number print कर
# 5 पेक्षा जास्त numbers skip कर (continue वापर) आणि बाकी print कर

# numbers = [3, 7, 1, 9, 4, 6, 2]
# total = 0
# highest = numbers[0]
# for i in numbers:
#     total = total + i
# print(f"total = {total}")
# for i in numbers:
#     if highest < i:
#         highest = i
# print(f"highest number = {highest}")
# for i in numbers:
#     if i > 5:
#         continue
#     print(i)
