# Create a simple number guessing game.
# The user gets 10 chances to guess a number.
# If the user guesses the number before 10 chances, stop asking the number from the user, say Congrats and end the game
# if the user never guesses the number, ask them 10 times and then end the game!!

import random

won = False
count1 = 0
count2 = 10
print("welcome to the number guessing game. We have a number thats need to be guess")
a = random.randint(1, 10)
while count1 < 10:
    b = int(input("Guess a number:- "))
    count1 = count1 + 1
    if b == a:
        print("Congrats")
        won = True
        break
    elif b < a:
        print("Your guess is Wrong! Try higher")
    elif b > a:
        print("Your guess is Wrong! Try lower")
    count2 = count2 - 1
    print(f"You have {count2} Attempt left")

if won == False:
    print("Game over!")
    print(f"The number was {a}")
