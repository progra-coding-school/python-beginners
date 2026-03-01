# Why Dictionaries Exist
# Before dictionaries, we stored related data in separate parallel lists.
# Lists work, but they are fragile — if the lists ever go out of sync, you get wrong data.
# A dictionary keeps all related data TOGETHER under a single meaningful key.
# KEY IDEA: label your data with names, not just store it by position.

# Without a dictionary — parallel lists approach
# To find Diya's grade, you must first find her index in the names list
names   = ["Aarav", "Diya", "Karthik"]
ages    = [13,       12,      14      ]
grades  = [7,        6,       8       ]

diya_index = names.index("Diya")
print("Diya's grade:", grades[diya_index])

# What goes wrong with parallel lists?
# → If someone inserts into names but forgets ages, all data shifts and breaks!
print("Problem: 3 separate lists must always stay in sync. Easy to break!")

print()

# With a dictionary — one clean structure
# Each student's data lives TOGETHER under their name as the key
# No index needed — just look up by name directly
students = {
    "Aarav":   {"age": 13, "grade": 7},
    "Diya":    {"age": 12, "grade": 6},
    "Karthik": {"age": 14, "grade": 8},
}

print("Diya's grade:", students["Diya"]["grade"])

# Adding a new student is easy — all their data stays in one place
students["Riya"] = {"age": 11, "grade": 5}
print("Added Riya:", students["Riya"])

print()

# Real-life example: contact book
# Without dict: find the index first, then look up the phone — two steps, two lists
contact_names   = ["Aarav", "Diya", "Amma"]
contact_phones  = ["9876543210", "9123456780", "9988776655"]
search = "Diya"
idx = contact_names.index(search)
print("Without dict —", search + "'s phone:", contact_phones[idx])

# With dict: one step, direct lookup by name — fast and readable
contacts = {
    "Aarav": "9876543210",
    "Diya":  "9123456780",
    "Amma":  "9988776655",
}
print("With dict    —", search + "'s phone:", contacts[search])

print()

# Three reasons dictionaries exist
print("3 Reasons Dictionaries Exist:")
print("  1. LABEL data meaningfully — 'name', 'age' instead of index 0, 1")
print("  2. FAST lookup — find by key directly, no looping needed")
print("  3. GROUPED — all data about one thing stays together")
