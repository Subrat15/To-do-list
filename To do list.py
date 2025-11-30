tasks = []

def show_menu():
    print("\nTO-DO LIST MENU")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks found!")
    else:
        print("\n My Task")
        for index, task in enumerate(tasks):
            status = "✔ Completed" if task["completed"] else "❌ Not Completed"
            print(f"{index + 1}. {task['title']}  --> {status}")

def add_task():
    title = input("Enter task name: ")
    tasks.append({"title": title, "completed": False})
    print("Task added successfully!")

def update_task():
    view_tasks()
    task_no = int(input("\nEnter task number to update: ")) - 1
    
    if 0 <= task_no < len(tasks):
        new_title = input("Enter new task name: ")
        tasks[task_no]["title"] = new_title
        print("Task updated successfully!")
    else:
        print("Invalid task number!")

def delete_task():
    view_tasks()
    task_no = int(input("\nEnter task number to delete: ")) - 1

    if 0 <= task_no < len(tasks):
        tasks.pop(task_no)
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

def mark_completed():
    view_tasks()
    task_no = int(input("\nEnter task number to mark as completed: ")) - 1

    if 0 <= task_no < len(tasks):
        tasks[task_no]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")
while True:
    show_menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        mark_completed()
    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")