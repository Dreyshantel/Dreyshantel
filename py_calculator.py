print("WELCOME TO PYTHON CALCULATOR!")


# create pemdas function for calculator
# additon
def add(n1, n2):
    return n1 + n2


# subtraction
def subtract(n1, n2):
    return n1 - n2


# multiplication
def multiply(n1, n2):
    return n1 * n2


# Division
def divide(n1, n2):
    return n1 / n2


# create a recursion function for calculator
def calculator():
    """
    create an input variable for numbers and generate an operation symbols
    """
    num1 = float(input("what's the first number? "))
    operation = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    for symbol in operation:
        print(symbol)

    # create a while loop for calculator to repeat calculation and  flag switch for calculator
    should_continue = True

    while should_continue:
        operation = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide
        }
        operation_symbol = input("pick an operation: ")
        new_num = float(input("What's the next number? "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, new_num)

        print(f"{num1} {operation_symbol} {new_num}: {answer}")

        if input(f"type 'y' to continue calculation with {answer}, type 'n' to exit. ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

        # invoking the calculator function


calculator()
