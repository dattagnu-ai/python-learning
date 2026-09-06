# Factorial Number


def factorial_number(num):
    if num == 0:
        return 1
    else:
        a = num * factorial_number(num - 1)
        return a


num = int(input("Enter a number:- "))
result = factorial_number(num)
print(f"Factorial of {num} is: {result}")
