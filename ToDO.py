TASK_FILE="tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return [line.rstrip("\n") for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
           file.write(task + "\n")


def main():
    tasks = load_tasks()

    while True:
        print("\nTO-DO LIST")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            if not tasks:
                print("No Tasks Available.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter the New Task: ")
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task Added Successfully.")

        elif choice == "3":
            if not tasks:
                print("No Tasks Available to Remove.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    index = int(input("Enter the Task Number to Remove: "))
                except ValueError:
                    print("Invalid number.")
                    continue

                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                    print("Task Removed Successfully.")
                else:
                    print("Task number out of range.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
