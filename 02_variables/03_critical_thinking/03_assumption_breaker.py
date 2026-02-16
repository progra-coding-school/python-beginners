# Program Code: CS-CT-03
# Title: Assumption Breaker - Variable Myths!
# Cognitive Skill: Critical Thinking (Questioning assumptions)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# When we learn something new, we carry ASSUMPTIONS -
# things we THINK are true but haven't tested.
# Good thinkers QUESTION their assumptions!
# Let's test common beliefs about Python variables.
# Guess True or False, then see the REAL answer!
# ============================================================

score = 0

print("=== Assumption Breaker: Variable Myths! ===")
print("Test your beliefs about Python variables.")
print("Type 'T' for True or 'F' for False.")
print()

# ----- MYTH 1 -----
print("--- Myth 1 ---")
print('"If I do b = a, then changing a later will also change b"')
print()
guess = input("True or False? (T/F): ").upper()
print()

# Let's test it!
print("Let's test it with REAL code:")
a = 10
b = a
print(f"  a = 10")
print(f"  b = a      --> b is now {b}")
a = 99
print(f"  a = 99     --> a changed to {a}")
print(f"  What is b? --> b is still {b}!")
print()
print("ANSWER: FALSE!")
print("When you write b = a, b gets the VALUE (10), not a link to a.")
print("Changing a later has NO effect on b.")
if guess == "F":
    score = score + 1
    print("You got it right!")
print()
input("Press Enter for Myth 2...")
print()

# ----- MYTH 2 -----
print("--- Myth 2 ---")
print('"Age and age are the SAME variable"')
print()
guess = input("True or False? (T/F): ").upper()
print()

print("Let's test it:")
Age = 25
age = 10
print(f"  Age = {Age}")
print(f"  age = {age}")
print(f"  Are they the same? NO! Age={Age}, age={age}")
print()
print("ANSWER: FALSE!")
print("Python is CASE-SENSITIVE. 'Age', 'age', and 'AGE'")
print("are THREE different variables!")
if guess == "F":
    score = score + 1
    print("You got it right!")
print()
input("Press Enter for Myth 3...")
print()

# ----- MYTH 3 -----
print("--- Myth 3 ---")
print('"If price = 100, then price + 50 changes price to 150"')
print()
guess = input("True or False? (T/F): ").upper()
print()

print("Let's test it:")
price = 100
print(f"  price = {price}")
price + 50
print(f"  price + 50  (just calculated, not stored)")
print(f"  price is still: {price}")
print()
price = price + 50
print(f"  price = price + 50  (NOW it is stored!)")
print(f"  price is now: {price}")
print()
print("ANSWER: FALSE!")
print("'price + 50' only CALCULATES, it does not STORE.")
print("You need 'price = price + 50' to actually UPDATE the variable!")
if guess == "F":
    score = score + 1
    print("You got it right!")
print()
input("Press Enter for Myth 4...")
print()

# ----- MYTH 4 -----
print("--- Myth 4 ---")
print('"You can store different types (text, numbers) in the same variable"')
print()
guess = input("True or False? (T/F): ").upper()
print()

print("Let's test it:")
my_var = "Hello"
print(f"  my_var = 'Hello'  --> type: text (string)")
my_var = 42
print(f"  my_var = 42       --> type: number (integer)")
my_var = 3.14
print(f"  my_var = 3.14     --> type: decimal (float)")
print(f"  It works! Python allows it!")
print()
print("ANSWER: TRUE!")
print("Python lets you change a variable's type. This is called")
print("'dynamic typing'. Not all languages allow this!")
if guess == "T":
    score = score + 1
    print("You got it right!")
print()
input("Press Enter for Myth 5...")
print()

# ----- MYTH 5 -----
print("--- Myth 5 ---")
print('"input() gives a number when the user types a number"')
print()
guess = input("True or False? (T/F): ").upper()
print()

print("Let's test it:")
print('  Imagine the user types 42 when asked:')
print('  age = input("Enter age: ")')
print('  The variable age will store "42" (a STRING, not a number!)')
print()
print("ANSWER: FALSE!")
print("input() ALWAYS gives a string, even if the user types numbers!")
print("You must use int() or float() to convert it.")
print('  age = int(input("Enter age: "))  # NOW it is a number')
if guess == "F":
    score = score + 1
    print("You got it right!")
print()

# Final Score
print("=" * 45)
print(f"YOUR SCORE: {score} / 5")
print()
if score == 5:
    print("Perfect! You question everything like a true thinker!")
elif score >= 3:
    print("Good job! You challenged most of your assumptions!")
else:
    print("Now you know the truth! Assumptions can trick us.")
    print("Always TEST what you believe!")
print("=" * 45)

# ============================================================
# REFLECTION PROMPTS:
# 1. Which myth surprised you the most? Why did you believe
#    the wrong thing?
# 2. Why is it important to TEST your assumptions instead of
#    just believing them?
# 3. Can you think of an assumption you had about something
#    in real life that turned out to be wrong?
#    (Example: "Heavy things fall faster than light things")
# ============================================================
