# Program Code: STR-LR-01
# Title: Trace the String — Follow the Code Step by Step!
# Cognitive Skill: Logical Reasoning (Tracing values)
# Topic: Strings in Python

# PROBLEM STATEMENT:
# Aarav has a mystery box — he puts a string in and
# applies several operations. Can YOU predict what comes out
# at each step before running the code?
# Think step-by-step. Then check your answer!

import time

print("TRACE THE STRING — DETECTIVE MODE!")
print()
print("RULES:")
print("  Look at each code block.")
print("  PREDICT what the output will be.")
print("  Then press ENTER to reveal the answer!")

score = 0
total = 5

# ROUND 1
print("\nROUND 1:")
print("""
print("cricket".upper())

What will the output be?
""")
input("Your prediction → press ENTER to see answer: ")
result = "cricket".upper()
print("\nAnswer: '" + result + "'")
guess = input("Did you get it right? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# ROUND 2
print("\nROUND 2:")
print("""
print("Aarav Sharma"[0] + "Aarav Sharma"[6])

What will the output be?
""")
input("Your prediction → press ENTER to see answer: ")
result = "Aarav Sharma"[0] + "Aarav Sharma"[6]
print("\nAnswer: '" + result + "'")
guess = input("Did you get it right? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# ROUND 3
print("\nROUND 3:")
print("""
print("Chennai"[2:5])

What will the output be?
""")
input("Your prediction → press ENTER to see answer: ")
result = "Chennai"[2:5]
print("\nAnswer: '" + result + "'")
guess = input("Did you get it right? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# ROUND 4
print("\nROUND 4:")
print("""
print("I love Python!".replace("Python", "Cricket"))

What will the output be?
""")
input("Your prediction → press ENTER to see answer: ")
result = "I love Python!".replace("Python", "Cricket")
print("\nAnswer: '" + result + "'")
guess = input("Did you get it right? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# ROUND 5
print("\nROUND 5 (TRICKY!):")
print("""
print("PYTHON"[::-1])

What will the output be?
""")
input("Your prediction → press ENTER to see answer: ")
result = "PYTHON"[::-1]
print("\nAnswer: '" + result + "'")
guess = input("Did you get it right? (y/n): ")
if guess.lower() == "y":
    score += 1

# FINAL SCORE
print()
print("YOUR SCORE :", score, "/", total)
if score == total:
    print("PERFECT! You are a String Detective!")
elif score >= 3:
    print("Great work! Keep practising.")
else:
    print("Keep going — tracing takes practice!")

# REFLECTION:
# 1. What did "PYTHON"[::-1] do? Can you explain it?
# 2. Which round was hardest? Why?
# 3. Write your own "trace this" challenge for a friend!
