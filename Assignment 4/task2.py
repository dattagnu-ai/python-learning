with open("output.txt", "w") as file:
    ip = input("Enter text to write to the file: ")
    file.write(ip + "\n")
    print("Data successfully written to output.txt")

with open("output.txt", "a") as file:
    text = input("Enter additional text to append: ")
    file.write(text)
    print("Data successfully appended")
with open("output.txt", "r") as file:
    r = file.read()

    print("Final content of output.txt:")
    print(r)
