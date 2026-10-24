def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operation")
        return

    print("Result:", result)


main()