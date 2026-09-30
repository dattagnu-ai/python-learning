# upper() - all characters uppercase karto
# Use: user input normalize karaycha tevha
s = "hello world"
print(s.upper())  # HELLO WORLD

# lower() - all characters lowercase karto
# Use: case-insensitive comparison karaycha tevha
s = "HELLO WORLD"
print(s.lower())  # hello world

# title() - har word cha pehla letter uppercase karto
# Warning: apostrophe nantarcha letter pan uppercase hoto
s = "it's alive"
print(s.title())  # It'S Alive

# swapcase() - uppercase → lowercase, lowercase → uppercase SAGLE letters
s = "hello WORLD"
print(s.swapcase())  # HELLO world

# capitalize() - sirf pehla letter uppercase, baaki lowercase
s = "hello WORLD"
print(s.capitalize())  # Hello world

# count() - substring kiti vela aali te monto
# Warning: overlapping count hot nahi
s = "banana"
print(s.count("a"))  # 3

# startswith() - string kasha ne start hote te check karto
# Tuple pass karta yeto multiple check la
s = "model.pkl"
print(s.startswith(("ml_", "model")))  # True

# endswith() - string kasha ne end hote te check karto
# Tuple pass karta yeto multiple check la
s = "model.pkl"
print(s.endswith((".pkl", ".h5")))  # True
