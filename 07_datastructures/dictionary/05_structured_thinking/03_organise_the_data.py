# Program Code: DC-ST-03
# Title: Organise the Data
# Cognitive Skill: Structured Thinking
# Topic: Dictionaries in Python

# Choosing the RIGHT data structure is the first step.
# Study each scenario and decide how to organise the data.

# ─── Scenario 1: Student profile ────────────────────────────────
print("=== Scenario 1: Student Profile ===")
# Need: store name, age, grade, city for one student
# Wrong: separate variables (hard to pass around)
# Right: one dictionary — everything about one student together

student = {
    "name":  "Aarav",
    "age":   13,
    "grade": 7,
    "city":  "Chennai",
}
print("Student:", student)
print()

# ─── Scenario 2: Class roster ───────────────────────────────────
print("=== Scenario 2: Class Roster ===")
# Need: store multiple students
# Wrong: one flat dict with mixed data
# Right: dict of dicts — name → profile

roster = {
    "Aarav":   {"age": 13, "grade": 7},
    "Diya":    {"age": 12, "grade": 6},
    "Karthik": {"age": 14, "grade": 8},
}
for name, info in roster.items():
    print(f"  {name}: Grade {info['grade']}, Age {info['age']}")
print()

# ─── Scenario 3: Attendance ─────────────────────────────────────
print("=== Scenario 3: Weekly Attendance ===")
# Need: track present/absent for each day per student
# Right: dict of dicts — student → {day → status}

attendance = {
    "Aarav": {"Mon": "P", "Tue": "P", "Wed": "A", "Thu": "P", "Fri": "P"},
    "Diya":  {"Mon": "P", "Tue": "A", "Wed": "P", "Thu": "P", "Fri": "A"},
}

for student, days in attendance.items():
    present = sum(1 for s in days.values() if s == "P")
    print(f"  {student}: {present}/5 days present")
print()

# ─── Scenario 4: Shop inventory ─────────────────────────────────
print("=== Scenario 4: Shop Inventory ===")
# Need: product → price AND quantity
# Right: dict of dicts

shop = {
    "pens":      {"price": 10, "qty": 50},
    "notebooks": {"price": 45, "qty": 30},
}
for item, data in shop.items():
    print(f"  {item}: Rs.{data['price']} × {data['qty']} = Rs.{data['price']*data['qty']}")

print()
print("=== Key Takeaway ===")
print("  Flat dict         → one thing with many properties")
print("  Dict of dicts     → many things, each with many properties")
print("  Dict with lists   → one thing with a collection of values")

# Think:
# 1. How would you redesign the attendance dict if you also needed to store the reason for absence?
# 2. Is a dict of dicts the best way for 10,000 students? What else might you use?
