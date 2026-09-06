# class Student:
#     pass


# student_1 = Student()
# student_2 = Student()
# # False because student_1 and student_2 are different objects.
# print(student_1 is student_2)

# student_1.name = "dattu"
# student_1.roll_no = 101
# student_1.marks = 90


# print(student_1.name)
# print(student_1.roll_no)
# print(student_1.marks)


class Book:
    pass


book_1 = Book()
book_2 = Book()

book_1.title = "the flag"
book_1.author = "dattu"
book_1.price = 150

book_2.title = "kingdom"
book_2.author = "shreya"
book_2.price = 149


print(f"book title:-{book_1.title}")
print(f"book price:-{book_1.price}")

print(f"book title:-{book_2.title}")
print(f"book price:-{book_2.price}")

book_1.price = 189
print(f"book_1 changed price:-{book_1.price}")
print(f"book price:-{book_2.price}")
