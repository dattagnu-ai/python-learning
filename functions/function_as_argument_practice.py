# ---------------------------------------------------
# Title: Single Parameter Function Reference
# ---------------------------------------------------


def square(x):
    return x * x


def apply_function(func, value):
    result = func(value)
    print(result)


apply_function(square, 5)


# ---------------------------------------------------
# Title: Dynamic Operations Using Function Arguments
# ---------------------------------------------------
"""

step 1: make a first function and give a parameter add(a,b)
step 2: addition of a parameter
step 3: print a result
step 4: make a second function and give a same parameter a,b
step 5: multiply a both parameters
step 6: print a result
step 7: make a third function and give a parameter apply_function(func,a,b)
step 8: set func(a,b)
step 9: call a function
        input:-apply_function(add, 5, 6)
               apply_function(multi, 5, 6)
        output:= addition 11
                 multiplication 30
hand by hand:-Call: apply_operation(add, 3, 4) execution start hota.

Parameter Mapping:

func = add (function reference)

a = 3

b = 4

Inside apply_operation:

Line runs: result = func(a, b)

Internal substitution: func ata add kade point kartoy, mhanun line hoti: result = add(3, 4)

Jumping to add(3, 4):

add function 3 + 4 calculate karto ani 7 return karto.

Back to apply_operation:

result variable madhe 7 save hoto.

Line runs: print(result) → Terminal madhe 7 print hoto.
"""


def add(a, b):
    result = a + b
    print(f"Addition {result}")


def multi(a, b):
    result = a * b
    print(f"Multiplication {result}")


def apply_operation(func, a, b):
    func(a, b)


apply_operation(add, 3, 4)
apply_operation(multi, 3, 4)


# ---------------------------------------------------
# Title: Extending Operations (Subtraction)
# ---------------------------------------------------


def sub(a, b):
    print(f"Subtraction {a - b}")


def apply_function(func, a, b):
    func(a, b)


apply_function(sub, 10, 3)
