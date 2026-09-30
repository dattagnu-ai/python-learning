# for i in range(1, 8):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()


for row in range(1, 6):
    for space in range(1, 6 - row):
        print(" ", end="")
    for col in range(1, row + 1):
        print("*", end=" ")
    print()


# for i in range(5):
# for j in range(5 - i):
# print("*", end="")
# print()


# for row in range(5):
# for i in range(5):
# print("*", end="")
# print()

# for i in range(1, 6):
# for j in range(1, i + 1):
# print(j, end="")
# print()
