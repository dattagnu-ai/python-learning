from datetime import datetime


class Expense:
    def __init__(self, category, description, amount, date):
        self.category = category.strip().capitalize()
        self.amount = float(amount)
        self.description = description.strip().capitalize()
        self.date = date if date else datetime.now().strftime("%d-%m-%Y")

    def display(self, count):
        print(
            f"{count}: {self.category:<12} {self.description:<15} {self.amount:<10} Rs {self.date}"
        )


class ExpenseTracker:
    def __init__(self):
        self.expense = []

    def add_expense(self):
        category = input("Enter Category:- ")
        description = input("Enter Description:- ")
        amount = input("Enter Amount:- ")
        date = input("Enter Date:- ")

        new_expense = Expense(category, description, amount, date)
        self.expense.append(new_expense)
        print("🎉 Expense added successfully!")

    def view_expense(self):
        if not self.expense:
            print("📭 No expenses found.")
        else:
            print(
                f"{'No':<4}{'Category':<12} {'Description':<15} {'Amount':<10} Rs {'Date'}"
            )
            print("-" * 55)
            for index, i in enumerate(self.expense, start=1):
                i.display(index)

    def search_expense(self, search):
        found = False
        if not search.strip():
            print("⚠️ Search cannot be empty.")
            return
        sear = search.strip().capitalize()
        count = 0
        for s in self.expense:
            if sear == s.description:
                if not found:
                    print(
                        f"{'No':<4}{'Category':<12} {'Description':<15} {'Amount':<10} Rs {'Date'}"
                    )
                    print("-" * 55)
                    found = True
                count += 1
                s.display(count)

        if not found:
            print("❌ No matching expense found.")

    def total_expense(self):
        if not self.expense:
            print("📭 No expenses to calculate.")
            return
        total = 0
        for i in self.expense:
            total = total + i.amount
        print(f"💰 Total Expense:- {total}")

    def delete_expense(self, delete):
        if delete <= 0 or delete > len(self.expense):
            print("⚠️ Please enter a valid expense number.")
            return
        index = delete - 1
        self.expense.pop(index)
        print("✅ Expense deleted successfully!")

    def exit(self):
        print("Thanks for using Expense Tracker! 👋")


def main():
    expense = ExpenseTracker()
    print("╔══════════════════════════╗")
    print("║     💰 EXPENSE TRACKER   ║")
    print("╚══════════════════════════╝")

    while True:
        print("╔══════════════════════════╗")
        print("║    1️⃣   Add Expenses      ║")
        print("║    2️⃣   View Expenses     ║")
        print("║    3️⃣   Search Expenses   ║")
        print("║    4️⃣   Total Expenses    ║")
        print("║    5️⃣   Delete Expenses   ║")
        print("║    6️⃣   Exit              ║")
        print("╚══════════════════════════╝")
        print("")

        try:
            choice = int(input("Enter choice 1 to 6:- "))
            print("")

            if choice == 1:
                expense.add_expense()
            elif choice == 2:
                expense.view_expense()
            elif choice == 3:
                b = input("🔍Search Expense:- ")
                expense.search_expense(b)
            elif choice == 4:
                expense.total_expense()
            elif choice == 5:
                c = int(input("🗑️ Enter expense NO. to Delete:- "))
                expense.delete_expense(c)
            elif choice == 6:
                expense.exit()
                break
            else:
                print("Invalid choice! please enter number 1-6")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
