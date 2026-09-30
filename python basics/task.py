"""Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
"""

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter second number   : "))
#
#
# if num2 == 0:
#    print("Error: Cannot not divide by 0")
# else:
#    print("======== RESULT ========")
#
#    print(f"Addition: {num1+num2}")
#    print(f"Subtraction: {num1-num2}")
#    print(f"Multiplication: {num1*num2}")
#    print(f"Division: {num1/num2}")


"""Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""


first_name = input("Enter first name: ")
last_name = input("Enter last name  : ")

full_name = first_name + " " + last_name

print(f"Hello, {full_name}! Welcome to Python program")
