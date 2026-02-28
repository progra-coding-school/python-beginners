# Program Code: STR-CT-03
# Title: Assumption Breaker — Test What You Think You Know!
# Cognitive Skill: Critical Thinking (Challenging assumptions)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Mani thinks he knows everything about strings.
# But Python is full of SURPRISES!
# In this program, we test common assumptions students make
# about strings — and see which ones are WRONG.
# ============================================================

print("=" * 55)
print("  ASSUMPTION BREAKER — TRUE OR FALSE ABOUT STRINGS!")
print("=" * 55)

print("""
For each statement, decide: TRUE or FALSE?
Then press ENTER to see the real answer.
""")

score = 0
total = 6

# -------------------------------------------------------
# ASSUMPTION 1
# -------------------------------------------------------
print("=" * 40)
print("STATEMENT 1:")
print('  "5" + "3" = 8')
print()
input("True or False? Press ENTER: ")
result = "5" + "3"
print('  ❌ FALSE! "5" + "3" = "' + result + '"')
print('  These are STRINGS, not numbers. + means JOIN, not add.')
print('  To add: int("5") + int("3") = 8')
guess = input("Did you say FALSE? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# ASSUMPTION 2
# -------------------------------------------------------
print("\n" + "=" * 40)
print("STATEMENT 2:")
print('  len("Hello World") = 10')
print()
input("True or False? Press ENTER: ")
text   = "Hello World"
length = len(text)
print('  ❌ FALSE! len("Hello World") =', length)
print("  The SPACE between Hello and World is also a character!")
guess = input("Did you say FALSE? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# ASSUMPTION 3
# -------------------------------------------------------
print("\n" + "=" * 40)
print("STATEMENT 3:")
print('  "aarav" == "Aarav" is True')
print()
input("True or False? Press ENTER: ")
result = "aarav" == "Aarav"
print('  ❌ FALSE! "aarav" == "Aarav" →', result)
print("  Python is case-sensitive. 'a' ≠ 'A'.")
guess = input("Did you say FALSE? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# ASSUMPTION 4
# -------------------------------------------------------
print("\n" + "=" * 40)
print("STATEMENT 4:")
print('  "Aarav"[0] = "D"   → changes the string to "Darav"')
print()
input("True or False? Press ENTER: ")
print('  ❌ FALSE! Strings are IMMUTABLE.')
print("  You cannot change individual characters of a string.")
print('  "Aarav"[0] = \'D\' will cause a TypeError!')
try:
    "Aarav"[0] = "D"
except TypeError as e:
    print("  Error proof:", e)
guess = input("Did you say FALSE? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# ASSUMPTION 5
# -------------------------------------------------------
print("\n" + "=" * 40)
print("STATEMENT 5:")
print('  "ha" * 3 = "hahaha"')
print()
input("True or False? Press ENTER: ")
result = "ha" * 3
print('  ✅ TRUE! "ha" * 3 = "' + result + '"')
print("  String repetition works exactly like this!")
guess = input("Did you say TRUE? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# ASSUMPTION 6
# -------------------------------------------------------
print("\n" + "=" * 40)
print("STATEMENT 6:")
print('  "Python"[-1] = "P"   (last character is P)')
print()
input("True or False? Press ENTER: ")
result = "Python"[-1]
print('  ❌ FALSE! "Python"[-1] = "' + result + '"')
print("  -1 means the LAST character, which is 'n', not 'P'.")
print("  'P' is at index 0. 'n' is at index 5 (or -1).")
guess = input("Did you say FALSE? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# FINAL SCORE
# -------------------------------------------------------
print("\n" + "=" * 55)
print("  ASSUMPTION BREAKER SCORE :", score, "/", total)
if score == total:
    print("  🏆 You broke all assumptions — Critical Thinker!")
elif score >= 4:
    print("  ✅ Great instincts! Keep questioning assumptions.")
else:
    print("  💡 Surprising, right? That's why we test our assumptions!")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. Which assumption surprised you the most? Why?
# 2. Why does Python treat "5" + "3" differently from 5 + 3?
# 3. What's the difference between a string "5" and integer 5?
# ============================================================
