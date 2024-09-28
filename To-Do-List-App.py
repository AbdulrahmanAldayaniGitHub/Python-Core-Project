tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def view_tasks():
    print("Your Tasks:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")

def delete_task(index):
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index-1)
        print(f"Deleted task: {removed_task}")
    else:
        print("Invalid task number")

# More functions for updating tasks, saving to file, loading from file, etc.
