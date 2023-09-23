# Codsoft Task-1
# ______________

import tkinter as tk
from tkinter import ttk

def display_list():
    with open("todo_list.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            listbox.delete(0, tk.END)
            for i, task in enumerate(tasks, start=1):
                listbox.insert(tk.END, f"{i}. {task.strip()}")
        else:
            listbox.insert(tk.END, "Your to-do list is empty!")

def add_task():
    task = task_entry.get()
    if task:
        with open("todo_list.txt", "a") as file:
            file.write(task + "\n")
        task_entry.delete(0, tk.END)
        display_list()

def remove_task():
    task_index = listbox.curselection()
    if task_index:
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
        index = task_index[0]
        removed_task = tasks.pop(index)
        with open("todo_list.txt", "w") as file:
            file.writelines(tasks)
        display_list()

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

listbox = tk.Listbox(frame, selectmode=tk.SINGLE)
listbox.pack()

task_entry = tk.Entry(frame)
task_entry.pack()

# Create a ttk style object
# _________________________
style = ttk.Style()

# Define a custom style for buttons
# _________________________________
style.configure("Custom.TButton", padding=10, background="blue", foreground="black", font=("Helvetica", 10))

add_button = ttk.Button(frame, text="Add Task", style="Custom.TButton", command=add_task)
add_button.pack()

remove_button = ttk.Button(frame, text="Remove Task", style="Custom.TButton", command=remove_task)
remove_button.pack()

display_list()

root.mainloop()
