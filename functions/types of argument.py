# default argument


# def info(age, name):
#     return age, name


# print(info(20))
# print(info(20, "shreya"))


# variable length keyword argument


def student(id, name, **marks):
    if len(marks) == 0:
        print(f"{name} is not attempt a exam")
    else:
        a = sum(marks.values()) / len(marks)
        print(f"{name} with id {id} secured by {a}")


student(101, "dattu", sub1=56.4, sub2=64.6, sub3=96.4)
