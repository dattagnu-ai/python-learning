import random

while True:
    choice = input("press 'Enter' to the roll of dice or 'q' for quit\n")

    if choice == "q":
        print("Thanks for play a game! bye.")
        break
    elif choice == "":
        number = random.randint(1, 6)
        print(f"Your number is {number}")
    else:
        print("Invalid number")
