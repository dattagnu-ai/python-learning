"""Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

full_name = first_name + " " + last_name
print(f"Hello,{full_name}! welcome to the Python Program")
