# Spot the Bug
# A good programmer does not just write code — they also read code critically.
# Each snippet below has ONE bug. Figure out what is wrong and why it will fail.
# Understanding bugs teaches you to write safer code from the start.

score = 0
total = 5

# --- Bug 1: IndexError — index out of valid range ---
# A 5-item list has valid indices 0, 1, 2, 3, 4. Index 5 does not exist!
print("Bug 1:")
print("  students = ['Aarav', 'Diya', 'Kabir', 'Riya', 'Arjun']")
print("  print(students[5])")
print("  What is the bug?")
ans = input("  > ").strip().lower()
if "index" in ans or "5" in ans or "out" in ans or "range" in ans or "6th" in ans:
    print("  Correct! List has 5 items (indices 0-4). Index 5 does not exist.")
    score += 1
else:
    print("  Bug: IndexError — 5 items means valid indices are 0 to 4. Index 5 is out of range.")
print()

# --- Bug 2: ValueError — remove() item not in list ---
# remove() searches for the value. If it cannot find it, it raises a ValueError.
# Always check with 'in' before removing!
print("Bug 2:")
print("  fruits = ['apple', 'banana', 'mango']")
print("  fruits.remove('guava')")
print("  What is the bug?")
ans = input("  > ").strip().lower()
if "guava" in ans or "value" in ans or "not in" in ans or "exist" in ans or "found" in ans:
    print("  Correct! 'guava' is not in the list — remove() gives ValueError.")
    score += 1
else:
    print("  Bug: ValueError — 'guava' is not in the list. Check with 'in' before removing.")
print()

# --- Bug 3: append vs extend — wraps the list as ONE nested item ---
# append(new) adds the ENTIRE list as a single item → team becomes length 3, not 4
# extend(new) adds each item separately → team becomes length 4 (correct)
print("Bug 3:")
print("  team = ['Aarav', 'Diya']")
print("  new = ['Kabir', 'Meera']")
print("  team.append(new)")
print("  print(len(team))   # Expected: 4")
print("  What is wrong — and what is the actual result?")
ans = input("  > ").strip()
if "3" in ans or "nested" in ans or "one item" in ans or "extend" in ans:
    print("  Correct! append(new) adds the whole list as ONE item → len = 3. Use extend(new).")
    score += 1
else:
    print("  Bug: len is 3 not 4. append() wraps new as ONE nested item. Use extend(new).")
print()

# --- Bug 4: off-by-one — range too large by 1 ---
# range(len(marks)) gives 0 to 4 — correct for a 5-item list
# range(len(marks) + 1) gives 0 to 5 — tries index 5 which does not exist → IndexError
print("Bug 4:")
print("  marks = [85, 90, 78, 92, 88]")
print("  for i in range(len(marks) + 1):")
print("      print(marks[i])")
print("  What is the bug?")
ans = input("  > ").strip().lower()
if "5" in ans or "+1" in ans or "range" in ans or "index" in ans or "out" in ans:
    print("  Correct! range(len(marks)+1) goes from 0 to 5. Index 5 does not exist → IndexError.")
    score += 1
else:
    print("  Bug: range(len+1) tries index 5 on a 5-item list. Use range(len(marks)) instead.")
print()

# --- Bug 5: poor style — manual loop instead of 'in' keyword ---
# The loop works, but it is unnecessarily complex.
# Python's 'in' keyword does the same search in one line — simpler and cleaner.
print("Bug 5 (Boss Bug):")
print("  cities = ['Chennai', 'Mumbai', 'Delhi', 'Kolkata']")
print("  found = False")
print("  for city in cities:")
print("      if city == 'Delhi': found = True")
print("  if found: print('City found!')")
print("  This works but has a problem. What is wrong with this approach?")
ans = input("  > ").strip().lower()
if "in" in ans or "manual" in ans or "scale" in ans or "simpler" in ans or "builtin" in ans or "built" in ans:
    print("  Correct! Use 'Delhi' in cities — one line, works for any size list.")
    score += 1
else:
    print("  Bug: Unnecessary manual loop. Use: if 'Delhi' in cities: print('Found!')")
print()

print("Score:", score, "/", total)
print()
# Summary of all bugs seen — good reference to review
print("Summary of bugs:")
print("  1. IndexError  — index out of valid range (0 to len-1)")
print("  2. ValueError  — remove() item not in list (check with 'in' first)")
print("  3. Logic bug   — append(list) nests it; use extend() to add items")
print("  4. Off-by-one  — range(len+1) goes one step too far")
print("  5. Poor style  — use 'item in list' instead of manual loop search")
