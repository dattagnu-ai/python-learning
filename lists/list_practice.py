# =======================
#    LISTS - PYTHON
# =======================

# Introduction & Indexing:

students = ["Ravi", "Priya", "Dattu", "Amit", "Shreya"]

print(f"length:- {len(students)}")
print(students[2])
print(students[-2])
print("Dattu" in students)


# Slicing, Concat, Repeat:


a = [5, 10, 15, 20, 25, 30]
b = [35, 40, 45]

print(a[2:5])
print(a[-3:])
print(a + b)
print(b * 3)
print(a[::3])


# Append, Insert, Extend, Remove, Pop:


nums = [10, 20, 30, 40, 50]

nums.append(60)
print(nums)

nums.insert(2, 99)
print(nums)

nums.extend([70, 80])
print(nums)

nums.remove(20)
print(nums)

nums.pop()
print(nums)

print(f"Final Result:- {nums}")


# Reverse, Sort, Count, Membership:

nums = [4, 7, 2, 9, 2, 5, 2, 5, 1]

print(nums.count(2))
nums.sort()
print(nums)
print(max(nums))
print(min(nums))
nums.reverse()
print(nums)
print(9 in nums)
print(99 in nums)


# Numerical Operations:

scores = [88, 74, 95, 62, 79, 91, 83]

print(sum(scores))
print(sum(scores) / len(scores))
print(max(scores))
print(min(scores))
print(max(scores) - min(scores))


# Nested Lists:


matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

print(matrix[1][1])
print(matrix[2][2])
print(matrix[0][0])
print(matrix[1])
print(matrix[0][2] + matrix[2][0])
