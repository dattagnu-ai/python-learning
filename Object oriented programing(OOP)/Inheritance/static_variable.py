# class Employee:

#     @staticmethod
#     def is_valid_salary(salary):
#         return salary > 0


# print(Employee.is_valid_salary(5000))
# print(Employee.is_valid_salary(-5000))


class BankAccount:

    @staticmethod
    def acc_no(accno):
        return len(accno) == 10


print(BankAccount.acc_no("12345712890"))
print(BankAccount.acc_no("1234571289"))
