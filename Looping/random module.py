# Shuffle a list of numbers randomly

import random

num = [1, 2, 3, 4, 5]
random.shuffle(num)
print(num)


# Random integer between 1-100, random fruit from list

import random

print(random.randint(1, 100))

fruits = ["apple", "banana", "mango", "grapes"]
print(random.choice(fruits))


# Shuffle cards and pick one randomly


import random

cards = ["A", "k", "q", "j", "10"]

random.shuffle(cards)
print(cards)
print(random.choice(cards))


# Assign random turn order to players using shuffle and while loop

import random

players = ["Dattu", "Rahul", "Shreya", "Amit", "Sneha"]
turn = 0
random.shuffle(players)
while turn < len(players):
    players[turn]
    print(f"turn {turn+ 1}: {players[turn]}")
    turn += 1
