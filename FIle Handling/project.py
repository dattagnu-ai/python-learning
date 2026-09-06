import json


def add_students(name, marks):
    student = {"Name": name, "Marks": marks}

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []

    students.append(student)

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def view_students():
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
            for value in students:
                print(f'Name:- {value["Name"]}')
                print(f"Marks:- {value['Marks']}")
                print("----------------------")

    except FileNotFoundError:
        print("First add a Students")


def search_students(search):
    try:
        found = False

        with open("students.json", "r") as file:
            students = json.load(file)
        for name in students:
            if name["Name"] == search:
                found = True
                print("----------------------")
                print(f'Name:- {name["Name"]}')
                print(f'Marks:- {name["Marks"]}')
                print("----------------------")
        if not found:
            print("Student Not Found")
    except FileNotFoundError:
        print("File Not Found")


def update_marks(name, marks):
    try:

        found = False
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        print("File Not Found")

    else:

        for i in students:

            if i["Name"] == name:
                i["Marks"] = marks
                found = True
                break
        if not found:
            print("Student Not Found")

        else:
            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)


def delete_students(name):
    try:
        found = False
        with open("students.json", "r") as file:
            students = json.load(file)
        for student in students:
            if student["Name"] == name:
                students.remove(student)
                found = True
                break
        if not found:
            print("Student Not Found")
        else:
            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)
    except FileNotFoundError:
        print("File Not Found")


def exit_app():
    print("Thank You For Visiting!")


def main():

    print("=========================")
    print(" STUDENT RECORD MANAGER ")
    print("=========================\n")
    while True:
        print("1. Add Students\n")
        print("2. View Students\n")
        print("3. Search Students\n")
        print("4. Update students\n")
        print("5. Remove Students\n")
        print("6. EXIT\n")
        choice = input("Enter Choice :- ")

        if choice == "1":
            name = input("Student Name:- ")
            marks = float(input("Enter Marks:- "))
            add_students(name, marks)
        elif choice == "2":
            view_students()
        elif choice == "3":
            name = input("Student Name:- ")
            search_students(name)
        elif choice == "4":
            name = input("Student Name:- ")
            marks = float(input("Enter Marks:- "))
            update_marks(name, marks)
        elif choice == "5":
            name = input("Student Name:- ")
            delete_students(name)
        elif choice == "6":
            exit_app()
            break
        else:
            print("Invalid Choice, Retry!")
            print("=========================\n")


main()
