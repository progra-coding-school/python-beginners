# Program Code: VAR-FC-03
# Title: Variable Memory Challenge
# Cognitive Skill: Focus and Concentration (Memory)
# Topic: Variables in Python

import time

total_score = 0

# Round 1 — 5 variables, 12 seconds
print("--- Round 1: Memorise 5 Variables ---")
print("You have 12 seconds!")
print("  name = 'Diya'")
print("  age = 9")
print("  city = 'Chennai'")
print("  sport = 'Badminton'")
print("  color = 'Green'")

for i in range(12, 0, -1):
    print("Time:", i, end="\r")
    time.sleep(1)

print("\n" * 30)
print("Answer from memory!")

r1 = 0
ans = input("Value of 'city'? ")
if ans.lower().strip() == "chennai":
    print("Correct!")
    r1 += 1
else:
    print("It was Chennai")

ans = input("Value of 'age'? ")
if ans.strip() == "9":
    print("Correct!")
    r1 += 1
else:
    print("It was 9")

ans = input("Value of 'sport'? ")
if ans.lower().strip() == "badminton":
    print("Correct!")
    r1 += 1
else:
    print("It was Badminton")

ans = input("Was there a variable called 'food'? (yes/no) ")
if ans.lower().strip() == "no":
    print("Correct! No food variable.")
    r1 += 1
else:
    print("No — there was no food variable.")

ans = input("Value of 'color'? ")
if ans.lower().strip() == "green":
    print("Correct!")
    r1 += 1
else:
    print("It was Green")

print("Round 1 score:", r1, "/ 5")
total_score += r1
input("Press Enter for Round 2...")

# Round 2 — 7 variables, 15 seconds
print("--- Round 2: Memorise 7 Variables ---")
print("You have 15 seconds!")
print("  student = 'Aarav'")
print("  grade = 6")
print("  school = 'DAV School'")
print("  maths = 88")
print("  science = 95")
print("  hobby = 'Cricket'")
print("  pet = 'Dog'")

for i in range(15, 0, -1):
    print("Time:", i, end="\r")
    time.sleep(1)

print("\n" * 30)
print("Answer from memory!")

r2 = 0
ans = input("Value of 'maths'? ")
if ans.strip() == "88":
    print("Correct!")
    r2 += 1
else:
    print("It was 88")

ans = input("Value of 'school'? ")
if ans.lower().strip() in ["dav school", "dav"]:
    print("Correct!")
    r2 += 1
else:
    print("It was DAV School")

ans = input("Value of 'grade'? ")
if ans.strip() == "6":
    print("Correct!")
    r2 += 1
else:
    print("It was 6")

ans = input("Which scored higher — maths or science? ")
if ans.lower().strip() == "science":
    print("Correct! science=95 > maths=88")
    r2 += 1
else:
    print("It was science (95 > 88)")

print("Round 2 score:", r2, "/ 4")
total_score += r2
input("Press Enter for Round 3...")

# Round 3 — variable that changes!
print("--- Round 3: Variable Changes! ---")
print("You have 18 seconds!")
print("  player = 'Priya'")
print("  score = 45")
print("  catches = 2")
print("  score = 72    <-- SCORE CHANGED!")

for i in range(18, 0, -1):
    print("Time:", i, end="\r")
    time.sleep(1)

print("\n" * 30)
print("Answer from memory!")

r3 = 0
ans = input("FINAL value of 'score'? ")
if ans.strip() == "72":
    print("Correct! It changed from 45 to 72.")
    r3 += 1
else:
    print("It was 72 (changed from 45).")

ans = input("FIRST value of 'score' (before change)? ")
if ans.strip() == "45":
    print("Correct!")
    r3 += 1
else:
    print("It was 45, then changed to 72.")

ans = input("Value of 'catches'? ")
if ans.strip() == "2":
    print("Correct!")
    r3 += 1
else:
    print("It was 2")

print("Round 3 score:", r3, "/ 3")
total_score += r3

print("Total score:", total_score, "/ 12")
