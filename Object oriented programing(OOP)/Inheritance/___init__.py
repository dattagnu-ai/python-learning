class Student:
    # student grade

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll_no = roll
        self.marks = marks

    def display(self):
        print(f"Name:- {self.name}")
        print(f"Roll No.:-{self.roll_no}")
        print(f"Marks:- {self.marks}")

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.marks = new_marks
            print(f"Updated Marks:- {self.marks}")
        else:
            print("Invalid marks")

    def is_passed(self):
        if self.marks >= 40:
            print("Passed")
        else:
            print("Fail")

    def calculate_grade(self):
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


student_1 = Student("Dattu", 101, 40)
student_1.display()
student_1.update_marks(120)
student_1.calculate_grade()
student_1.is_passed()

print("______________________________\n")

student_2 = Student("Shreya", 101, 39)
student_2.display()
student_2.calculate_grade()
student_2.is_passed()


# Banking system


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        print(f"Name:- {self.name}")
        print(f"Balance:- {self.balance}")

    def deposit(self, amount):
        print(f"Deposit Amount:- {amount}")
        self.balance += amount
        print(f"Total Balance:- {self.balance}")

    def withdrawal(self, amount):
        if amount <= self.balance:
            print(f"Withdrawal Amount:- {amount}")
            self.balance -= amount
            print(f"Total Balance:- {self.balance}")
        else:
            print("Insufficient Balance")


bank_1 = BankAccount("Dattu", 5000)
bank_1.display()
bank_1.deposit(500)
bank_1.withdrawal(90000)
