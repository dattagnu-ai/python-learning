class Expense:

    def __init__(self, name, amount):
        self.name = name
        self.amount = float(amount)

    def display(self):
        print(f"{self.name}           {self.amount}")


print("Category        Amount")
print("")
expanse1 = Expense("food", "900")
expanse1.display()
expanse2 = Expense("travel", "1900")
expanse2.display()
expanse3 = Expense("lunch", "700")
expanse3.display()
expanse4 = Expense("chips", "90")
expanse4.display()


class Expense_tracker:

    def __init__(self):
        self.expense = []

    def add_expense(self, expense_add):
        self.expense.append(expense_add)

    def show_expense(self):
        for sh in self.expense:
            sh.display()

    def delete_expense(self, delete):
        found = False
        for de in self.expense:
            if delete.lower() == de.name.lower():
                self.expense.remove(de)
                print("Expense deleted")
                found = True
                break
        if not found:
            print("Invalid Category")

    def edit_expense(self, edit):
        found = False
        for ed in self.expense:
            if edit.lower() == ed.name.lower():
                print(f"Expense founded:- {ed.name}")
                new_name = input("Enter new name:- ")
                new_amount = input("Enter new amount:- ")
                if new_name:
                    ed.name = new_name
                if new_amount:
                    ed.amount = float(new_amount)
                print("Expense updated")
                found = True
                break
        if not found:
            print("Invalid Category")

    def search_expense(self, name):
        found = False
        for n in self.expense:
            if name.lower() == n.name.lower():
                n.display()
                found = True
                break
        if not found:
            print("Invalid Name")

    def total_expense(self):
        total = 0
        for te in self.expense:
            total += te.amount
        print(f"Total amount:- {total}")


print("Category        Amount")
print("")
expanse1 = Expense("food", "900")

expanse2 = Expense("travel", "1900")

expanse3 = Expense("lunch", "700")

expanse4 = Expense("chips", "90")

et = Expense_tracker()
et.add_expense(expanse1)
et.add_expense(expanse2)
et.add_expense(expanse3)
et.add_expense(expanse4)
et.show_expense()
et.delete_expense("chips")
et.search_expense("chips")
et.edit_expense("lunch")
et.total_expense()
et.show_expense()
