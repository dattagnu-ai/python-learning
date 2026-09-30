# Checking Positive or Negative or Zero number


num = int(input("Enter a Number:- "))
if num > 0:
    print(f"{num} is positive Number")
elif num < 0:
    print(f"{num} is negative Number")
else:
    print("Zero")


# Getting a Grades


marks = int(input("Enter a Marks:- "))

if marks >= 90:
    print("A Grade")
elif marks >= 70:
    print("B Grade")
elif marks >= 50:
    print("c Grade")
else:
    print("Fail")


# Checking a Number Wise Days

day = int(input("Enter a Date:- "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")


# Checking Temperature


temperature = int(input("enter a celsius:- "))

if temperature >= 35:
    print(f"{temperature}° Very Hot")
elif temperature >= 25:
    print(f"{temperature}° Warm")
elif temperature >= 15:
    print(f"{temperature}° cool")
else:
    print(f"{temperature}° cold")
