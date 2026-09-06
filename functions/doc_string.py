"""
    Problem: add_numbers(a, b) navाचं function लिही jo doन numbers add karto ani result return karto. Function madhे proper docstring add kar je explain karel:

function kay karто
parameters kay ahet (types sahit)
return value kay ahe

Code lihण्याआधी he kar:

Problem 2 वेळा वाच
Input/output plain words madhे सांग (docstring sathi specifically — kay information tyat asaव लागते)
Plain English steps लिही — docstring format मध्ये काय काय ओळी असतील
"""


def add_numbers(a, b):
    """
    add two two number return their sum

    parameter:
    a(int): first number
    b(int): second number

    returns:
    int: sum of a and b
    """
    return a + b


help(add_numbers)
print(add_numbers(3, 5))
