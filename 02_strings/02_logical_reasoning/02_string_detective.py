# Program Code: STR-LR-02
# Title: String Detective — Find the Hidden Pattern!
# Cognitive Skill: Logical Reasoning (Pattern recognition)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Diya has hidden secret messages inside strings.
# Use your string skills to decode the patterns and
# figure out what the output will be — without running the code first!
# ============================================================

import time

print("=" * 55)
print("    STRING DETECTIVE — DECODE THE PATTERN!")
print("=" * 55)

score = 0
total = 5

# -------------------------------------------------------
# CLUE 1: Length and Indexing
# -------------------------------------------------------
print("\n" + "=" * 40)
print("🔍 CLUE 1: What is the output?")
print("-" * 40)
print("""
print(len("PROGRA"))
print("PROGRA"[-1])
""")
input("Your answers (length, last char) → press ENTER: ")
print("  len =", len("PROGRA"))
print("  'PROGRA'[-1] = '" + "PROGRA"[-1] + "'")
guess = input("Correct? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# CLUE 2: Chain of Methods
# -------------------------------------------------------
print("\n" + "=" * 40)
print("🔍 CLUE 2: What is the final output?")
print("-" * 40)
print("""
print("  hello world  ".strip().title())
""")
input("Your answer → press ENTER: ")
result = "  hello world  ".strip().title()
print("  Answer: '" + result + "'")
guess = input("Correct? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# CLUE 3: Counting
# -------------------------------------------------------
print("\n" + "=" * 40)
print("🔍 CLUE 3: How many 'a's in the sentence?")
print("-" * 40)
print("""
print("Aarav and Amma ate amazing aloo.".count("a"))
""")
input("Your answer → press ENTER: ")
count = "Aarav and Amma ate amazing aloo.".count("a")
print("  Answer:", count)
print("  (Note: 'A' and 'a' are different — case-sensitive!)")
guess = input("Correct? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# CLUE 4: Membership
# -------------------------------------------------------
print("\n" + "=" * 40)
print("🔍 CLUE 4: True or False?")
print("-" * 40)
print("""
print("diya" in "Aarav, Diya, Mani, Priya")
print("Mani" in "Aarav, Diya, Mani, Priya")
""")
input("Your answers (True/False, True/False) → press ENTER: ")
team = "Aarav, Diya, Mani, Priya"
print("  'diya' in team  →", "diya" in team)
print("  'Mani' in team  →", "Mani" in team)
guess = input("Both correct? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# CLUE 5: Slice Pattern
# -------------------------------------------------------
print("\n" + "=" * 40)
print("🔍 CLUE 5 (CHALLENGE): Decode the slice!")
print("-" * 40)
print("""
print("STR-2026-AARAV"[4:8])
print("STR-2026-AARAV"[-5:])
""")
input("Your answers → press ENTER: ")
code = "STR-2026-AARAV"
print("  code[4:8]  = '" + code[4:8] + "'")
print("  code[-5:]  = '" + code[-5:] + "'")
guess = input("Both correct? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# FINAL SCORE
# -------------------------------------------------------
print("\n" + "=" * 55)
print("  DETECTIVE SCORE :", score, "/", total)
if score == total:
    print("  🏆 MASTER DETECTIVE — Outstanding!")
elif score >= 3:
    print("  ✅ Good detective skills! Keep sharpening.")
else:
    print("  🔍 Keep investigating — you'll crack it!")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. Why did 'diya' (lowercase) return False in Clue 4?
# 2. What pattern did you use to solve the slice in Clue 5?
# 3. Create your own string detective clue for a classmate!
# ============================================================
