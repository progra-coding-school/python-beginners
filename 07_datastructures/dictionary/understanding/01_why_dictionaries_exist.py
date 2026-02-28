# Program Code: DC-UN-01
# Title: Why Dictionaries Exist
# Cognitive Skill: Understanding
# Topic: Dictionaries in Python

# WITHOUT a dictionary: you need parallel lists — messy and fragile.
# WITH a dictionary: one structure, keys make retrieval natural.

print("=== WITHOUT a dictionary — parallel lists ===")

names   = ["Aarav", "Diya", "Karthik"]
ages    = [13,       12,      14      ]
grades  = [7,        6,       8       ]

# To find Diya's grade, you must know her INDEX
diya_index = names.index("Diya")
print(f"Diya's grade: {grades[diya_index]}")

# What if lists get out of sync? Disaster!
# What if someone inserts into names but forgets ages? Wrong data!
print("Problem: 3 separate lists must always stay in sync. Easy to break!")

print()

print("=== WITH a dictionary — one clean structure ===")

students = {
    "Aarav":   {"age": 13, "grade": 7},
    "Diya":    {"age": 12, "grade": 6},
    "Karthik": {"age": 14, "grade": 8},
}

# To find Diya's grade — readable and direct
print(f"Diya's grade: {students['Diya']['grade']}")

# Add a new student — everything stays together
students["Riya"] = {"age": 11, "grade": 5}
print("Added Riya:", students["Riya"])

print()

# --- Real-life: phone contacts ---
print("=== Real-life: Contact Book ===")

# Without dict: search through two lists
contact_names   = ["Aarav", "Diya", "Amma"]
contact_phones  = ["9876543210", "9123456780", "9988776655"]
search = "Diya"
idx = contact_names.index(search)
print(f"Without dict — {search}'s phone: {contact_phones[idx]}")

# With dict: instant lookup by name
contacts = {
    "Aarav": "9876543210",
    "Diya":  "9123456780",
    "Amma":  "9988776655",
}
print(f"With dict    — {search}'s phone: {contacts[search]}")

print()

print("=== 3 Reasons Dictionaries Exist ===")
print("1. LABEL data meaningfully — 'name', 'age' instead of index 0, 1")
print("2. FAST lookup — find by key directly, no looping needed")
print("3. GROUPED — all data about one thing stays together")

# Think:
# 1. How would you store a cricket team's player stats WITHOUT a dictionary?
# 2. Name 3 real apps that use key-value storage (hint: login, settings, maps).
