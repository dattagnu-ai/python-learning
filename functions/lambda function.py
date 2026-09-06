names = ["Python", "C", "Java", "JavaScript"]

# Lambda वापरून नावांच्या लांबीनुसार (len) Sort करा
sorted_names = sorted(names, key=lambda x: len(x))

print(sorted_names)


result = lambda a: a * a
fun = result(5)
print(fun)


numbers = [5, 2, 8, 1, 9, 3]

func = sorted(numbers, key=lambda x: x, reverse=True)
print(func)


stationery = [("Pen", 20), ("Book", 150), ("Bag", 500)]
sorted_books = sorted(stationery, key=lambda x: x[1], reverse=True)
print(sorted_books)

# x[1] he pratyek vaastu chi price show karnya cha kam karat ahe
