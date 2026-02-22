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
word = "PROGRA"
print(len(word))
print(word[-1])
""")
input("Your answers (length, last char) → press ENTER: ")
word = "PROGRA"
print(f"  len = {len(word)}")
print(f"  word[-1] = '{word[-1]}'")
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
text = "  hello world  "
result = text.strip().title()
print(result)
""")
input("Your answer → press ENTER: ")
text   = "  hello world  "
result = text.strip().title()
print(f"  Answer: '{result}'")
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
sentence = "Aarav and Amma ate amazing aloo."
count = sentence.count("a")
print(count)
""")
input("Your answer → press ENTER: ")
sentence = "Aarav and Amma ate amazing aloo."
count    = sentence.count("a")
print(f"  Answer: {count}")
print(f"  (Note: 'A' and 'a' are different — case-sensitive!)")
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
team = "Aarav, Diya, Mani, Priya"
print("diya" in team)
print("Mani" in team)
""")
input("Your answers (True/False, True/False) → press ENTER: ")
team = "Aarav, Diya, Mani, Priya"
print(f"  'diya' in team  → {('diya' in team)}")
print(f"  'Mani' in team  → {('Mani' in team)}")
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
code = "STR-2026-AARAV"
print(code[4:8])
print(code[-5:])
""")
input("Your answers → press ENTER: ")
code = "STR-2026-AARAV"
print(f"  code[4:8]  = '{code[4:8]}'")
print(f"  code[-5:]  = '{code[-5:]}'")
guess = input("Both correct? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# FINAL SCORE
# -------------------------------------------------------
print("\n" + "=" * 55)
print(f"  DETECTIVE SCORE : {score} / {total}")
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
