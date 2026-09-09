from datetime import datetime
    
def add_expense(category,amount,description,date):
    
def view_expense():
    pass
def search_expense():
    pass
def total_expense():
    pass
def delete_expense():
    pass
def exit(self):
    print("Thanks For Visit!")


def main():
    
    print("===================")
    print("  Expense tracker")
    print("===================")

    while True:

        print("1: Add Expenses")
        print("2: View Expenses")
        print("3: Search Expenses")
        print("4: Total Expenses")
        print("5: Delete Expenses")
        print("6: Exit")

        try:
            choice = int(input("Enter choice 1 to 6:- "))

            if choice == 1:
                a = input("Enter Expense:- ")
                add_expense(a)
            elif choice == 2:
                view_expense()
            elif choice == 3:
                b = input("Search Expense:- ")
                search_expense(b)
            elif choice == 4:
                total_expense()
            elif choice == 5:
                c = input("search Expense:- ")
                delete_expense(c)
            elif choice == 6:
                exit()
                break
            else:
                print("Invalid Choice! please Enter number 1-6")
        except ValueError:
            print("Please Enter Only Digits")


main()
