import art 

#calculator

#Add
def add(n1, n2):
    return n1 + n2

#substract
def subtract(n1,n2):
    return n1 - n2

#multiply
def multiply(n1,n2):
    return n1 * n2

#divide
def divide(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():

    running = True

    print(art.logo)

    num1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)

    operation_symbol = input("Pick an operation from the line above: ")

    num2 = float(input("What's the next number? "))

    answer = operations[operation_symbol](num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    while running:

        response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if response == 'y':
            operation_symbol = input("Pick another operation: ")
            num3 = float(input("What's the next number?: "))

            newAnswer = operations[operation_symbol](answer,num3)
            print(f"{answer} {operation_symbol} {num3} = {newAnswer}")
            answer = newAnswer
        else:
            running = False
            calculator()

calculator()
