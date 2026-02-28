# Program Code: STR-LR-01
# Title: Trace the String — Follow the Code Step by Step!
# Cognitive Skill: Logical Reasoning (Tracing values)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav has a mystery box — he puts a string in and
# applies several operations. Can YOU predict what comes out
# at each step before running the code?
# Think step-by-step. Then check your answer!
# ============================================================

import time

print("=" * 55)
print("       TRACE THE STRING — DETECTIVE MODE!")
print("=" * 55)

print("""
RULES:
  Look at each code block.
  PREDICT what the output will be.
  Then press ENTER to reveal the answer!
""")

score = 0
total = 5

# -------------------------------------------------------
# ROUND 1
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 1:")
print("-" * 40)
print("""
print("cricket".upper())

What will the output be?
""")
input("Your prediction → press ENTER to see answer: ")
result = "cricket".upper()
print("\n✅ Answer: '" + result + "'")
guess = input("Did you get it right? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# ROUND 2
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 2:")
print("-" * 40)
print("""
print("Aarav Sharma"[0] + "Aarav Sharma"[6])

What will the output be?
""")
input("Your prediction → press ENTER to see answer: ")
result = "Aarav Sharma"[0] + "Aarav Sharma"[6]
print("\n✅ Answer: '" + result + "'")
guess = input("Did you get it right? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# ROUND 3
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 3:")
print("-" * 40)
print("""
print("Chennai"[2:5])

What will the output be?
""")
input("Your prediction → press ENTER to see answer: ")
result = "Chennai"[2:5]
print("\n✅ Answer: '" + result + "'")
guess = input("Did you get it right? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# ROUND 4
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 4:")
print("-" * 40)
print("""
print("I love Python!".replace("Python", "Cricket"))

What will the output be?
""")
input("Your prediction → press ENTER to see answer: ")
result = "I love Python!".replace("Python", "Cricket")
print("\n✅ Answer: '" + result + "'")
guess = input("Did you get it right? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# ROUND 5
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 5 (TRICKY!):")
print("-" * 40)
print("""
print("PYTHON"[::-1])

What will the output be?
""")
input("Your prediction → press ENTER to see answer: ")
result = "PYTHON"[::-1]
print("\n✅ Answer: '" + result + "'")
guess = input("Did you get it right? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# FINAL SCORE
# -------------------------------------------------------
print("\n" + "=" * 55)
print("  YOUR SCORE :", score, "/", total)
if score == total:
    print("  🏆 PERFECT! You are a String Detective!")
elif score >= 3:
    print("  ✅ Great work! Keep practising.")
else:
    print("  💪 Keep going — tracing takes practice!")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. What did "PYTHON"[::-1] do? Can you explain it?
# 2. Which round was hardest? Why?
# 3. Write your own "trace this" challenge for a friend!
# ============================================================
