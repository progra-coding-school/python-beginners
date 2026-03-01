# Add, Update, and Delete — Modifying a Dictionary
# Dictionaries are mutable — you can change them after creation.
# Same syntax for adding AND updating: dict[key] = value
#   If the key is NEW → it gets added.
#   If the key EXISTS → its value gets overwritten.

student = {
    "name":  "Aarav",
    "age":   13,
    "grade": 7,
}
print("Original:", student)

# Adding new key-value pairs — just assign to a key that doesn't exist yet
# Python automatically adds the new key
student["city"]   = "Chennai"
student["school"] = "Progra School"
print("After adding:", student)

print()

# Updating existing values — same assignment syntax, but the key already exists
# The old value is replaced immediately by the new one
student["age"]   = 14          # birthday!
student["grade"] = 8           # promoted!
print("After updating:", student)

print()

# Deleting a key-value pair — two methods with different purposes

# Method 1: del — removes the key permanently, returns NOTHING
# Use when you just want to delete and don't need the old value
del student["school"]
print("After del school:", student)

# Method 2: .pop() — removes AND returns the deleted value in one step
# Use when you want to SAVE the value before deleting it
removed_city = student.pop("city")
print("Removed city:", removed_city)
print("After pop:", student)

# .pop() with a default — safe even if key doesn't exist (avoids KeyError)
result = student.pop("address", "Not found")
print("Pop missing key:", result)      # Not found — no error

print()

# .clear() — removes ALL items at once, leaving an empty dictionary
temp = {"a": 1, "b": 2}
temp.clear()
print("After clear:", temp)   # {}

print()

# .update() — adds OR overwrites multiple keys at once from another dictionary
# Like doing several assignments in one line
contact = {"name": "Aarav", "age": 14}
extra   = {"email": "aarav@progra.com", "phone": "9876543210"}
contact.update(extra)            # adds email and phone (new keys)
print("After update/merge:", contact)

contact.update({"age": 15})      # overwrites existing age
print("After updating age:", contact)
