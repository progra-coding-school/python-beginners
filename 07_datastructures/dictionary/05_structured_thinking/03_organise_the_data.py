# Organise the Data — Choosing the Right Dictionary Structure
# The structure you choose determines how easy every operation will be.
# Three common patterns:
#   Flat dict       → one thing with multiple properties: {"name": "Aarav", "age": 13}
#   Dict of dicts   → many things, each with multiple properties: {name: {age, grade}}
#   Dict with lists → one key, collection of values: {sport: [player1, player2]}

# Scenario 1: Single student profile
# One student, multiple properties — flat dictionary is the right fit
print("Scenario 1: Student Profile")
# Wrong: four separate variables → hard to pass around, easy to lose track
# Right: one dictionary — everything about one student in one place
student = {
    "name":  "Aarav",
    "age":   13,
    "grade": 7,
    "city":  "Chennai",
}
print("Student:", student)
print()

# Scenario 2: Multiple students — dictionary of dictionaries
# Each student's name is the OUTER key; their profile is the INNER dict
# This lets you look up any student's data directly by name: roster["Aarav"]
print("Scenario 2: Class Roster")
roster = {
    "Aarav":   {"age": 13, "grade": 7},
    "Diya":    {"age": 12, "grade": 6},
    "Karthik": {"age": 14, "grade": 8},
}
for name, info in roster.items():
    print("  " + name + ": Grade " + str(info["grade"]) + ", Age " + str(info["age"]))
print()

# Scenario 3: Attendance — student → {day → status}
# Two levels of nesting: student name → day → "P" or "A"
# To count attendance: loop through values and count how many are "P"
print("Scenario 3: Weekly Attendance")
attendance = {
    "Aarav": {"Mon": "P", "Tue": "P", "Wed": "A", "Thu": "P", "Fri": "P"},
    "Diya":  {"Mon": "P", "Tue": "A", "Wed": "P", "Thu": "P", "Fri": "A"},
}
for student, days in attendance.items():
    present = sum(1 for s in days.values() if s == "P")   # count "P" entries
    print("  " + student + ":", str(present) + "/5 days present")
print()

# Scenario 4: Shop inventory — product → {price, quantity}
# Nesting lets you store multiple properties per product in one clean lookup
print("Scenario 4: Shop Inventory")
shop = {
    "pens":      {"price": 10, "qty": 50},
    "notebooks": {"price": 45, "qty": 30},
}
for item, data in shop.items():
    total_value = data["price"] * data["qty"]
    print("  " + item + ": Rs." + str(data["price"]) + " x " + str(data["qty"]) + " = Rs." + str(total_value))

print()

# Key takeaway — match the structure to what you need to store and access
print("Key Takeaway:")
print("  Flat dict         → one thing with many properties")
print("  Dict of dicts     → many things, each with many properties")
print("  Dict with lists   → one thing with a collection of values")
