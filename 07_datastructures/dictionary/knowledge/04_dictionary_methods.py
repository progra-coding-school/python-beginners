# Dictionary Methods
# Python gives you built-in methods to explore and modify dictionaries.
# The most important: .keys() .values() .items() .get() .update() .pop() .clear()
# Choosing the right method makes your code shorter and safer.

student = {
    "name":    "Aarav",
    "age":     13,
    "grade":   7,
    "city":    "Chennai",
    "school":  "Progra School",
}

# .keys() — returns all the keys (the labels)
# Use when you only need to know what keys exist in the dictionary
print("Keys:", student.keys())
for key in student.keys():
    print("  Key:", key)

print()

# .values() — returns all the values (the data)
# Use when you only need the data, not the labels
print("Values:", student.values())
for value in student.values():
    print("  Value:", value)

print()

# .items() — returns all (key, value) pairs as tuples
# This is the MOST USEFUL loop — you get both key and value at the same time
print("Items:", student.items())
for key, value in student.items():
    print("  " + str(key) + " →", value)

print()

# .get(key, default) — safe access, never crashes even if key is missing
print(student.get("name"))          # Aarav
print(student.get("marks"))         # None  (key missing, no error)
print(student.get("marks", "N/A"))  # N/A   (custom default returned)

print()

# .update(other_dict) — adds new keys and overwrites existing ones from another dict
extras = {"marks": 87, "grade": 8}
student.update(extras)   # grade goes from 7 to 8; marks is new
print("After update:", student)

print()

# .pop(key) — removes a key and returns its value in one step
grade = student.pop("grade")
print("Popped grade:", grade)
print("After pop:", student)

print()

# .clear() — removes everything, makes the dictionary empty
temp = {"x": 1, "y": 2}
temp.clear()
print("After clear:", temp)   # {}

print()

# len() — counts the number of key-value pairs (not a method, but a built-in function)
print("Number of items:", len(student))

print()

# Quick reference — all the methods in one place
print("Dictionary Methods Summary:")
print("  .keys()          → all keys")
print("  .values()        → all values")
print("  .items()         → all (key, value) pairs")
print("  .get(k, default) → safe access")
print("  .update(dict)    → merge/overwrite")
print("  .pop(key)        → remove and return")
print("  .clear()         → remove everything")
print("  len(dict)        → count of pairs")
