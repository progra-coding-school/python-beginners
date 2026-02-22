# Program Code: LP-KN-04
# Title: break and continue
# Cognitive Skill: Knowledge
# Topic: Loops in Python

# break   → EXIT the loop immediately
# continue → SKIP this iteration, go to next

# --- break: stop the loop early ---
print("=== break ===")
for i in range(1, 11):
    if i == 6:
        print("Found 6! Stopping.")
        break
    print(i)
# Output: 1 2 3 4 5 → stops at 6

print()

# --- continue: skip one iteration ---
print("=== continue ===")
for i in range(1, 11):
    if i % 2 == 0:
        continue    # skip even numbers
    print(i)
# Output: 1 3 5 7 9 → skips all even numbers

print()

# --- break in a while loop ---
print("=== break in while ===")
number = 1
while number <= 100:
    if number > 5:
        break
    print(number)
    number += 1

print()

# --- Real-life: Search a list ---
print("=== Search with break ===")
shopping_list = ["rice", "dal", "sugar", "oil", "salt"]
search_item = input("Search for item: ")

for item in shopping_list:
    if item == search_item:
        print(f"'{search_item}' found in the list!")
        break
else:
    # This else runs if the loop finished WITHOUT a break
    print(f"'{search_item}' is NOT in the list.")

print()

# --- Real-life: Skip invalid data ---
print("=== Skip invalid with continue ===")
scores = [85, -1, 72, 999, 65, -5, 90]
for score in scores:
    if score < 0 or score > 100:
        print(f"  Skipping invalid score: {score}")
        continue
    print(f"  Valid score: {score}")

# Think:
# 1. What is the difference between break and continue?
# 2. If break is inside a nested loop, which loop does it exit?
