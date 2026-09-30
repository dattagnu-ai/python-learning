try:
    with open("sample.txt", "r") as file:
        rl1 = file.readline().strip()
        rl2 = file.readline().strip()
    print("Reading file content:")
    print(f"Line 1: {rl1}")
    print(f"Line 2: {rl2}")

except FileNotFoundError:

    print("Error: The file 'sample.txt' was not found")
