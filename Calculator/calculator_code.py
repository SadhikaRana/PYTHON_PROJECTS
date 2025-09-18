def add(n1, n2):
    return n1 + n2         # while storing a function to a variable,
                     # only the name of the function is used without the parentheses
addition = add
#print(addition(5,5))
def subtract(n1,n2):
    return n1 - n2
subtraction = subtract
def multiply(n1,n2):
    return n1*n2
multiplication = multiply
def divide(n1,n2):
    return n1/n2
division = divide

operations = {
    "+" : add ,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

import art

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What's the first number?: "))

    while should_accumulate:
        for symbols in operations:
            print(symbols)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result},"
                       f"or type 'n' to start new calculation: " ).lower()
        if choice == 'y':
            num1 = result
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()
calculator()

