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

running = True

num1 = int(input("What's the first number?: "))

for key in operations:
    print(key)

operation_symbol = input("Pick an operation from the line above: ")

while running:

    num2 = int(input("What's the next number? "))

    answer = operations[operation_symbol](num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower() == 'y':
        
        num2 = int(input("What's the next number? "))

    else:
        running = False
        
    #operation_symbol = input("Pick another operation: ")
    #num3 = int(input("What's the next number?: "))

    #newAnswer = operations[operation_symbol](answer,num3)

    #print(f"{answer} {operation_symbol} {num3} = {newAnswer}")





