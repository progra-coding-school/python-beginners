# Program Code: SE-CT-02
# Title: Which Approach Is Better?
# Cognitive Skill: Critical Thinking
# Topic: Sets in Python

# Two approaches — same problem, different tools.
# Read both, decide which is better and why.

# =========================================================
# Problem 1: Find unique items in a list
# =========================================================

print("=== Problem 1: Remove duplicates ===")

items = ["pen", "book", "pen", "eraser", "book", "pen", "ruler"]

# Approach A: Manual loop
unique_a = []
for item in items:
    if item not in unique_a:
        unique_a.append(item)
print("Approach A:", sorted(unique_a))

# Approach B: Set
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

print("=== Problem 2: Homework submission check ===")

# 500 students — checking if each name is in the submission list
submitted_list = ["Aarav", "Diya", "Karthik", "Riya", "Ananya"]
submitted_set  = {"Aarav", "Diya", "Karthik", "Riya", "Ananya"}

student = "Karthik"

# Approach A: list
result_a = student in submitted_list   # scans left to right
print("List check:", result_a)

# Approach B: set
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

print("=== Problem 3: Common items between two groups ===")

group1 = ["mango", "banana", "apple", "grapes"]
group2 = ["banana", "orange", "apple", "mango"]

# Approach A: nested loop
common_a = []
for item in group1:
    if item in group2 and item not in common_a:
        common_a.append(item)
print("Approach A:", sorted(common_a))

# Approach B: set intersection
common_b = set(group1) & set(group2)
print("Approach B:", sorted(common_b))

print()
print("Verdict: Approach B is clearer and faster.")
print("  A uses nested logic and manual duplicate checking.")
print("  B uses & — one symbol, self-documenting.")

# Think:
# 1. Can you think of a situation where the LIST approach might be necessary?
# 2. Does Approach B always preserve the original order? Does it matter here?
