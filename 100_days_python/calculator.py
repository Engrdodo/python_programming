def add(n1, n2):
    """Adds two numbers""" #docstrings
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    }

def calculator():
    num1 = float(input("What is the first number?: "))
    for operator in operations:
        print(operator)
    should_continue = True

    while should_continue:
        operation_symbol =  input("Pick an operator: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol] #takes the value associated with keys
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        option = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
        if option == "y":
            num1 = answer
        else:
            should_continue = False
            calculator() #recursion, function calling itself

calculator()
