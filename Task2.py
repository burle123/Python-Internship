#TASK SCHEDULER
# Problem : 
# Maintain Task List:
# -Add task
# -Mark Complete
# -Delete task
# -Show Pending/Completed

# TASK SCHEDULER

tasks = []              # List to store tasks
completed = []          # List to store completed tasks

while True:
    print("\n===== TASK SCHEDULER =====")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. Delete Task")
    print("4. Show Pending Tasks")
    print("5. Show Completed Tasks")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # Add Task
    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    # Mark Task as Complete
    elif choice == '2':
        if len(tasks) == 0:
            print("No pending tasks!")
        else:
            print("\nPending Tasks:")
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])
            num = int(input("Enter task number to mark complete: "))
            if 1 <= num <= len(tasks):
                completed.append(tasks[num-1])
                tasks.pop(num-1)
                print("Task marked as completed!")
            else:
                print("Invalid task number!")

    # Delete Task
    elif choice == '3':
        if len(tasks) == 0:
            print("No pending tasks to delete!")
        else:
            print("\nPending Tasks:")
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num-1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")

    # Show Pending Tasks
    elif choice == '4':
        if len(tasks) == 0:
            print("No pending tasks!")
        else:
            print("\nPending Tasks:")
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])

    # Show Completed Tasks
    elif choice == '5':
        if len(completed) == 0:
            print("No completed tasks!")
        else:
            print("\nCompleted Tasks:")
            for i in range(len(completed)):
                print(i+1, ".", completed[i])

    # Exit
    elif choice == '6':
        print("Exiting Task Scheduler. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-6.")

