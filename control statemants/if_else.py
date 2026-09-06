# Checking Odd Or Even
num = int(input("Enter  a Number:- "))
if num % 2 == 0:
    print(f"{num} is Even Number")
else:
    print(f"{num} is odd Number")

# Checking Positive Or Negative
num = int(input("Enter a number:- "))
if num > 0:
    print(f"{num} is positive Number")
else:
    print(f"{num} is Negative Number")

# Empty of any Content
string = input("Enter Somthong:- ")
if string == "":
    print("Empty String")
else:
    print(f"String has content {string}")

# Checking  a number Equal or not
num1 = int(input("Enter first Number:- "))
num2 = int(input("Enter Second Number:- "))

if num1 == num2:
    print("Both are equal")
else:
    print("Not equal")


name = input("Enter a Name:- ")

if name == "Dattu":
    print("Welcome back, Dattu!")
else:
    print("You are not authorized")
