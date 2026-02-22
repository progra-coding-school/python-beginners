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
word = "cricket"
result = word.upper()
print(result)

What will result be?
""")
input("Your prediction → press ENTER to see answer: ")
word   = "cricket"
result = word.upper()
print(f"\n✅ Answer: '{result}'")
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
name = "Aarav Sharma"
result = name[0] + name[6]
print(result)

What will result be?
""")
input("Your prediction → press ENTER to see answer: ")
name   = "Aarav Sharma"
result = name[0] + name[6]
print(f"\n✅ Answer: '{result}'")
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
city = "Chennai"
result = city[2:5]
print(result)

What will result be?
""")
input("Your prediction → press ENTER to see answer: ")
city   = "Chennai"
result = city[2:5]
print(f"\n✅ Answer: '{result}'")
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
text = "I love Python!"
result = text.replace("Python", "Cricket")
print(result)

What will result be?
""")
input("Your prediction → press ENTER to see answer: ")
text   = "I love Python!"
result = text.replace("Python", "Cricket")
print(f"\n✅ Answer: '{result}'")
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
word = "PYTHON"
result = word[::-1]
print(result)

What will result be?
""")
input("Your prediction → press ENTER to see answer: ")
word   = "PYTHON"
result = word[::-1]
print(f"\n✅ Answer: '{result}'")
guess = input("Did you get it right? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# FINAL SCORE
# -------------------------------------------------------
print("\n" + "=" * 55)
print(f"  YOUR SCORE : {score} / {total}")
if score == total:
    print("  🏆 PERFECT! You are a String Detective!")
elif score >= 3:
    print("  ✅ Great work! Keep practising.")
else:
    print("  💪 Keep going — tracing takes practice!")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. What did word[::-1] do? Can you explain it?
# 2. Which round was hardest? Why?
# 3. Write your own "trace this" challenge for a friend!
# ============================================================
