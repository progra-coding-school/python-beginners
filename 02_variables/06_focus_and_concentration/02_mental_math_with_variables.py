# Program Code: CS-FC-02
# Title: Mental Math with Variables - Brain Calculator!
# Cognitive Skill: Focus & Concentration (Mental tracking of changing values)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav is playing a cricket match! His score keeps changing
# every over. Can you track his score in YOUR HEAD?
# No paper. No calculator. Just your BRAIN!
# Follow each step and keep a running total mentally.
# At the end, tell me the final score!
# ============================================================

# ------------------------------------------------------------
# INSTRUCTIONS:
# 1. A variable starts at a value
# 2. Operations are shown one by one
# 3. Track the value MENTALLY (in your head!)
# 4. At the end, enter your answer
# 5. NO paper, NO calculator - pure brain power!
# ------------------------------------------------------------

import time

score = 0

print("=== Brain Calculator: Mental Math with Variables ===")
print("Track the value in your HEAD. No paper allowed!")
print()

# ----- ROUND 1: Easy (3 operations) -----
print("--- Round 1 (Easy) ---")
print()
print("Aarav starts his innings...")
print()
time.sleep(1)

print("  runs = 0")
time.sleep(2)
print("  Over 1: runs = runs + 6    (Hit a six!)")
time.sleep(2)
print("  Over 2: runs = runs + 4    (Hit a four!)")
time.sleep(2)
print("  Over 3: runs = runs + 3    (Took 3 singles)")
print()

# Actual calculation
runs = 0
runs = runs + 6
runs = runs + 4
runs = runs + 3

guess = int(input("What is the value of runs? : "))
print(f"Answer: runs = {runs}")
if guess == runs:
    print("Correct! 0 + 6 + 4 + 3 = 13")
    score = score + 1
else:
    print(f"Trace: 0 -> 6 -> 10 -> {runs}")
print()
time.sleep(1)

# ----- ROUND 2: Medium (5 operations) -----
print("--- Round 2 (Medium) ---")
print()
print("Diya is counting her savings this week...")
print()
time.sleep(1)

print("  savings = 50              (Started with Rs.50)")
time.sleep(2)
print("  savings = savings + 20    (Monday pocket money)")
time.sleep(2)
print("  savings = savings - 15    (Bought pencils)")
time.sleep(2)
print("  savings = savings + 20    (Wednesday pocket money)")
time.sleep(2)
print("  savings = savings + 10    (Found a Rs.10 note!)")
time.sleep(2)
print("  savings = savings - 25    (Bought a book)")
print()

savings = 50
savings = savings + 20
savings = savings - 15
savings = savings + 20
savings = savings + 10
savings = savings - 25

guess = int(input("What is the value of savings? : "))
print(f"Answer: savings = {savings}")
if guess == savings:
    print("Excellent mental math!")
    score = score + 1
else:
    print(f"Trace: 50 -> 70 -> 55 -> 75 -> 85 -> {savings}")
print()
time.sleep(1)

# ----- ROUND 3: Hard (7 operations with multiply) -----
print("--- Round 3 (Hard!) ---")
print()
print("A shopkeeper is calculating throughout the day...")
print()
time.sleep(1)

print("  money = 100               (Started the day with Rs.100)")
time.sleep(2)
print("  money = money + 50        (First customer)")
time.sleep(2)
print("  money = money + 50        (Second customer)")
time.sleep(2)
print("  money = money - 80        (Paid the supplier)")
time.sleep(2)
print("  money = money + 30        (Third customer)")
time.sleep(2)
print("  money = money + 40        (Fourth customer)")
time.sleep(2)
print("  money = money - 60        (Bought more stock)")
time.sleep(2)
print("  money = money + 20        (Fifth customer)")
print()

money = 100
money = money + 50
money = money + 50
money = money - 80
money = money + 30
money = money + 40
money = money - 60
money = money + 20

guess = int(input("What is the value of money? : "))
print(f"Answer: money = {money}")
if guess == money:
    print("Incredible focus! You tracked 7 operations mentally!")
    score = score + 1
else:
    print(f"Trace: 100 -> 150 -> 200 -> 120 -> 150 -> 190 -> 130 -> {money}")

print()
print("=" * 40)
print(f"YOUR SCORE: {score} / 3")
if score == 3:
    print("Your brain is a SUPERCOMPUTER!")
elif score >= 1:
    print("Good effort! Practice makes the brain stronger!")
else:
    print("Keep trying! Mental math is like a muscle - it grows!")
print("=" * 40)

# ============================================================
# REFLECTION PROMPTS:
# 1. Was it harder to track when there were MORE steps?
#    Why does our brain struggle with many steps?
# 2. What tricks did you use to keep track? Did you
#    say the number in your head after each step?
# 3. A computer NEVER loses track, even after 1000 steps.
#    That's why we use variables! They are the computer's
#    PERFECT memory. But training YOUR brain to track
#    values makes you a better programmer!
# ============================================================
