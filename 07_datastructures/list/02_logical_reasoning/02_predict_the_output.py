# Program Code: LIST-LR-02
# Title: Predict the Output
# Cognitive Skill: Logical Reasoning (Predicting list output)
# Topic: Lists in Python

score = 0
total = 5

print("=== Predict the List Output ===")
print("Predict the EXACT output of each code snippet.")
print()

# --- Q1 ---
print("Q1:")
print("  students = ['Aarav', 'Diya', 'Kabir']")
print("  print(students[2])")
ans = input("  > ").strip()
students = ["Aarav", "Diya", "Kabir"]
if ans == str(students[2]):
    print("  Correct!")
    score += 1
else:
    print("  Answer:", students[2], " (index 2 = third item)")
print()

# --- Q2 ---
print("Q2:")
print("  marks = [88, 74, 91, 65, 80]")
print("  print(marks[1:4])")
ans = input("  > ").strip().replace(" ", "")
marks = [88, 74, 91, 65, 80]
actual = marks[1:4]
if ans == str(actual).replace(" ", ""):
    print("  Correct!")
    score += 1
else:
    print("  Answer:", actual, " (index 1, 2, 3 — stops before 4)")
print()

# --- Q3 ---
print("Q3:")
print("  scores = [67, 23, 89, 45]")
print("  scores.sort()")
print("  print(scores[0])")
ans = input("  > ").strip()
scores = [67, 23, 89, 45]
scores.sort()
if ans == str(scores[0]):
    print("  Correct! sort() gives", scores, "— index 0 is", scores[0])
    score += 1
else:
    print("  Answer:", scores[0], " (after sort:", scores, ")")
print()

# --- Q4 ---
print("Q4:")
print("  team = ['Aarav', 'Diya', 'Kabir', 'Riya']")
print("  team.append('Arjun')")
print("  team.pop()")
print("  team.pop()")
print("  print(len(team))")
ans = input("  > ").strip()
team = ["Aarav", "Diya", "Kabir", "Riya"]
team.append("Arjun")
team.pop()
team.pop()
if ans == str(len(team)):
    print("  Correct! Start 4, +1 append, -2 pops = 3")
    score += 1
else:
    print("  Answer:", len(team), " (4 + 1 append - 2 pops = 3)")
print()

# --- Q5 ---
print("Q5 (Boss):")
print("  fruits = ['mango', 'banana', 'apple']")
print("  for i, fruit in enumerate(fruits):")
print("      print(i, fruit)")
print("  What does the loop print? (type line by line, e.g. 0 mango / 1 banana / ...)")
ans = input("  > ").strip()
fruits = ["mango", "banana", "apple"]
lines = [str(i) + " " + fruit for i, fruit in enumerate(fruits)]
actual = " / ".join(lines)
if ans.replace(" ", "") == actual.replace(" ", ""):
    print("  Correct!")
    score += 1
else:
    print("  Answer:", actual)
print()

print("Score:", score, "/", total)
