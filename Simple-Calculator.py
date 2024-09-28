def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero!"

while True:
    print("Choose operation: +, -, *, / (or 'q' to quit)")
    operator = input("Enter operator: ")

    if operator == 'q':
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print(f"Result: {add(num1, num2)}")
    elif operator == '-':
        print(f"Result: {subtract(num1, num2)}")
    elif operator == '*':
        print(f"Result: {multiply(num1, num2)}")
    elif operator == '/':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid operator!")
