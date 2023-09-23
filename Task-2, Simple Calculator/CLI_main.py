# Codsoft Task-2 
# ______________

# Define a function for each arithmetic operation
# _______________________________________________
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

# Main Program
# ____________

def main():

    # Display a menu to the user
    # __________________________

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Input two numbers and the operation choice from the user
    # ________________________________________________________

    choice = int(input("Enter choice (1/2/3/4): "))
    features = [1,2,3,4]

    if choice in features:
        val1 = float(input("Enter first number: "))
        val2 = float(input("Enter second number: "))

        if choice == features[0]:
            result = add(val1, val2)
            print("Result: ", round(result,2))
        elif choice == features[1]:
            result = subtract(val1, val2)
            print("Result: ", round(result,2))
        elif choice == features[2]:
            result = multiply(val1,val2)
            print("Result: ", round(result,2))
        elif choice == features[3]:
            result = divide(val1, val2)
            print("Result: ",result)
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()