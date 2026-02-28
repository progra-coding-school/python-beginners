# Program Code: EX-KN-01
# Title: What Is an Exception?
# Cognitive Skill: Knowledge
# Topic: Exceptions in Python

# An EXCEPTION is an error that happens WHILE a program is running.
# Without handling it, the program CRASHES and stops.

# --- Common exceptions you will see ---

print("=== 1. ZeroDivisionError ===")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Caught:", e)

print()

print("=== 2. TypeError ===")
try:
    result = "age" + 13     # can't add string and int
except TypeError as e:
    print("Caught:", e)

print()

print("=== 3. ValueError ===")
try:
    num = int("hello")      # "hello" can't become an integer
except ValueError as e:
    print("Caught:", e)

print()

print("=== 4. NameError ===")
try:
    print(unknown_variable)  # variable doesn't exist
except NameError as e:
    print("Caught:", e)

print()

print("=== 5. IndexError ===")
try:
    fruits = ["mango", "banana"]
    print(fruits[10])       # index 10 doesn't exist
except IndexError as e:
    print("Caught:", e)

print()

print("=== 6. KeyError ===")
try:
    info = {"name": "Aarav"}
    print(info["age"])      # key 'age' doesn't exist
except KeyError as e:
    print("Caught:", e)

print()

# --- What happens WITHOUT exception handling ---
print("=== WITHOUT handling — program crashes ===")
print("If you remove the try/except above, Python prints a Traceback")
print("and STOPS the program immediately at the error line.")
print()
print("=== WITH handling — program continues ===")
print("try/except catches the error gracefully and lets the program keep running.")

# Think:
# 1. What type of exception would you get if you do: [1, 2, 3]["a"]?
# 2. Name two situations in real apps where exceptions are likely to occur.
