"""ho chal practice que karun thoda hard de

8:56 AM
ठीक आहे. एक-एक दे, सगळे एकत्र नाही.

Question 1:

python
nums = [5, 3, 8, 1, 9, 2, 7]
हे कर — code लिही:

List sort कर
शेवटचा element काढ (pop)
7 list मध्ये आहे का check कर
print कर final list"""

# nums = [5, 3, 8, 1, 9, 2, 7]
# nums.sort()
# print(nums)
# nums.pop()
# print(7 in nums)
# print(nums)


"""
Question 2:
pythonnums = [4, 2, 7, 2, 9, 2, 1]
Code लिही:

2 किती वेळा आहे ते print कर
List reverse कर
पहिले 3 elements print कर (slicing वापर)"""


# pythonnums = [4, 2, 7, 2, 9, 2, 1]
#
# print(pythonnums.count(2))
# pythonnums.reverse()
# print(pythonnums)
# print(pythonnums[:3])


# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)
# c = c * 2
# print(c)
# c.sort()
# print(c)
# print(c.count(3))
# print(c[-3:])


"""Question 4 — आता real problem:
एक list आहे:
pythonmarks = [85, 92, 78, 95, 88, 78, 90]
Code लिही:

Highest mark print कर (sort वापर)
78 किती वेळा आलं ते print कर
List reverse करून पहिले 4 marks print कर"""

# pythonmarks = [85, 92, 78, 95, 88, 78, 90]

# pythonmarks.sort()
# print(pythonmarks)

# print(pythonmarks[-1])

# print(pythonmarks.count(78))

# pythonmarks.reverse()
# print(f"Reverse the Numbers: {pythonmarks}, \nThe first 4 Numbers {pythonmarks[:4]}")


# data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# data.sort()
# print(data)
#
# data.pop()
# print(data)
#
# data.reverse()
# print(data)
#
# print(data.count(1))
#
# print(data[:3])
#
# print(5 in data)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(matrix[2][1])
# print(matrix[0][2])
# print(matrix[1][1])

# data = [[10, 20], [30, 40], [50, 60]]
# data[1][0] = 99
# print(data)
# print(data[2][1] + data[0][0])


a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
print(a)
print(len(a))


a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
print(len(a))
