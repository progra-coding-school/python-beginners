# Which Approach Is Better?
# Two approaches — same problem, different tools.
# Read both, decide which is better and why.

# =========================================================
# Problem 1: Find unique items in a list
# =========================================================

print("Problem 1: Remove duplicates:")

items = ["pen", "book", "pen", "eraser", "book", "pen", "ruler"]

# Approach A: Manual loop — scans the growing list every time
unique_a = []
for item in items:
    if item not in unique_a:    # this check scans the whole list on every iteration
        unique_a.append(item)
print("Approach A:", sorted(unique_a))

# Approach B: Set — O(1) membership check, one line
unique_b = list(set(items))
print("Approach B:", sorted(unique_b))

print()
print("Verdict: Approach B is better.")
print("  A scans the list every time — slow for large lists.")
print("  B uses a set — O(1) membership, much faster.")
print("  B is also one line vs 3 lines.")

print()

# =========================================================
# Problem 2: Check if a student submitted homework
# =========================================================

print("Problem 2: Homework submission check:")

# 500 students — checking if each name is in the submission list
submitted_list = ["Aarav", "Diya", "Karthik", "Riya", "Ananya"]
submitted_set  = {"Aarav", "Diya", "Karthik", "Riya", "Ananya"}

student = "Karthik"

# Approach A: list — Python scans from the first item until it finds the match
result_a = student in submitted_list   # scans left to right
print("List check:", result_a)

# Approach B: set — Python computes the hash and jumps directly to the slot
result_b = student in submitted_set    # direct hash lookup
print("Set check :", result_b)

print()
print("Verdict: Approach B is better for large collections.")
print("  List: speed degrades as list grows (O(n))")
print("  Set : always near-instant (O(1)) regardless of size")

print()

# =========================================================
# Problem 3: Finding common items
# =========================================================

print("Problem 3: Common items between two groups:")

group1 = ["mango", "banana", "apple", "grapes"]
group2 = ["banana", "orange", "apple", "mango"]

# Approach A: nested loop — checks every item in group1 against every item in group2
common_a = []
for item in group1:
    if item in group2 and item not in common_a:
        common_a.append(item)
print("Approach A:", sorted(common_a))

# Approach B: set intersection — one operator, built-in, fast
common_b = set(group1) & set(group2)
print("Approach B:", sorted(common_b))

print()
print("Verdict: Approach B is clearer and faster.")
print("  A uses nested logic and manual duplicate checking.")
print("  B uses & — one symbol, self-documenting.")

# Think:
# 1. Can you think of a situation where the LIST approach might be necessary?
# 2. Does Approach B always preserve the original order? Does it matter here?
