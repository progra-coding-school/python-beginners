# List Pattern Finder
# Every list tells a story — the items follow a pattern.
# This exercise trains you to spot the rule hidden in the numbers.
# Look at the values, find the rule (+2, x3, sum, slice...), then answer.

score = 0
total = 5

# --- Q1: +2 pattern ---
# Each number increases by 2: 2, 4, 6, 8 → next must be 10
print("Q1: What comes next?")
print("  evens = [2, 4, 6, 8, ?]")
ans = input("  > ").strip()
if ans == "10":
    print("  Correct! Pattern: +2 each time.")
    score += 1
else:
    print("  Answer: 10   (+2 pattern: 2, 4, 6, 8, 10)")
print()

# --- Q2: ×3 pattern with a gap ---
# 1 × 3 = 3, 3 × 3 = 9, 9 × 3 = 27, 27 × 3 = 81
print("Q2: What is the missing value?")
print("  teams = [1, 3, 9, ?, 81]")
print("  (Hint: each number is multiplied by 3)")
ans = input("  > ").strip()
if ans == "27":
    print("  Correct! Pattern: x3 each time. 1, 3, 9, 27, 81.")
    score += 1
else:
    print("  Answer: 27   (x3 pattern: 1 -> 3 -> 9 -> 27 -> 81)")
print()

# --- Q3: accumulator pattern (running total) ---
# total starts at 0 and adds each item: 0+10=10, +20=30, +30=60, +40=100
print("Q3: After this code, what is total?")
print("  nums = [10, 20, 30, 40]")
print("  total = 0")
print("  for n in nums:")
print("      total += n")
ans = input("  > ").strip()
if ans == "100":
    print("  Correct! 10 + 20 + 30 + 40 = 100.")
    score += 1
else:
    print("  Answer: 100   (10 + 20 + 30 + 40 = 100)")
print()

# --- Q4: step slicing ---
# [::2] means: start at 0, go to end, step by 2 — picks index 0, 2 → 'a', 'c'
print("Q4: What is the output?")
print("  letters = ['a', 'b', 'c', 'd']")
print("  print(letters[::2])")
ans = input("  > ").strip().replace(" ", "")
if ans in ["['a','c']", "['a', 'c']"]:
    print("  Correct! Step 2 takes every other item starting from index 0.")
    score += 1
else:
    print("  Answer: ['a', 'c']   (every 2nd item: index 0, 2)")
print()

# --- Q5 (Boss Round): sort descending then index 0 ---
# sort(reverse=True) gives [5, 4, 3, 2, 1] — largest first — so index 0 = 5
print("Q5 (Boss Round): What is the output?")
print("  nums = [5, 1, 3, 2, 4]")
print("  nums.sort(reverse=True)")
print("  print(nums[0])")
ans = input("  > ").strip()
if ans == "5":
    print("  Correct! Descending sort gives [5, 4, 3, 2, 1] — index 0 = 5.")
    score += 1
else:
    print("  Answer: 5   (sort descending: [5, 4, 3, 2, 1], index 0 = 5)")
print()

print("Score:", score, "/", total)
