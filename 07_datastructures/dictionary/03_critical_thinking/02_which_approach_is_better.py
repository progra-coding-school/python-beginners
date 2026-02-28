# Program Code: DC-CT-02
# Title: Which Approach Is Better?
# Cognitive Skill: Critical Thinking
# Topic: Dictionaries in Python

# Two approaches solve the same problem.
# Read both, then decide: WHICH IS BETTER and WHY?

# =========================================================
# Problem: Find a student's phone number by name
# =========================================================

print("=== Approach A: Parallel Lists ===")
names  = ["Aarav", "Diya", "Karthik", "Riya"]
phones = ["9876543210", "9123456780", "9988776655", "9876001122"]

search = "Karthik"
if search in names:
    idx = names.index(search)
    print(f"{search}'s phone: {phones[idx]}")
else:
    print("Not found.")

print()
print("=== Approach B: Dictionary ===")
contacts = {
    "Aarav":   "9876543210",
    "Diya":    "9123456780",
    "Karthik": "9988776655",
    "Riya":    "9876001122",
}

phone = contacts.get(search, "Not found.")
print(f"{search}'s phone: {phone}")

print()
print("--- Verdict ---")
print("Approach B (dictionary) is better because:")
print("  1. Lookup is direct — no need to find an index first.")
print("  2. Adding a contact keeps everything in one place.")
print("  3. Lists can go out of sync if someone adds to one but forgets the other.")

print()

# =========================================================
# Problem: Count how many times each item appears
# =========================================================

print("=== Approach A: Manual search with a list ===")
items   = ["pen", "book", "pen", "eraser", "pen", "book"]
counted = []

for item in items:
    found = False
    for entry in counted:
        if entry[0] == item:
            entry[1] += 1
            found = True
            break
    if not found:
        counted.append([item, 1])

for entry in counted:
    print(f"  {entry[0]}: {entry[1]}")

print()
print("=== Approach B: Dictionary counter ===")
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

for item, count in freq.items():
    print(f"  {item}: {count}")

print()
print("--- Verdict ---")
print("Approach B is shorter, clearer, and faster to read and write.")
print("Approach A uses nested loops — harder to understand and maintain.")

# Think:
# 1. Can you think of a situation where parallel lists might actually make sense?
# 2. Why does Approach B use .get(item, 0) instead of just freq[item]?
