# Checking a num positive or negative and even or odd

num = int(input("Enter a Number:- "))

if num > 0:
    print("Number is positive")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Number is negative")


# checking a username and password

username = input("Enter a User Name:- ")
password = input("Enter a Code:- ")
if username == "dattu":

    if password == "dattu123":
        print("Login successful")
    else:
        print("Password is wrong")
else:
    print("User not found")


# checks loan eligibility by evaluating age and salart

age = int(input("Enter Age:- "))

if age >= 18:
    salary = float(input("Enter salary:- "))

    if salary >= 30000:
        print("Loan approved")
    else:
        print("Income too low")
else:
    print("Not eligible due to age")
