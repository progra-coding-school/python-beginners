# Program Code: DT-LR-03
# Title: Type Detective
# Cognitive Skill: Logical Reasoning (Working from clues)
# Topic: Data Types in Python

score = 0

print("You will see an OUTPUT. Deduce the data TYPE that was used.")

# Clue 1
print("\n--- Clue 1 ---")
print("Output: 15.0")
guess = input("What type produced this? (int / float / str) ")
print("Answer: float")
if guess.lower() == "float":
    print("Correct! The .0 tells you it's a float.")
    score += 1
else:
    print("The decimal point .0 means float, even though the value is whole.")

# Clue 2
print("\n--- Clue 2 ---")
print("Output: True")
guess = input("What type produced this? (int / float / str / bool) ")
print("Answer: bool")
if guess.lower() == "bool":
    print("Correct!")
    score += 1
else:
    print("True and False are boolean values.")

# Clue 3
print("\n--- Clue 3 ---")
print("Code: result = a + b")
print("Output of result: 510")
print("What type are a and b?")
guess = input("Type? (int / float / str) ")
print("Answer: str")
if guess.lower() == "str":
    print("Correct! Adding two strings joins them: '5' + '10' = '510'")
    score += 1
else:
    print("If a=5, b=10 (int), result would be 15. But 510 means strings joined.")

# Clue 4
print("\n--- Clue 4 ---")
print("Code: x = 7 / 2")
print("What will type(x) show?")
guess = input("Type? (int / float / str / bool) ")
print("Answer: float")
if guess.lower() == "float":
    print("Correct! Division / ALWAYS gives float in Python 3.")
    score += 1
else:
    print("In Python 3, / always gives a float. 7/2 = 3.5, not 3.")

# Clue 5 — Challenge
print("\n--- Clue 5 (Challenge) ---")
print("Code: z = int(float(user_input))")
print("What was user_input if z = 3?")
guess = input("Give a possible value for user_input: ")
print("Possible: '3.9', '3.1', '3.5' — any string of a decimal between 3 and 4")
print("float('3.9') = 3.9, then int(3.9) = 3 (truncates).")
score += 1

print(f"\nScore: {score} / 5")
