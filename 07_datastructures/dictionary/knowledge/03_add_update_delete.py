# Program Code: DC-KN-03
# Title: Add, Update, and Delete
# Cognitive Skill: Knowledge
# Topic: Dictionaries in Python

student = {
    "name":  "Aarav",
    "age":   13,
    "grade": 7,
}
print("Original:", student)

# --- ADD a new key-value pair ---
# Just assign to a key that doesn't exist yet
student["city"]   = "Chennai"
student["school"] = "Progra School"
print("After adding:", student)

print()

# --- UPDATE an existing value ---
# Assign to a key that already exists
student["age"]   = 14          # birthday!
student["grade"] = 8           # promoted!
print("After updating:", student)

print()

# --- DELETE a key-value pair ---

# Method 1: del — removes the key, gives nothing back
del student["school"]
print("After del school:", student)

# Method 2: .pop() — removes AND returns the deleted value
removed_city = student.pop("city")
print("Removed city:", removed_city)
print("After pop:", student)

# Method 3: .pop() with a default — safe even if key missing
result = student.pop("address", "Not found")
print("Pop missing key:", result)      # Not found — no error

print()

# --- CLEAR all items ---
temp = {"a": 1, "b": 2}
temp.clear()
print("After clear:", temp)   # {}

print()

# --- UPDATE / MERGE with another dictionary ---
contact = {"name": "Aarav", "age": 14}
extra   = {"email": "aarav@progra.com", "phone": "9876543210"}
contact.update(extra)
print("After update/merge:", contact)

# .update() also overwrites existing keys
contact.update({"age": 15})
print("After updating age:", contact)

# Think:
# 1. What is the difference between del and .pop()?
# 2. If you .update() with a key that already exists, what happens?
