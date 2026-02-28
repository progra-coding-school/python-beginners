# Program Code: DC-KN-04
# Title: Dictionary Methods
# Cognitive Skill: Knowledge
# Topic: Dictionaries in Python

student = {
    "name":    "Aarav",
    "age":     13,
    "grade":   7,
    "city":    "Chennai",
    "school":  "Progra School",
}

# --- .keys() — all keys ---
print("Keys:", student.keys())
# Loop through keys
for key in student.keys():
    print(f"  Key: {key}")

print()

# --- .values() — all values ---
print("Values:", student.values())
# Loop through values
for value in student.values():
    print(f"  Value: {value}")

print()

# --- .items() — all key-value pairs as tuples ---
print("Items:", student.items())
# Loop through key-value pairs (most useful!)
for key, value in student.items():
    print(f"  {key} → {value}")

print()

# --- .get(key, default) — safe access ---
print(student.get("name"))          # Aarav
print(student.get("marks"))         # None (key missing, no error)
print(student.get("marks", "N/A"))  # N/A (custom default)

print()

# --- .update(other_dict) — add or overwrite from another dict ---
extras = {"marks": 87, "grade": 8}
student.update(extras)
print("After update:", student)

print()

# --- .pop(key) — remove and return a value ---
grade = student.pop("grade")
print("Popped grade:", grade)
print("After pop:", student)

print()

# --- .clear() — remove ALL items ---
temp = {"x": 1, "y": 2}
temp.clear()
print("After clear:", temp)

print()

# --- len() — number of key-value pairs ---
print("Number of items:", len(student))

print()

# --- Summary Table ---
print("=== Dictionary Methods Summary ===")
print("  .keys()          → all keys")
print("  .values()        → all values")
print("  .items()         → all (key, value) pairs")
print("  .get(k, default) → safe access")
print("  .update(dict)    → merge/overwrite")
print("  .pop(key)        → remove and return")
print("  .clear()         → remove everything")
print("  len(dict)        → count of pairs")
