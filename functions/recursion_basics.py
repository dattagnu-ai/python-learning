# ----------------------------------------
# Example 1: Countdown Using Recursion
# ----------------------------------------


def countdown(n):
    if n == 0:
        print("done")
        return
    print(n)
    countdown(n - 1)


countdown(6)

# ----------------------------------------
# Example 2: Print Numbers in Descending Order
# ----------------------------------------


def show(n):
    if n == 0:
        return

    print(n)
    show(n - 1)


show(3)


# ----------------------------------------
# Example 3: Print Numbers in Ascending Order
# ----------------------------------------
def show(n):
    if n == 0:
        return

    show(n - 1)
    print(n)


show(3)

# ----------------------------------------
# Example 4: Factorial Using Recursion
# ----------------------------------------

"""
step 1: make a function
step 2: give a parameter for input:- n
step 3: check condition if n==0 return 1
step 4: else give a factorial n and call recursion function
step 5: factorial formula:- fact=n*factorial(n-1)
        factorial(3) = 3 * factorial(2)
        factorial(2) = 2 * factorial(1)
        factorial(1) = 1 * factorial(0)
        factorial(0) = 1 (stop)
step 6: print a factorial number
step 7: input: print(factorial(3))
        output: 6
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        fact = n * factorial(n - 1)
        return fact


print(factorial(3))


# ----------------------------------------
# Example 5: Sum of Digits Using Recursion
# ----------------------------------------

"""
step 1: make a function
step 2: check a condition if n==0 return 0
step 3: else call a recursion 
        formula:- (n % 10) + sum_digits(n // 10)
        4 + sum_digits(123)
        4 + (3 + sum_digits(12))
        4 + 3 + (2 + sum_digits(1))
        4 + 3 + 2 + (1 + sum_digits(0))
        4 + 3 + 2 + 1 + 0
        10
step 4: print a function and give input
step 5: input:- print(sum_digits(1234))
        output:- 10
"""


def sum_digits(n):
    if n == 0:
        return 0
    else:

        return (n % 10) + sum_digits(n // 10)


print(sum_digits(1234))
