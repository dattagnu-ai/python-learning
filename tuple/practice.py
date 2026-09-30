t = (1, 2, 3)
t = t + (4,)
print(t)


t = ([1, 2], [3, 4])
t[0].append(99)
print(t)


random = ("dattu", 1, 99, 22, 2.10)
random3 = ["shreya", 2, 3, 99, 3.0]

print(type(random))
print(type(random3))

print(list(random))
print(tuple(random3))

print(random3.index(99))


# Mutable (list)
l = [1, 2, 3]
print(id(l))
l.append(4)
print(id(l))  # SAME id — same object modified

a = 256
b = 256
print(id(a) == id(b))

a = 1000
b = 1000
print(id(a) == id(b))
