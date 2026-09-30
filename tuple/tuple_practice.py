# Q1
t = (3, 6, 9, 12, 6, 15, 6)
print(t.count(6))  # counting a how many of 6 element in t
print(t.index(6))  # indexing which index no having 6

# Q2
t = (10, 20, 30, 40, 50)
print(t[1:4])  # positive index start no 1 and end is 4
print(t[-2:]) # start from index -2 (40) to end of tuple

# Q3
t1 = (1, 2, 3)
t2 = t1  # (1,2,3)
t1 = t1 + (4, 5)  # adding a numbers in t1
print(t1)  # printing a t1 Output:- (1,2,3,4,5)
print(t2)  # printing a t2 Output:- (1,2,3)

# Q4
t = ([1, 2], [3, 4])
t[0].append(99)  # adding a number in index number 0
print(t)  # ([1,2,99],[3,4])

# Q5
t = (5, 10, 15, 20)
print(t[::2])  # (5,15)
print(t[::-1])  # (20, 15, 10, 5)
