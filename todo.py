#!/usr/bin/env python3
"""
Simple Terminal-based Todo List Application
"""

def display_menu():
    """Display the menu options."""
    print("\n===== Todo List Menu =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("==========================")

def view_tasks(tasks):
    """Display all tasks with numbers."""
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("\nEnter the task description: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Error: Task description cannot be empty.")

def remove_task(tasks):
    """Remove a task by its number."""
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the todo list application."""
    tasks = []
    print("Welcome to the Todo List Application!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Thank you for using the Todo List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()