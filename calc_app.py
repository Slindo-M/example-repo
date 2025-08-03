# This programs performs and records simple calculations.
# This programs requires user input.
# This program performs and records simple calculations or prints previous ones.

equations_list = []
operations = ["+", "-", "*", "/"]

user_choice = input("Please select 'PC' to perform a calculation or 'PPC' to print previous calculations: ")

if user_choice.upper() == "PC":
    equation = input("Enter a simple equation using two numbers (e.g. 5 + 3): ")

    # Split and validate the equation
    for op in operations:
        if op in equation:
            parts = equation.split(op)
            if len(parts) == 2:
                try:
                    num1 = float(parts[0].strip())
                    num2 = float(parts[1].strip())
                    result = None
                    if op == "+":
                        result = num1 + num2
                    elif op == "-":
                        result = num1 - num2
                    elif op == "*":
                        result = num1 * num2
                    elif op == "/":
                        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
                    
                    output = f"{num1} {op} {num2} = {result}"
                    print(output)
                    # Save to file
                    with open("equations.txt", "a", encoding="utf-8") as file:
                        file.write(output + "\n")
                except ValueError:
                    print("Please enter valid numbers.")
                break
    else:
        print("Please enter a valid equation with a supported operator (+, -, *, /).")

elif user_choice.upper() == "PPC":
    try:
        with open("equations.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            if lines:
                print("Previous calculations:")
                for line in lines:
                    print(line.strip())
            else:
                print("No previous calculations found.")
    except FileNotFoundError as error:
        print("The file you're trying to open does not exist.")
        print(error)
else:
    print("Invalid choice. Please enter 'PC' or 'PPC'.")

    