# Program Code: OP-HOT-02
# Title: Design a Multi-Operator Calculator
# Cognitive Skill: Higher Order Thinking (Design from Scratch)
# Topic: Operators in Python

# Design challenge: Build a calculator that handles ALL operator types.
# The user picks what they want to calculate — you handle it!

print("╔══════════════════════════════╗")
print("║   Progra Smart Calculator   ║")
print("╚══════════════════════════════╝")
print()
print("What do you want to calculate?")
print("1. Arithmetic (+ - * / // % **)")
print("2. Check a comparison (== != > < >= <=)")
print("3. Combine conditions (and / or / not)")
print("4. Operator Precedence Explorer")
print()

choice = input("Enter 1, 2, 3, or 4: ")

# --- Option 1: Arithmetic ---
if choice == "1":
    a = float(input("Enter first number: "))
    print("Operators: + - * / // % **")
    op = input("Enter operator: ").strip()
    b = float(input("Enter second number: "))

    if op == "+":
        print(f"{a} + {b} = {a + b}")
    elif op == "-":
        print(f"{a} - {b} = {a - b}")
    elif op == "*":
        print(f"{a} * {b} = {a * b}")
    elif op == "/":
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Error: Cannot divide by zero!")
    elif op == "//":
        if b != 0:
            print(f"{a} // {b} = {a // b}")
        else:
            print("Error: Cannot divide by zero!")
    elif op == "%":
        if b != 0:
            print(f"{a} % {b} = {a % b}")
        else:
            print("Error: Cannot modulo by zero!")
    elif op == "**":
        print(f"{a} ** {b} = {a ** b}")
    else:
        print("Unknown operator!")

# --- Option 2: Comparison ---
elif choice == "2":
    a = float(input("Enter first number: "))
    print("Operators: == != > < >= <=")
    op = input("Enter comparison operator: ").strip()
    b = float(input("Enter second number: "))

    if op == "==":
        result = a == b
    elif op == "!=":
        result = a != b
    elif op == ">":
        result = a > b
    elif op == "<":
        result = a < b
    elif op == ">=":
        result = a >= b
    elif op == "<=":
        result = a <= b
    else:
        result = "Unknown operator"

    print(f"{a} {op} {b} → {result}")

# --- Option 3: Logic ---
elif choice == "3":
    print("Enter two conditions as True or False:")
    c1 = input("Condition 1 (True/False): ").strip().lower() == "true"
    op = input("Operator (and/or/not): ").strip().lower()
    if op != "not":
        c2 = input("Condition 2 (True/False): ").strip().lower() == "true"

    if op == "and":
        print(f"{c1} and {c2} → {c1 and c2}")
    elif op == "or":
        print(f"{c1} or {c2} → {c1 or c2}")
    elif op == "not":
        print(f"not {c1} → {not c1}")
    else:
        print("Unknown operator")

# --- Option 4: Precedence ---
elif choice == "4":
    print("Enter an expression to evaluate (e.g., 5 + 3 * 2):")
    expr = input("> ")
    try:
        result = eval(expr)
        print(f"Result: {result}")
        print("(Python applied BODMAS automatically!)")
    except:
        print("Invalid expression. Try again.")
