# Program Code: CS-FC-03
# Title: Variable Memory Palace
# Cognitive Skill: Focus & Concentration (Observation and short-term memory)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Programmers must hold MANY variable values in their head
# while reading code. Let's train that skill!
# You will SEE some variable assignments for a few seconds.
# Then the screen CLEARS and you must answer questions
# from MEMORY! How many can you remember?
# ============================================================

# ------------------------------------------------------------
# INSTRUCTIONS:
# 1. Variable assignments will be shown on screen
# 2. MEMORIZE them! You have a few seconds.
# 3. The screen will "clear" (scroll away)
# 4. Answer the questions from memory
# 5. NO scrolling back up! Trust your brain!
# ------------------------------------------------------------

import time

total_score = 0

print("=== Variable Memory Palace ===")
print("Memorize the variables. Answer from memory!")
print()

# ----- ROUND 1: 5 variables -----
print("--- Round 1: Memorize 5 Variables ---")
print("You have 12 seconds. MEMORIZE these!")
print()
print("  name = 'Diya'")
print("  age = 9")
print("  city = 'Chennai'")
print("  sport = 'Badminton'")
print("  color = 'Green'")
print()

# Countdown
for i in range(12, 0, -1):
    print(f"  Time remaining: {i} seconds...", end="\r")
    time.sleep(1)

# Clear screen by printing blank lines
print("\n" * 30)
print("=" * 40)
print("  SCREEN CLEARED! Answer from memory!")
print("=" * 40)
print()

# Quiz
r1_score = 0
ans = input("  What was the value of 'city'?   : ")
if ans.lower().strip() == "chennai":
    print("  Correct!")
    r1_score = r1_score + 1
else:
    print("  It was 'Chennai'")

ans = input("  What was the value of 'age'?    : ")
if ans.strip() == "9":
    print("  Correct!")
    r1_score = r1_score + 1
else:
    print("  It was 9")

ans = input("  What was the value of 'sport'?  : ")
if ans.lower().strip() == "badminton":
    print("  Correct!")
    r1_score = r1_score + 1
else:
    print("  It was 'Badminton'")

ans = input("  Was there a variable called 'food'? (yes/no): ")
if ans.lower().strip() == "no":
    print("  Correct! There was no 'food' variable.")
    r1_score = r1_score + 1
else:
    print("  Nope! There was no 'food' variable. Trick question!")

ans = input("  What was the value of 'color'?  : ")
if ans.lower().strip() == "green":
    print("  Correct!")
    r1_score = r1_score + 1
else:
    print("  It was 'Green'")

print(f"\n  Round 1 Score: {r1_score}/5")
total_score = total_score + r1_score

input("\nPress Enter for Round 2...")
print()

# ----- ROUND 2: 7 variables -----
print("--- Round 2: Memorize 7 Variables ---")
print("You have 15 seconds. MEMORIZE these!")
print()
print("  student = 'Aarav'")
print("  grade = 6")
print("  school = 'DAV School'")
print("  maths = 88")
print("  science = 95")
print("  hobby = 'Cricket'")
print("  pet = 'Dog'")
print()

for i in range(15, 0, -1):
    print(f"  Time remaining: {i} seconds...", end="\r")
    time.sleep(1)

print("\n" * 30)
print("=" * 40)
print("  SCREEN CLEARED! Answer from memory!")
print("=" * 40)
print()

r2_score = 0
ans = input("  What was the value of 'maths'?    : ")
if ans.strip() == "88":
    print("  Correct!")
    r2_score = r2_score + 1
else:
    print("  It was 88")

ans = input("  What was the value of 'school'?   : ")
if ans.lower().strip() in ["dav school", "dav"]:
    print("  Correct!")
    r2_score = r2_score + 1
else:
    print("  It was 'DAV School'")

ans = input("  What was the value of 'grade'?    : ")
if ans.strip() == "6":
    print("  Correct!")
    r2_score = r2_score + 1
else:
    print("  It was 6")

ans = input("  What was 'hobby'?                 : ")
if ans.lower().strip() == "cricket":
    print("  Correct!")
    r2_score = r2_score + 1
else:
    print("  It was 'Cricket'")

ans = input("  Which scored higher: maths or science? : ")
if ans.lower().strip() == "science":
    print("  Correct! science=95 > maths=88")
    r2_score = r2_score + 1
else:
    print("  It was science (95 > 88)")

print(f"\n  Round 2 Score: {r2_score}/5")
total_score = total_score + r2_score

input("\nPress Enter for the FINAL Round...")
print()

# ----- ROUND 3: 7 variables WITH a reassignment! -----
print("--- Round 3 (HARD): Variables CHANGE! ---")
print("Some variables get NEW values! Watch carefully!")
print("You have 18 seconds. MEMORIZE everything!")
print()
print("  player = 'Priya'")
print("  team = 'Blue Tigers'")
print("  score = 45")
print("  overs = 10")
print("  catches = 2")
print("  wickets = 1")
print("  score = 72")
print("  ^^^ SCORE CHANGED! ^^^")
print()

for i in range(18, 0, -1):
    print(f"  Time remaining: {i} seconds...", end="\r")
    time.sleep(1)

print("\n" * 30)
print("=" * 40)
print("  SCREEN CLEARED! Answer from memory!")
print("=" * 40)
print()

r3_score = 0
ans = input("  What is the FINAL value of 'score'? : ")
if ans.strip() == "72":
    print("  Correct! It was reassigned from 45 to 72.")
    r3_score = r3_score + 1
else:
    print("  It was 72! Remember, score was changed from 45 to 72.")

ans = input("  What was the value of 'team'?       : ")
if ans.lower().strip() == "blue tigers":
    print("  Correct!")
    r3_score = r3_score + 1
else:
    print("  It was 'Blue Tigers'")

ans = input("  What was the value of 'catches'?    : ")
if ans.strip() == "2":
    print("  Correct!")
    r3_score = r3_score + 1
else:
    print("  It was 2")

ans = input("  What was the FIRST value of score (before change)? : ")
if ans.strip() == "45":
    print("  Correct! Score started at 45 then changed to 72.")
    r3_score = r3_score + 1
else:
    print("  It was 45, then changed to 72.")

ans = input("  What was the value of 'player'?     : ")
if ans.lower().strip() == "priya":
    print("  Correct!")
    r3_score = r3_score + 1
else:
    print("  It was 'Priya'")

print(f"\n  Round 3 Score: {r3_score}/5")
total_score = total_score + r3_score

# Final Results
print()
print("=" * 40)
print(f"  TOTAL SCORE: {total_score} / 15")
print()
if total_score >= 13:
    print("  PHOTOGRAPHIC MEMORY! Incredible!")
elif total_score >= 9:
    print("  Strong memory! Keep training!")
elif total_score >= 5:
    print("  Good start! Your memory will improve with practice!")
else:
    print("  Memory is like a muscle - it gets stronger with practice!")
print("=" * 40)

# ============================================================
# REFLECTION PROMPTS:
# 1. Was Round 3 harder because the variable CHANGED value?
#    In real code, variables change all the time! That's why
#    programmers need strong memory to read code well.
#
# 2. Did you use any tricks to memorize? (e.g., grouping
#    related items, creating a story, repeating in your head)
#    These are real MEMORY TECHNIQUES that help in life too!
#
# 3. A computer never forgets a variable's value. But humans do!
#    That's why we write clear code with good variable names -
#    so we don't NEED to memorize everything!
# ============================================================
