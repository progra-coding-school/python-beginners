# What Is a Dictionary?
# A dictionary stores data as KEY : VALUE pairs.
# Think of it like a real dictionary — you look up a WORD (key) to find its MEANING (value).
# Or like a contact book — you look up a NAME (key) to find a PHONE NUMBER (value).
# Syntax: {key: value, key: value, ...}

# Creating a dictionary — curly braces with key: value pairs
# Each key is like a label on a jar — it must be unique
student = {
    "name":   "Aarav",
    "age":    13,
    "grade":  7,
    "city":   "Chennai"
}

# Accessing a value — use the key inside square brackets
# dict["key"] looks up the key and returns its value
print("Name:", student["name"])     # Aarav
print("Age:", student["age"])       # 13
print("Grade:", student["grade"])   # 7

print()

# A dictionary can hold any type of value — strings, numbers, booleans, even lists!
profile = {
    "name":        "Diya",          # string
    "age":         12,               # integer
    "height":      4.8,              # float
    "is_enrolled": True,             # boolean
    "subjects":    ["Maths", "Science", "English"]   # list as a value!
}

print("Name:", profile["name"])
print("Subjects:", profile["subjects"])

print()

# Key vocabulary:
# {}         → curly braces — used to create a dictionary
# key        → the label used to look up data (must be unique!)
# value      → the data stored under a key
# :          → separates the key from its value
# ,          → separates each key-value pair
# dict[key]  → how you access a value

# Real-life example: a school attendance register
# Student name is the KEY, attendance status is the VALUE
attendance = {
    "Aarav":   "Present",
    "Diya":    "Absent",
    "Karthik": "Present",
    "Riya":    "Present",
}

# Loop through ALL key-value pairs using .items()
# .items() gives (key, value) pairs — one per student
for name, status in attendance.items():
    print("  " + name.ljust(10) + " : " + status)
