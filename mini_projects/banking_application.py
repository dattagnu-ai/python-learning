# Banking Application
from datetime import datetime

balance = 0
name = ""
transaction_history = []


def create_account():
    global balance, name
    if name != "":
        print("Account already exists.")
        return
    name = input("Enter Name:- ")
    if name.strip() == "":
        print("Name cannot be empty.")
        return
    amount = int(input("Enter initial balance:- "))
    timestamp = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")

    if amount <= 0:
        print(f"Account Not create because Amount is {amount}")
    else:
        balance = amount
        transaction_history.append(f"[{timestamp}] Initial Deposit {amount}")
        print("Account has been created")
        print(f"Name:- {name}")
        print(f"Balance:- {balance}")
        print("===================")


def deposit_amount():
    global balance
    if name == "":
        print("Please create account first")
        return
    deposit = int(input("Enter Deposit Amount:- "))
    if deposit <= 0:
        print(f"Sorry! {deposit} is not deposit Amount")
    else:
        balance += deposit
        timestamp = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        transaction_history.append(f"[{timestamp}] Deposit: {deposit}")
        print("SUCCESSFUL!")
        print(f"Your deposit Amount is {deposit}")
        print(f"Total Balance = {balance}")
        print("===================")


def withdrawal_amount():
    global balance
    if name == "":
        print("Please create account first")
        return
    withdrawal = int(input("Enter Withdrawal Amount:- "))
    if withdrawal <= 0:
        print(f"Sorry! {withdrawal} is not Withdrawal Amount")
    elif withdrawal <= balance:
        balance -= withdrawal
        timestamp = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        transaction_history.append(f"[{timestamp}] Withdrawal: {withdrawal}")
        print("SUCCESSFUL!")
        print(f"Your Withdrawal Amount {withdrawal}")
        print(f"Total Balance = {balance}")
        print("===================")

    else:
        print("Insufficient Balance")


def check_balance():
    if name == "":
        print("Please create account first")
        return
    print("=============================\n")
    print(f"Account Holder:- {name}")
    print(f"Balance Amount = {balance}")
    print("\n=============================")


def exit_app():
    print("Thank you for using Python Bank 😊")
    print("===================")


def main():
    print("======================")
    print("Welcome to python Bank")
    print("======================\n")
    while True:
        print("1. Create Account")
        print("2. Deposit Amount")
        print("3. Withdrawal Amount")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")
        choice = input("Enter Choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_amount()
        elif choice == "3":
            withdrawal_amount()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("======================")
            print("TRANSACTION HISTORY")
            print("======================")
            if not transaction_history:
                print("Sorry! Not found any transaction")
            else:
                for transaction in transaction_history:
                    print(transaction)
            print(f"Total Balance = {balance}")

        elif choice == "6":
            exit_app()
            break
        else:
            print("Invalid Choice!!! Retry")


if __name__ == "__main__":
    main()
