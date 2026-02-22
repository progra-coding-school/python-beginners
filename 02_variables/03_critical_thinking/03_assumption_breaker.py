# Program Code: VAR-CT-03
# Title: Assumption Breaker
# Cognitive Skill: Critical Thinking (Testing assumptions)
# Topic: Variables in Python

score = 0

# Myth 1
print("--- Myth 1 ---")
print("'If b = a, then changing a later will also change b'")
guess = input("True or False? (T/F) ").upper()
a = 10
b = a
a = 99
print("a = 10, b = a, then a = 99")
print("b is now:", b)
print("Answer: FALSE. b got the value 10, not a link to a.")
if guess == "F":
    score = score + 1
    print("Correct!")
input("Press Enter for Myth 2...")

# Myth 2
print("--- Myth 2 ---")
print("'Age and age are the same variable'")
guess = input("True or False? (T/F) ").upper()
Age = 25
age = 10
print("Age =", Age, "  age =", age)
print("Answer: FALSE. Python is case-sensitive.")
if guess == "F":
    score = score + 1
    print("Correct!")
input("Press Enter for Myth 3...")

# Myth 3
print("--- Myth 3 ---")
print("'price + 50 changes price to price + 50'")
guess = input("True or False? (T/F) ").upper()
price = 100
price + 50            # calculates but does NOT store
print("After price + 50, price is still:", price)
price = price + 50    # this stores it
print("After price = price + 50, price is:", price)
print("Answer: FALSE. You must assign the result back.")
if guess == "F":
    score = score + 1
    print("Correct!")
input("Press Enter for Myth 4...")

# Myth 4
print("--- Myth 4 ---")
print("'A variable can hold text, then a number, then a decimal'")
guess = input("True or False? (T/F) ").upper()
my_var = "Hello"
print(type(my_var))
my_var = 42
print(type(my_var))
my_var = 3.14
print(type(my_var))
print("Answer: TRUE. Python allows this — called dynamic typing.")
if guess == "T":
    score = score + 1
    print("Correct!")
input("Press Enter for Myth 5...")

# Myth 5
print("--- Myth 5 ---")
print("'input() gives a number when the user types a number'")
guess = input("True or False? (T/F) ").upper()
print("input() ALWAYS gives a string — even if the user types 42.")
print("Use int() or float() to convert it.")
print("Answer: FALSE.")
if guess == "F":
    score = score + 1
    print("Correct!")

print("Score:", score, "/ 5")
