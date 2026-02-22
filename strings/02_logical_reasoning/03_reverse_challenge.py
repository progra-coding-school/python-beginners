# Program Code: STR-LR-03
# Title: Reverse Challenge — Work Backwards from the Output!
# Cognitive Skill: Logical Reasoning (Reverse reasoning)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav gives you the OUTPUT and asks: "What was the INPUT?"
# You need to work BACKWARDS to figure out the original string.
# This is called REVERSE REASONING — a key thinking skill!
# ============================================================

import time

print("=" * 55)
print("    REVERSE CHALLENGE — WORK BACKWARDS!")
print("=" * 55)

print("""
In each round, you'll see:
  - The OPERATION applied to a string
  - The OUTPUT (result)
  - You must figure out the ORIGINAL string!
""")

score = 0
total = 4

# -------------------------------------------------------
# ROUND 1: Reversing upper()
# -------------------------------------------------------
print("=" * 40)
print("ROUND 1:")
print("-" * 40)
print("""
An unknown string had .upper() applied to it.
The result is: 'CHENNAI'

What could the original string have been?
(Multiple answers possible!)
""")

answer = input("Your answer: ")
print(f"\nPossible answers: 'chennai', 'Chennai', 'CHENNAI', 'cHENNAI' ...")
print("The key: upper() converts ALL letters to capitals.")
word = "CHENNAI"
print(f"Verify: 'chennai'.upper() = '{('chennai').upper()}'")
guess = input("Did you reason it correctly? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# ROUND 2: Reversing strip()
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 2:")
print("-" * 40)
print("""
An unknown string had .strip() applied to it.
The result is: 'Aarav'

What could the original string have been?
(Name at least 2 possibilities)
""")

answer = input("Your answer: ")
print("\nPossible answers: '  Aarav', 'Aarav  ', '  Aarav  ', 'Aarav'")
print("strip() removes leading and trailing spaces only.")
guess = input("Did you reason it correctly? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# ROUND 3: Reversing replace()
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 3:")
print("-" * 40)
print("""
result = original.replace("Cricket", "Python")
result = "I love Python and Python is fun!"

What was the original string?
""")

answer = input("Your answer: ")
print("\nAnswer: 'I love Cricket and Cricket is fun!'")
print("replace() swapped every 'Python' back to 'Cricket'")
guess = input("Did you reason it correctly? (y/n): ")
if guess.lower() == "y":
    score += 1
time.sleep(1)

# -------------------------------------------------------
# ROUND 4: Reversing a slice
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 4 (TRICKY!):")
print("-" * 40)
print("""
word = original
result = word[2:5]
result = 'YTH'

The original string has at least 5 characters.
Positions 2, 3, 4 are Y, T, H.

What is a possible original string?
""")

answer = input("Your answer: ")
print("\nAnswer: 'PYTHON' works! word[2:5] = 'THO'... wait let's verify:")
check = "PYTHON"
print(f"  'PYTHON'[2:5] = '{check[2:5]}'")
print(f"  Hmm! That's 'THO', not 'YTH'.")
print(f"  Let's try: 'XYTHON'[2:5] = '{('XYTHON')[2:5]}'... ")
print(f"  'MYTH1S'[0:3] = '{('MYTH1S')[0:3]}'...")
print(f"  Answer: any string where positions 2,3,4 are Y,T,H")
print(f"  Example: '??YTH????' — like 'XXYTH' → [2:5] = 'YTH'")
example = "XXYTH"
print(f"  Verify: 'XXYTH'[2:5] = '{example[2:5]}'  ✅")
guess = input("Did you reason it correctly? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# FINAL SCORE
# -------------------------------------------------------
print("\n" + "=" * 55)
print(f"  REVERSE CHALLENGE SCORE : {score} / {total}")
if score == total:
    print("  🏆 Excellent reverse thinking skills!")
elif score >= 2:
    print("  ✅ Good work! Reverse thinking is tough — keep going!")
else:
    print("  💪 This takes practice — reverse thinking is a power skill!")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. Why can multiple original strings produce the same upper() output?
# 2. What would you get if you reversed [::-1] on 'NOHTYP'?
# 3. Create your own reverse challenge for a classmate!
# ============================================================
