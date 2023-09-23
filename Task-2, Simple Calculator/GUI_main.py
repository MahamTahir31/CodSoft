# Codsoft Task-2 
# ______________

import tkinter as tk
from tkinter import ttk

# Define arithmetic operations as functions
# _________________________________________
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# Function to perform the calculation
# ___________________________________
def calculate():
    val1 = float(entry_val1.get())
    val2 = float(entry_val2.get())
    choice = operation_choice.get()

    if choice == "Addition":
        result = add(val1, val2)
    elif choice == "Subtraction":
        result = subtract(val1, val2)
    elif choice == "Multiplication":
        result = multiply(val1, val2)
    elif choice == "Division":
        result = divide(val1, val2)
    
    result_label.config(text=f"Result: {result}")

# Create the main GUI window
# __________________________
root = tk.Tk()
root.title("Calculator")

# Create a frame for better styling
# _________________________________
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Create input fields and labels with improved styling
# ____________________________________________________
entry_val1 = ttk.Entry(frame)
entry_val1.grid(row=0, column=1, padx=5, pady=5)

entry_val2 = ttk.Entry(frame)
entry_val2.grid(row=1, column=1, padx=5, pady=5)

operation_choice = tk.StringVar()
# Default operation choice
# ________________________
operation_choice.set("Addition")  

operation_label = ttk.Label(frame, text="Select operation:")
operation_label.grid(row=2, column=0, columnspan=2, pady=10)

operation_menu = ttk.OptionMenu(frame, operation_choice, "Addition", "Subtraction", "Multiplication", "Division")
operation_menu.grid(row=2, column=2, padx=5, pady=5)

calculate_button = ttk.Button(frame, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=3, pady=10)

result_label = ttk.Label(frame, text="")
result_label.grid(row=4, column=0, columnspan=3, pady=10)

# Apply padding and expand options for widgets
# ____________________________________________
for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=5)
    
frame.columnconfigure((0, 1, 2), weight=1)

# Start the Tkinter main loop
# ___________________________
root.mainloop()
