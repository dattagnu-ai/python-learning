# Discard and Remove

# Q1
s = {1, 2, 3, 4, 5}
s.discard(3)  # 3 removed, no error even if not present
s.remove(6)   # KeyError — 6 not in set, execution stops here
print(s)      # this line never runs

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
print(type(s1 & s2))  # <class 'set'> — result is set, not frozenset

# Update

s = {1, 2, 3}
s.update({3, 4, 5})  #adds multiple elements at once, unlike add() which adds only one
print(s)  # {1,2,3,4,5}
