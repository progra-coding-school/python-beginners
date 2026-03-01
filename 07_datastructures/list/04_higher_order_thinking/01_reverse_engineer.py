# Program Code: LIST-HOT-01
# Title: Reverse Engineer the List
# Cognitive Skill: Higher Order Thinking (Reverse engineering)
# Topic: Lists in Python

score = 0

print("=== Reverse Engineer the List ===")
print("Given BEFORE and AFTER — figure out what code ran.")
print()

# --- Challenge 1: append ---
print("Challenge 1:")
print("  Before: ['Aarav', 'Diya', 'Kabir']")
print("  After : ['Aarav', 'Diya', 'Kabir', 'Meera']")
print("  What single line of code caused this change?")
ans = input("  > ").strip().lower()
print("  Answer: team.append('Meera')")
if "append" in ans:
    print("  Correct!")
    score += 1
print()

# --- Challenge 2: remove or pop ---
print("Challenge 2:")
print("  Before: [10, 20, 30, 40, 50]")
print("  After : [10, 20, 40, 50]")
print("  30 is gone. What code removed it? (two valid answers!)")
ans = input("  > ").strip().lower()
print("  Answer: scores.remove(30)  OR  scores.pop(2)")
if "remove" in ans or "pop" in ans:
    print("  Correct!")
    score += 1
print()

# --- Challenge 3: sort ---
print("Challenge 3:")
print("  Before: ['mango', 'apple', 'banana']")
print("  After : ['apple', 'banana', 'mango']")
print("  Items rearranged alphabetically. What did this?")
ans = input("  > ").strip().lower()
print("  Answer: fruits.sort()")
if "sort" in ans:
    print("  Correct!")
    score += 1
print()

# --- Challenge 4: sort(reverse=True) ---
print("Challenge 4 (Boss Round):")
print("  Before: [5, 3, 8, 1, 9]")
print("  After : [9, 8, 5, 3, 1]")
print("  Sorted largest to smallest. What did this?")
ans = input("  > ").strip().lower()
print("  Answer: rankings.sort(reverse=True)")
if "reverse" in ans:
    print("  Correct!")
    score += 1
print()

print("Score:", score, "/ 4")
