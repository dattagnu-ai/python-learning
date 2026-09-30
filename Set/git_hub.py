# Discard and Remove

s = {1, 2, 3, 4, 5}
s.discard(3)  # deleting a number 3 {1,2,4,5}
s.remove(6)  # Error
print(s)  # KeyError

# Union, Intersection and Difference

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)  # {1,2,3,4,5,6}:-Union
print(A & B)  # {3,4}:-intersection finding a common elements
print(A - B)  # {1,2}:-finding a difference in b
print(B - A)  # {5,6}:-finding a difference in a

# Add() Function

s = {1, 2, 3}
s.add(2)
print(
    s
)  # {1,2,3}:-adding a element but s is already have a element that's why he not showing because of rule
print(len(s))  # 3 measuring a length


# Frozenset

s1 = {1, 2, 3}
s2 = frozenset({3, 4, 5})
print(s1 & s2)  # {3}:=intersection rule finding a common element
print(type(s1 & s2))  # <class 'set'> showing a type


# Update

s = {1, 2, 3}
s.update({3, 4, 5})  # adding a element here not allow a like append() function
print(s)  # {1,2,3,4,5}
