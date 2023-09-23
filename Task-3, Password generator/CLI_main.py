# Codsoft Task-3
# ______________

import random
import string

# Function to generate a random password
# ______________________________________
def generate_password(length):
    # Define the characters to use for generating the password
    # ________________________________________________________
    characters = string.ascii_letters + string.digits + string.punctuation

    # Check if the desired length is valid
    # ____________________________________
    if length < 4:
        return "Error: Password length should be at least 4 characters!\n"

    # Generate the password
    # _____________________
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt the user for the desired password length
# _______________________________________________
try:
    password_length = int(input("\nEnter the desired password length: "))
    
    # Generate and display the password
    # _________________________________
    password = generate_password(password_length)
    print("\nGenerated Password:", password , "\n")
except ValueError:
    print("\nPlease enter a valid number for password length!\n")
