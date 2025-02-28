def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_no = int(input("Enter task number to remove: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
