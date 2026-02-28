# Program Code: STR-FC-02
# Title: Mental String Tracking — Track the Changes in Your Head!
# Cognitive Skill: Focus and Concentration (Mental tracking)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# A string goes through MULTIPLE changes one step at a time.
# Can you TRACK the value of the string mentally after each step?
# Don't run the code until you've predicted every output!
# ============================================================

import time

print("=" * 55)
print("  MENTAL STRING TRACKING — FOLLOW EVERY STEP!")
print("=" * 55)

print("""
You'll see a series of string operations applied step by step.
PREDICT the value of the string after each step.
Then reveal the answer.
""")

# -------------------------------------------------------
# CHALLENGE 1: Chain of transformations
# -------------------------------------------------------
print("=" * 40)
print("CHALLENGE 1: Follow the string through 4 steps")
print("-" * 40)

text = "  hello world  "
print('  Start: "' + text + '"')
print()

print('  Step 1: Apply .strip()')
input("  What is the string now? Press ENTER to reveal: ")
text = text.strip()
print('  → "' + text + '"')
time.sleep(0.5)

print('\n  Step 2: Apply .upper()')
input("  What is the string now? Press ENTER to reveal: ")
text = text.upper()
print('  → "' + text + '"')
time.sleep(0.5)

print("\n  Step 3: Apply .replace('WORLD', 'INDIA')")
input("  What is the string now? Press ENTER to reveal: ")
text = text.replace("WORLD", "INDIA")
print('  → "' + text + '"')
time.sleep(0.5)

print('  Step 4: Add "!" to the end')
input("  What is the string now? Press ENTER to reveal: ")
text = text + "!"
print('  → "' + text + '"')

print('\n  FINAL VALUE: "' + text + '"')
print()
guess = input("Did you track all 4 steps correctly? (y/n): ")
step1_score = 1 if guess.lower() == "y" else 0

# -------------------------------------------------------
# CHALLENGE 2: Slicing and indexing
# -------------------------------------------------------
print("\n" + "=" * 40)
print("CHALLENGE 2: Slicing operations")
print("-" * 40)

word = "CRICKET"
print('  word = "' + word + '"')
print()

operations = [
    ("word[0]",    word[0],    "First character"),
    ("word[-1]",   word[-1],   "Last character"),
    ("word[2:5]",  word[2:5],  "Slice from index 2 to 4"),
    ("word[:3]",   word[:3],   "First 3 characters"),
    ("word[::-1]", word[::-1], "Reversed"),
]

score2 = 0
for op, result, hint in operations:
    print("  Operation: " + op + "   ← (" + hint + ")")
    input("  Your prediction? Press ENTER to reveal: ")
    print('  → "' + result + '"')
    correct = input("  Correct? (y/n): ")
    if correct.lower() == "y":
        score2 += 1
    time.sleep(0.5)
    print()

# -------------------------------------------------------
# CHALLENGE 3: Method chain — predict the FINAL output only
# -------------------------------------------------------
print("=" * 40)
print("CHALLENGE 3: FULL METHOD CHAIN (hardest!)")
print("-" * 40)
raw = "  progra kids  "
print('  Start: "' + raw + '"')
print()
print('  Apply: .strip() → then .title() → then .replace("Kids", "Coders") → then + " School"')
print()
input("  What is result? Predict mentally then press ENTER: ")
result = raw.strip().title().replace("Kids", "Coders") + " School"
print('  → "' + result + '"')
correct = input("  Correct? (y/n): ")
step3_score = 1 if correct.lower() == "y" else 0

# -------------------------------------------------------
# FINAL SCORE
# -------------------------------------------------------
total_score = step1_score + (1 if score2 >= 4 else 0) + step3_score
print("\n" + "=" * 55)
print("  MENTAL TRACKING SCORE :", total_score, "/ 3")
print("  (Slicing sub-score    :", score2, "/", len(operations), ")")
if total_score == 3:
    print("  🏆 Mental tracking master — incredible focus!")
elif total_score >= 2:
    print("  ✅ Strong mental tracking! Keep sharpening.")
else:
    print("  🧠 Keep practising — mental tracking is a powerful skill!")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. Which step was hardest to track mentally? Why?
# 2. How does practising mental tracking help your coding?
# 3. Try creating your own 4-step transformation challenge!
# ============================================================
