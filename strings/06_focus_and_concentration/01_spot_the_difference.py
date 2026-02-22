# Program Code: STR-FC-01
# Title: Spot the Difference — Find the Tiny String Changes!
# Cognitive Skill: Focus and Concentration (Attention to detail)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Two strings LOOK almost the same — but they're slightly different.
# Can you spot the difference WITHOUT running the code?
# This trains your eye to see small but important details in code!
# ============================================================

import time

print("=" * 55)
print("   SPOT THE DIFFERENCE — STRING EDITION!")
print("=" * 55)

print("""
In each round, two strings are shown.
SPOT the difference before pressing ENTER!
""")

score = 0
total = 5

# -------------------------------------------------------
# ROUND 1: Case difference
# -------------------------------------------------------
print("=" * 40)
print("ROUND 1: What is different?")
print("-" * 40)
print('  String A: "Aarav Sharma"')
print('  String B: "Aarav sharma"')
print()
input("Found it? Press ENTER: ")
print("""
  🔍 DIFFERENCE: The 'S' in 'Sharma'
     String A: Sharma (capital S) ← Proper Case
     String B: sharma (small s)   ← Not properly formatted
  💡 This matters in comparisons! A == B → False
""")
a = "Aarav Sharma"
b = "Aarav sharma"
print(f"  'Aarav Sharma' == 'Aarav sharma' → {a == b}")
guess = input("Did you spot it? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# ROUND 2: Extra space
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 2: What is different?")
print("-" * 40)
print('  String A: "Python"')
print('  String B: "Python "')
print()
input("Found it? Press ENTER: ")
print("""
  🔍 DIFFERENCE: An invisible SPACE at the end of String B!
     "Python"  → length 6
     "Python " → length 7
  💡 This is why we always use .strip() before comparing!
""")
x = "Python"
y = "Python "
print(f"  len('Python')   = {len(x)}")
print(f"  len('Python ')  = {len(y)}")
print(f"  'Python' == 'Python ' → {x == y}")
guess = input("Did you spot it? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# ROUND 3: Letter swap
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 3: What is different?")
print("-" * 40)
print('  String A: "Chennai"')
print('  String B: "Channai"')
print()
input("Found it? Press ENTER: ")
print("""
  🔍 DIFFERENCE: 'e' and 'a' are SWAPPED!
     Chennai → C-h-e-n-n-a-i
     Channai → C-h-a-n-n-a-i
  💡 Spelling matters! 'Chennai' find('e') → 2
                       'Channai' find('e') → -1 (not found!)
""")
guess = input("Did you spot it? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# ROUND 4: Quote type
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 4: What is different?")
print("-" * 40)
print("  String A: name = 'Aarav'")
print('  String B: name = "Aarav"')
print()
input("Found it? Press ENTER: ")
print("""
  🔍 DIFFERENCE: Single quotes vs Double quotes
     But guess what — in Python, BOTH create the SAME string!
     'Aarav' == "Aarav" → True
  💡 Key difference: use double quotes when string has apostrophe
     e.g., "I don't know" (can't use single quotes here)
""")
a = 'Aarav'
b = "Aarav"
print(f"  'Aarav' == \"Aarav\" → {a == b}")
guess = input("Did you spot it? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# ROUND 5: Index off by one
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 5 (TRICKY!): What is different?")
print("-" * 40)
print('  Code A: word = "Python"')
print('           print(word[0:3])')
print()
print('  Code B: word = "Python"')
print('           print(word[1:3])')
print()
input("Found it? Press ENTER: ")
word = "Python"
print(f"""
  🔍 DIFFERENCE: Starting index — 0 vs 1
     word[0:3] = '{word[0:3]}'   (includes index 0: 'P')
     word[1:3] = '{word[1:3]}'   (starts from index 1: 'y')
  💡 Off-by-one errors are the most common bugs in slicing!
""")
guess = input("Did you spot it? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# FINAL SCORE
# -------------------------------------------------------
print("\n" + "=" * 55)
print(f"  SPOT THE DIFFERENCE SCORE : {score} / {total}")
if score == total:
    print("  🏆 Eagle Eye! Nothing escapes your attention!")
elif score >= 3:
    print("  ✅ Sharp focus! Keep training your attention to detail.")
else:
    print("  👁️  Focus harder — small differences make big bugs!")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. Which round was hardest to spot? Why?
# 2. Why are invisible characters (like spaces) dangerous?
# 3. Can you create your own "spot the difference" challenge?
# ============================================================
