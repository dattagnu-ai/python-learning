import json
import os


class Task:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists("Tasks.json"):
            try:
                with open("Tasks.json", "r") as file:
                    self.tasks = json.load(file)
            except FileNotFoundError:
                self.tasks = []

    def save_tasks(self):
        with open("Tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_tasks(self, task):
        if not task.strip():
            print("Invalid Task! Please enter a task.")
        else:
            self.tasks.append(task)
            self.save_tasks()
            print(f"{task} Added to the list")

    def show_tasks(self):
        if not self.tasks:
            print("No task available")
            return

        count = 0
        for i in self.tasks:
            count += 1
            print(f"{count}: {i}")

    def delete_task(self, number):
        index = number - 1
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
            print("Task deleted successful")
        else:
            print("Invalid Task Number")

    def mark_task_completed(self, number):
        index = number - 1

        if 0 <= index < len(self.tasks):
            if not self.tasks[index].endswith("✔️"):
                self.tasks[index] += "✔️"
                self.save_tasks()
                print(f"Task marked completed {self.tasks[index]}")
                
            else:
                print("This Task already complete")
        else:
            print("Invalid Task")

    def exit(self):
        print("Thanks For Visit!")


def main():
    task = Task()
    print("======================")
    print("      TO DO LIST")
    print("======================")

    while True:
        
        print("")
        print("1: Add Task")
        print("2: View Task")
        print("3: Remove Task")
        print("4: Mark to complete task")
        print("5: Exit")
        try:
            choice = int(input("Enter Choice 1 to 5:- "))

            if choice == 1:

                a = input("Enter a Task:- ")
                task.add_tasks(a)
            elif choice == 2:
                task.show_tasks()
            elif choice == 3:
                try:
                    b = int(input("Enter a Task:- "))
                    task.delete_task(b)
                except ValueError:
                    print("Invalid Task Number! Please enter a valid number.")

            elif choice == 4:
                try:
                    c = int(input("Enter a Task:- "))
                    task.mark_task_completed(c)
                except ValueError:
                    print("Invalid Task Number! Please enter a valid number.")

            elif choice == 5:
                task.exit()
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Invalid Choice! Please enter a number from 1 to 5.")


main()
