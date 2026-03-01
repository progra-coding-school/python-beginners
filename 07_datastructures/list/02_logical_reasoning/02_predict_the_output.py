# Predict the Output
# Before running code, a good programmer can predict exactly what it will print.
# This skill comes from understanding what each operation does step by step.
# Read each snippet, work it out in your head, then type the exact output.

score = 0
total = 5

# --- Q1: Basic index access ---
# Index 2 means the THIRD item (counting starts at 0)
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

# --- Q2: Slicing ---
# marks[1:4] means: start at index 1, stop BEFORE index 4
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

# --- Q3: sort() then index 0 ---
# sort() rearranges the list first; then [0] gives the smallest (it is now at the front)
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

# --- Q4: append then two pops ---
# Count carefully: start=4, +1 append=5, -1 pop=4, -1 pop=3
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

# --- Q5 (Boss): enumerate loop output ---
# enumerate gives (index, item) pairs starting at 0 — print(i, fruit) prints "0 mango" etc.
print("Q5 (Boss):")
print("  fruits = ['mango', 'banana', 'apple']")
print("  for i, fruit in enumerate(fruits):")
print("      print(i, fruit)")
print("  What does the loop print? (e.g. 0 mango / 1 banana / ...)")
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
