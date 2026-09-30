# class Employee:
#     company = "Google"

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print(f"Name:- {self.name}")
#         print(f"Salary:- {self.salary}")

#     @classmethod
#     def change_company(cls, new_company):
#         cls.company = new_company


# Employee.change_company("Microsoft")
# employee_1 = Employee("dattu", 90000)
# employee_1.display()
# print(employee_1.company)
# print("")
# employee_2 = Employee("Shreya", 90000)
# employee_2.display()
# print(employee_1.company)


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")
        return cls(name, int(salary))


employee_1 = Employee.from_string("Dattu,20000")
print(employee_1.name)
print(employee_1.salary)
