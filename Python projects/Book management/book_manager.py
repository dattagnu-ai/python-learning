from book import Book
import json
import os


class BookManager:

    def __init__(self):
        self.books = []
        self.file_name = "book_manager.json"
        self.book_data()

    def add_books(self):
        book_id = input("Book ID: ")
        category = input("Category: ")
        title = input("Title: ")
        author = input("Author: ")
        price = input("Price: ")

        new_book = Book(book_id, category, title, author, price)
        self.books.append(new_book)
        self.save_file()
        print("")
        print("✅ Book added successfully!")

    def view_books(self):
        if not self.books:
            print("📚 Book list is empty.")
            return
        print("")
        print(
            f"{'Sr':<2} {'Book ID':<9} {'Category':<18} {'Title':<25} {'Author':<25} {'Price':<13}"
        )
        print("-" * 92)
        count = 0
        for book in self.books:
            count += 1
            book.display(count)

    def search_books(self, search):
        found = False
        sear = search.lower().strip()
        if not self.books:
            print("")
            print("📚 Book list is empty.")
            return
        count = 0
        for book in self.books:

            if (
                sear in book.category.lower()
                or sear in book.title.lower()
                or sear in book.author.lower()
            ):
                if not found:
                    print("")
                    print(
                        f"{'Sr':<2} {'Book ID':<9} {'Category':<18} {'Title':<25} {'Author':<25} {'Price':<13}"
                    )
                    print("-" * 92)
                found = True
                count += 1
                book.display(count)
        if not found:
            print("")
            print("🔍 No books found matching your search.")

    def delete_books(self, book_number):
        if not self.books:
            print("📚 Book list is empty.")
            return
        if book_number <= 0 or book_number > len(self.books):
            print("")
            print("⚠️ Please enter a valid Book number.")
            return
        index = book_number - 1
        self.books.pop(index)
        self.save_file()
        print("")
        print("✅ Book deleted successfully!")

    def exit(self):
        print("👋 Thank you for using Book Management System!")

    def book_data(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r") as file:
                    file_load = json.load(file)

                    self.books = [
                        Book(
                            item["Book ID"],
                            item["Category"],
                            item["Title"],
                            item["Author"],
                            item["Price"],
                        )
                        for item in file_load
                    ]
            except (json.JSONDecodeError, KeyError):
                self.books = []

    def save_file(self):
        with open(self.file_name, "w") as file:

            data = [book.to_dict() for book in self.books]
            json.dump(data, file)
