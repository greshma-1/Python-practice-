# To-Do List App (Very Simple)

tasks = []   # empty list to store tasks

while True:
    print("\n--- To-Do List ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # show tasks
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        # add task
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print("Task added!")

    elif choice == "3":
        # remove task
        if len(tasks) == 0:
            print("No tasks to remove!")
        else:
            task_no = int(input("Enter task number to remove: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Bye! 👋")
        break

    else:
        print("Invalid choice! Please try again.")
