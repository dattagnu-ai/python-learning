# # Checking Even or Odd

num = int(input("Enter a Number:- "))
print("Even") if num % 2 == 0 else print("Odd")


# Positive or Negative

num = int(input("Enter a Number:- "))
print(f"{num} is Positive Number") if num > 0 else print(f"{num} is Negative Number")


# Adult or Minor

name = input("Enter Name:- ")
age = int(input("Enter Age:- "))
print(f"{name} is Adult") if age >= 18 else print(f"{name} is Minor")


# Greater or Equal

num1 = int(input("Enter First Number:- "))
num2 = int(input("Enter Second Number:- "))
print("Both is Equal" if num1 == num2 else f"{num1} is greater" if num1 > num2 else f"{num2} is greater")