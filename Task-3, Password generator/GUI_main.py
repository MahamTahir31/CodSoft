# Codsoft Task-3
# ______________

import tkinter as tk
from tkinter import ttk
import random
import string

# Function to generate a random password
# ______________________________________
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    if length < 4:
        return "Error: Password length should be at least 4 characters!"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to generate a password and update the result label
# ___________________________________________________________
def generate_update_password():
    try:
        password_length = int(password_length_entry.get())
        password = generate_password(password_length)
        result_label.config(text="\nGenerated Password: " + password)
    except ValueError:
        result_label.config(text="Please enter a valid number for password length!")

# Create the main GUI window
# __________________________
root = tk.Tk()
root.title("Password Generator")

# Create a frame for better styling
# _________________________________
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Create labels and entry fields
# ______________________________
password_length_label = ttk.Label(frame, text="Enter password length:")
password_length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

password_length_entry = ttk.Entry(frame)
password_length_entry.grid(row=0, column=1, padx=5, pady=5)

generate_button = ttk.Button(frame, text="Generate Password", command=generate_update_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Apply padding and expansion options for widgets
# _______________________________________________
for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=5)
    
frame.columnconfigure((0, 1), weight=1)

# Start the Tkinter main loop
# ___________________________
root.mainloop()
