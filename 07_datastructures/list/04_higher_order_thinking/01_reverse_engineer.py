# Reverse Engineer the List
# Normal coding: you know the goal → you write the code.
# Reverse engineering: you see the RESULT → you figure out WHAT CODE caused it.
# This builds deep understanding — if you can reverse it, you truly understand it.

score = 0


# --- Challenge 1: append ---
# A new item appeared at the END of the list.
# Which method adds to the end? → append()
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
# The item 30 at index 2 disappeared. Two methods can do this:
# remove(30)  → deletes by VALUE (doesn't need to know the index)
# pop(2)      → deletes by INDEX (doesn't need to know the value)
# Both are valid — that's why the challenge says "two valid answers"!
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
# The items rearranged from random order to alphabetical order.
# Only sort() or sorted() does this. Since the list itself changed → sort()
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
# Items went from mixed order to largest-first (descending).
# sort() alone gives ascending. To get descending → sort(reverse=True)
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
