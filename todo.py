# Define a dictionary to store tasks
tasks = {}

# Define a function to add a task


def add_task():
    task_name = input("Enter task name: ")
    tasks[task_name] = False

# Define a function to view tasks


def view_tasks():
    for task, completed in tasks.items():
        status = "Completed" if completed else "Not completed"
        print(f"{task}: {status}")

# Defina a function to mark a task as completed


def complete_task():
    task_name = input("Enter task name: ")
    if task_name in tasks:
        tasks[task_name] = True
        print("Task marked as completed")
    else:
        print("Task not found")

# Define a function to delete a task


def delete_task():
    task_name = input("Enter task name: ")
    if task_name in tasks:
        del tasks[task_name]
        print("Task deleted")
    else:
        print("Task not found")

# Define the main function


def main():
    while True:
        print("\n\n1. Add a task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Quit")
        choice = input("\nEnter your choice (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
