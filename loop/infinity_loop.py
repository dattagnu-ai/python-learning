word = "quit"
while True:
    a = input("enter a word:- ")
    print(a)
    if a == word:
        break


total = 0
count = 0

while True:
    num = input("Enter a number:- ")
    if num == "done":
        break
    a = int(num)
    total = total + a
    count = count + 1
if count > 0:

    average = total / count
    print(total)
    print(average)
else:
    print("No numbers entered")
