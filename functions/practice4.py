# ----------------------------------------
# Example 1: Default Arguments
# ----------------------------------------


def greet(name, word="Hello"):
    print(f"{word}, {name}!")


greet("Dattu")
greet("dattu", word="Hi")


# ----------------------------------------
# Example 2: Using *args for Variable Arguments
# ----------------------------------------
"""
step 1= make a function total_marks and add a *variable
step 2= after that make a total variable for total of marks
step 3= make a one more variable for calculate average of marks
        formula:- average=total/len(marks)
step 4= print a total and average
step 6= call a function and give a input
        input=(80,90,70)
        expecting output:- total= 240 and average- 80.0
"""


def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    print(f"Total: {total}, Average: {average}")


total_marks(80, 90, 70)

# ----------------------------------------
# Example 3: Student Report Generator
# (Required Parameter + *args + Default Argument)
# ----------------------------------------
"""
step 1: make a function 
step 2: give a parameters 
step 3: name= for user giving a name,*marks= for multiple marks,grade_system= default arg 
step 4: calculate total,average,and gpa 
step 5: give a condition if user change a change the default arg into "gpa"
step 6: print a name, total and gpa
step 7: else: user not changing a default arg print normaly, like name,total and average 
step 8: input:- student_report("Dattu", 80, 90, 70)
        output:-Name:- Dattu Total: 240 Average: 80.0%
        when input:- student_report("Dattu", 80, 90, 70, grade_system="gpa")
        output:-Name:- Dattu Total: 240 GPA: 3.2
"""


def student_report(name, *marks, grade_system="percentage"):

    if not marks:
        print(f"Name:- {name}")
        print("Marks entry missing! Total: 0")
        return

    total = sum(marks)
    average = total / len(marks)
    gpa = average / 25

    if grade_system == "gpa":
        print(f"Name:- {name}")
        print(f"Total: {total}")
        print(f"GPA: {gpa}")
    else:
        print(f"Name:- {name}")
        print(f"Total: {total}")
        print(f"Average: {average}%")


student_report("dattu")
student_report("Dattu", 80, 90, 70)
student_report("Dattu", 80, 90, 70, grade_system="gpa")
