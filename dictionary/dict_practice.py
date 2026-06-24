# DICTIONARYs

d = {"name": "dattu", "age": 20, "city": "Alapalli"}
print(d.keys())
print(d.values())


# Q2


d = {"a": 1, "b": 2, "c": 3}

d["b"] = 99
d["d"] = 4
d.pop("a")
print(d)


# Q3

import copy

d1 = {"name": "dattu", "marks": {"math": 90}}
d2 = copy.copy(d1)
d1["marks"]["math"] = 50

print(d1)  # {'name': 'dattu', 'marks': {'math': 50}}
print(
    d2
)  # {'name': 'dattu', 'marks': {'math': 50}} in a shallow copy inner dictionary is shared


# Q4

d = {"x": 10, "y": 20, "z": 30}
for key, value in d.items():
    print(f"{key}={value}")


# Q5

d4 = {"a": 1, "b": 2, "c": 3}
total = 0
for val in d4.values():

    total = total + val
print(total)
