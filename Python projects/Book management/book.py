class Book:
    def __init__(self, book_id, category, title, author, price):
        try:
            if int(book_id) < 0:
                print("❌ Invalid Book ID! Please enter a positive number.")
                self.book_id = 0
            else:
                self.book_id = int(book_id)
        except (ValueError, TypeError):
            print("❌ Invalid Book ID! Please enter a valid number.")
            self.book_id = 0
        self.category = category.strip().capitalize() if category else "Other"
        self.title = title.strip().capitalize() if title.strip() else "-"
        self.author = author.strip().capitalize() if author else "-"
        try:
            if float(price) < 0:
                print("⚠️ Price cannot be negative.")
                self.price = 0.0
            else:
                self.price = float(price)
        except (ValueError, TypeError):
            self.price = 0.0

    def display(self, count):

        print(
            f"{count}: {self.book_id:<9} {self.category:<18} {self.title:<25} {self.author:<25} Rs{self.price:<13.2f}"
        )

    def to_dict(self):
        return {
            "Book ID": self.book_id,
            "Category": self.category,
            "Title": self.title,
            "Author": self.author,
            "Price": self.price,
        }
