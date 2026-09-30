# x = 10


# def show():
#     x = 20
#     print(x)


# show()
# print(x)

# count = 5


# def modify():

#     count = 100
#     print("Inside:", count)


# modify()
# print("Outside:", count)


# n = 5


# def add():
#     global n
#     n = 100
#     print(f"local {n}")


# add()
# print(f"Global {n}")


"""
step 1: make a global variable and value is 0 total_students=0
step 2: make a func there has a no params add_students()
step 3: call a global variable in the func
step 4: calculate a students total_students+=1
step 5: print a students
step 6: call a function how many user want ex.3 time
        output:-total student 1
        output:-total student 2
        output:-total student 3
hand-to-hand:- first global variable call =0
                then total student =1
                mens 0+1=1
                    then 1+1=2
                    continue the process
"""

total_students = 0


def add_students():
    global total_students
    total_students += 1

    print(f"Total students: {total_students}")


add_students()
add_students()
add_students()
