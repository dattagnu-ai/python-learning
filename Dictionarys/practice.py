# d = {"a": 1, "a": 2}
# print(d)  # {"a": 2} — first value overridden
#
#
# employee1 = {"id": 1001, "Name": "dattu", "salary": 10000}
# print(employee1.get("phone", 123456))
# print(employee1.get("Name", 123456))
#
#
# d = {"a": 1, "b": 2, "c": 3}
# d.pop("b")
# print(d)
# d.popitem()
# print(d)


# d = {"name": "dattu", "age": 20, "city": "alapalli"}
# d.pop("age")
# print(d)  # {"name": "dattu","city": "alapalli"}
#
#
# d = {"a": 1, "b": 2, "c": 3}
# d["b"] = 99
# d["d"] = 4
# print(d)  # {"a": 1, "b": 99, "c": 3,"d":4}
#
# d = {"x": 10, "y": 20, "z": 30}
# d.popitem()
# print(d)  # {"x": 10, "y": 20}
#
# d = {"a": 1, "b": 2}
# d["a"] = 100
# d["c"] = 3
# d.pop("b")
# print(d)  # {"a": 100,"c":3}

# d = {"name": "dattu", "age": 20}
# print(d.pop("city", "dasttu"))
# print(d)  # Error


# s1 = {"dattu": 20, "rice": 20, "marks": {"math": 87, "eng": 56, "bio": 84}}
#
# print(s1.keys())
# print(s1.values())
# print(s1.items())


# import copy
#
## Shallow copy
#
# s1 = {"dattu": 20, "rice": 20, "marks": {"math": 87, "eng": 56, "bio": 84}}
#
# s2 = copy.copy(s1)
#
# s1["dattu"] = "shreya"
# s1["marks"][1] = 87
#
# print(f"s1:- {s1}")
# print(f"s2:- {s2}")
#
## deep copy
#
# s1 = ["dattu", 20, 6.01, [10, 20, 30]]
# s2 = copy.deepcopy(s1)
#
# s1[0] = "shreya"
# s1[3][2] = 50
#
# print(f"s1 = {s1}")
# print(f"s2 = {s2}")
#
#
# import copy
#
# s1 = {"dattu": 20, "marks": {"math": 87}}
# s2 = copy.deepcopy(s1)
# s1["marks"]["math"] = 99
# print(s1)
# print(s2)
#
# for i in range(1, 11, 2):
#    print(i)
#


# for i in range(1, 11):
#    print(i)

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)


# list = [3, 6, 9, 12, 15]
# total = 0
# for i in list:
#     total = total + i
# print(total)


# for i in range(1, 6):
#     print("dattu")


# for i in range(1, 6):
#     total = i**2
#     print(total)
