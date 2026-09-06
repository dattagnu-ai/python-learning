# class student:

#     def __init__(self, name, roll_no, marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks

#     def display(self):
#         print(self.name)
#         print(self.roll_no)
#         print(self.marks)


# student_1 = student("dattu", 101, 90)
# student_1.display()
# student_2 = student("shreya", 101, 85)


# class Employee:

#     def introduce(self):
#         print(f"Hi i'm {self.name} and my role is {self.role}")


# Employee_1 = Employee()
# Employee_2 = Employee()

# Employee_1.name = "Dattu"
# Employee_1.role = "ML Engineer"
# Employee_1.introduce()

# Employee_2.name = "Rahul"
# Employee_2.role = "data Engineer"
# Employee_2.introduce()


# class Movie:

#     def display_info(self):
#         print(f"Movie Title:- {self.title}")
#         print(f"Movie Rating:- {self.rating}")

#     def is_recommended(self):
#         if self.rating >= 8:
#             print("Recommended")
#         else:
#             print("Not recommended")


# movie_1 = Movie()
# movie_1.title = "Pushpa"
# movie_1.rating = 9
# movie_1.display_info()
# movie_1.is_recommended()

# print("_____________________")
# movie_2 = Movie()
# movie_2.title = "king"
# movie_2.rating = 7
# movie_2.display_info()
# movie_2.is_recommended()


class Student:

    def display_result(self):
        print(f"Name:- {self.name}")
        print(f"Marks:- {self.marks}")
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

    def display_grade(self):
        if self.marks >= 90:
            print("Grade:- A")
        elif self.marks >= 75:
            print("Grade:- B")
        elif self.marks >= 60:
            print("Grade:- C")
        elif self.marks >= 40:
            print("Grade:- D")
        else:
            print("Grade:- F")


student_1 = Student()

student_1.name = "Dattu"
student_1.marks = 90
student_1.display_result()
student_1.display_grade()
print("______________________\n")

student_2 = Student()

student_2.name = "Rahul"
student_2.marks = 75
student_2.display_result()
student_2.display_grade()

print("______________________\n")

student_3 = Student()

student_3.name = "Shreya"
student_3.marks = 60
student_3.display_result()
student_3.display_grade()

print("______________________\n")

student_4 = Student()

student_4.name = "Lokesh"
student_4.marks = 40
student_4.display_result()
student_4.display_grade()

print("______________________\n")
student_5 = Student()

student_5.name = "Dikesh"
student_5.marks = 39
student_5.display_result()
student_5.display_grade()
