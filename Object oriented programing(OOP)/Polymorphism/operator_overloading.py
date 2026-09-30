# class point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return point(self.x + other.x, self.y + other.y)


# p1 = point(10, 20)
# p2 = point(5, 15)


# result = p1 + p2
# print(result.x)
# print(result.y)


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __eq__(self, other):
#         return self.price == other.price


# p1 = Product("Phone", 20000)
# p2 = Product("Laptop", 20000)
# p3 = Product("Mouse", 1000)

# print(p1 == p2)
# print(p1 == p3)


# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"


# book = Book("Python Basics", "John", 500)

# print(book)


# class Playlist:
#     def __init__(self, songs):
#         self.songs = songs

#     def __len__(self):
#         return len(self.songs)


# playlist = Playlist(["Song A", "Song B", "Song C"])
# print(len(playlist))


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Laptop", 50000)
p2 = Product("Phone", 30000)

print(p1 > p2)
