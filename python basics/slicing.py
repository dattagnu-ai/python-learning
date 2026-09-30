s1 = "Hello world"

print(s1[2:9:1])
print(s1[2:7:2])
print(s1[1:12:3])


s2 = "Dattagnu"

print("\nBasic slicing")

print(s2[0:3])
print(s2[1:4])
print(s2[0:5])

print("\nstart/stop skip")
print(s2[:3])
print(s2[5:])
print(s2[:])

print("\nUsing step")
print(s2[::4])
print(s2[::1])

print("\nNegative Indexing")
print(s2[-2])
print(s2[-5:])
print(s2[::-3])
