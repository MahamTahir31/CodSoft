# Codsoft Task-1
# ______________

# Function to display the todo list
# _________________________________

def display_list():
    with open("todo_list.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            print("\t\t\t\t\t\t\tTo-Do List:\n\t\t\t\t\t\t\t===========")
            for i, task in enumerate(tasks, start=1):
                print(f"\t\t\t\t\t\t\t{i}. {task.strip()}")
        else:
            print("\t\t\t\t\t\t\tYour to-do list is empty!")

# Function to add a task to the to-do list
# ________________________________________

def add_task(task):
    with open("todo_list.txt", "a") as file:
        file.write(task + "\n")
    print(f"\t\t\t\t\t\t\tAdded task: {task}")

# Function to remove a task from the to-do list
# _____________________________________________

def remove_task(task_index):
    with open("todo_list.txt", "r") as file:
        tasks = file.readlines()
    
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        with open("todo_list.txt", "w") as file:
            file.writelines(tasks)
        print(f"\t\t\t\t\t\t\tRemoved task: {removed_task.strip()}")
    else:
        print("\n\t\t\t\t\t\t\tInvalid task \n\t\t\t\t\t\t\t___________")

# Main Function
# _____________

def main():
    while True:
        print("\n\t\t\t\t\t\t\tOptions:\n\t\t\t\t\t\t\t=========")
        print("\t\t\t\t\t\t\t1. Display To-Do List")
        print("\t\t\t\t\t\t\t2. Add Task")
        print("\t\t\t\t\t\t\t3. Remove Task")
        print("\t\t\t\t\t\t\t4. Exit")

        choice = input("\t\t\t\t\t\t\tEnter your choice: ")

        if choice == "1":
            display_list()
        elif choice == "2":
            task = input("\t\t\t\t\t\t\tEnter the task: ")
            add_task(task)
        elif choice == "3":
            task_index = int(input("\t\t\t\t\t\t\tEnter the task index to remove: "))
            remove_task(task_index)
        elif choice == "4":
            print("\t\t\t\t\t\t\tGoodbye!")
            break
        else:
            print("\n\t\t\t\t\t\t\tInvalid choice. Please try again.\n\t\t\t\t\t\t\t_________________________________")

if __name__ == "__main__":
    main()
