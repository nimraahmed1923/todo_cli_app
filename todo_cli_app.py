import json
import os

# ==============================
# LOAD TASKS FROM FILE
# ==============================
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# ==============================
# SAVE TASKS TO FILE
# ==============================
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved! ✅")

# ==============================
# ADD TASK
# ==============================
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task} ✅")

# ==============================
# REMOVE TASK
# ==============================
def remove_task(tasks):
    if len(tasks) == 0:
        print("No tasks to remove! ❌")
        return
    
    list_tasks(tasks)
    
    try:
        number = int(input("Enter task number to remove: "))
        
        if number < 1 or number > len(tasks):
            print("Invalid number! ❌")
            return
            
        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Removed: {removed} ✅")
        
    except ValueError:
        print("Please enter a valid number! ❌")

# ==============================
# LIST ALL TASKS
# ==============================
def list_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found! ❌")
        return
    
    print("\n=== YOUR TASKS ===")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("==================\n")

# ==============================
# MAIN MENU
# ==============================
def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== TO-DO APP ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")
        print("=================")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == "1":
            add_task(tasks)
            
        elif choice == "2":
            remove_task(tasks)
            
        elif choice == "3":
            list_tasks(tasks)
            
        elif choice == "4":
            print("Goodbye Nimmi! 👋")
            break
            
        else:
            print("Invalid choice! Enter 1-4 ❌")

# RUN THE APP!
main()