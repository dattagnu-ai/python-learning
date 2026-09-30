from book_manager import BookManager


def main():
    book_manager = BookManager()
    print("╔══════════════════════════╗")
    print("║     📚 BOOK MANAGEMENT   ║")
    print("╚══════════════════════════╝")

    while True:
        print("\n╔══════════════════════════╗")
        print("║    1️⃣   Add Books         ║")
        print("║    2️⃣   View Books        ║")
        print("║    3️⃣   Search Books      ║")
        print("║    4️⃣   Delete Books      ║")
        print("║    5️⃣   Exit              ║")
        print("╚══════════════════════════╝")
        print("")
        try:
            choice = int(input("Enter your choice (1-5):- "))

            if choice == 1:
                book_manager.add_books()
            elif choice == 2:
                book_manager.view_books()
            elif choice == 3:
                b = input("Search books:- ")
                book_manager.search_books(b)
            elif choice == 4:
                try:
                    a = int(input("🗑️  Enter book NO. of delete:- "))
                    book_manager.delete_books(a)
                except ValueError:
                    print("")
                    print("⚠️ Please enter valid number")

            elif choice == 5:
                book_manager.exit()
                break
            else:
                print("")
                print("⚠️  Invalid choice. please enter a number between 1 - 5")
        except ValueError:
            print("")
            print("⚠️  Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
