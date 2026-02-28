# Program Code: DC-ST-02
# Title: Naming Matters
# Cognitive Skill: Structured Thinking
# Topic: Dictionaries in Python

# Good names make code readable without needing comments.
# Compare the same program written with poor names vs good names.

# ─── VERSION A: Poor naming ─────────────────────────────────────
print("=== Version A: Poor naming (hard to read) ===")

d  = {"a": 13, "b": 7, "c": 85}
d2 = {}

for x in d:
    if d[x] > 10:
        d2[x] = d[x]

print(d2)
# What does this do? Hard to tell without reading closely!

print()

# ─── VERSION B: Good naming ─────────────────────────────────────
print("=== Version B: Good naming (self-explanatory) ===")

student_ages     = {"Aarav": 13, "Diya": 7, "Karthik": 85}  # sample data
secondary_school = {}

for student_name, age in student_ages.items():
    if age > 10:
        secondary_school[student_name] = age

print(secondary_school)
# Immediately clear: filter students older than 10.

print()

# ─── Naming rules for dictionaries ──────────────────────────────
print("=== Naming Guidelines ===")
guidelines = {
    "Use noun phrases"        : "student_marks, not d or data",
    "Key describes content"   : "'name', 'price', 'qty' — not 'k' or 'x'",
    "Plural for collections"  : "contacts = {}, not contact = {}",
    "Avoid abbreviations"     : "total_price not tp",
    "Singular for one record" : "student = {'name': 'Aarav'} not students",
}

for rule, example in guidelines.items():
    print(f"  {rule:<28} → {example}")

print()

# ─── Practice: rename these variables ───────────────────────────
print("=== Practice: What better names would you use? ===")

# Poor:
d3 = {"r": 120, "g": 45, "b": 85}
# Better names might be: fruit_prices = {"mango": 120, "banana": 45, "apple": 85}

# Poor:
x2 = {"p": "9876543210", "q": "9123456780"}
# Better: emergency_contacts = {"hospital": "...", "police": "..."}

print("Rename d3:")
fruit_prices = {"mango": 120, "banana": 45, "apple": 85}
print("  fruit_prices =", fruit_prices)

print("Rename x2:")
emergency_contacts = {"hospital": "9876543210", "police": "9123456780"}
print("  emergency_contacts =", emergency_contacts)

# Think:
# 1. Look at a program you wrote before — are your variable names clear?
# 2. What is a bad name for a dictionary storing a student's subjects and marks?
#    What would a good name be?
