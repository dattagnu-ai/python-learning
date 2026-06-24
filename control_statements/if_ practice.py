# eligible or not
age = int(input("What is your Age?:- "))
if age >= 18:
    print("You are eligible to vote")

# Even or odd
num = int(input("Enter  a Number:- "))
if num % 2 == 0:
    print(f"{num} is Even Number")

# Greater or smaller
num1 = int(input("Enter a Number:- "))
num2 = int(input("Enter a Number:- "))

if num1 > num2:
    print("First number is greater")


# Password Checking
password = "dattu123"
pas = input("Enter a password:- ")

if pas == password:
    print("Access granted")
