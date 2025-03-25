# Basic Calculator Program

def calculator():
    try:
        # Get user input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Get user input for the operation
        operator = input("Enter operation (+, -, *, /): ").strip()
        
        # Perform calculation based on operator
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operator. Please use +, -, *, or /.")
            return
        
        # Display the result
        print(f"{num1} {operator} {num2} = {result}")

    except ValueError:
        print("Error: Please enter valid numeric values.")

# Run the calculator
calculator()
