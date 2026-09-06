## Operators Practice Programs


# question 1

num1 = float(input("Enter Nun1: "))
num2 = float(input("Enter Nun2: "))

if num2 == 0:
    print("0 is not Divisible No.")
else:
    print("\n========== Result ==========\n")
    print(f"Addition: {num1+num2}")
    print(f"Subtraction: {num1-num2}")
    print(f"Multiplication: {num1*num2}")
    print(f"Division: {num1/num2}")

# question 2

a = 10
b = 20

print(a > b)
print(a < b)
print(a == b)


# question 3

age = 20
citizen = True
# and
print(citizen == True and age >= 10)
print
print(citizen == False and age >= 10)

# or
print(age <= 30 or citizen == False)
print(age <= 10 or citizen == True)

# not
print(not citizen)
print(not (age < 18))
