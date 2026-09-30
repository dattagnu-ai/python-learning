# import random
# while True
# input() ghe
# Jar "y" asel → random.randint(1,6) print kar.
# Jar "n" asel → break


import random

while True:
    dice = input("Roll a dice? (y/n):- ")
    if dice == "y":
        print(random.randint(1, 6))
    else:
        break
