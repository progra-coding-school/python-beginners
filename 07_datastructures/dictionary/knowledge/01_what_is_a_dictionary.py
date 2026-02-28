# Program Code: DC-KN-01
# Title: What Is a Dictionary?
# Cognitive Skill: Knowledge
# Topic: Dictionaries in Python

# A dictionary stores data as KEY : VALUE pairs.
# Think of it like a real dictionary — you look up a WORD (key) to find its MEANING (value).
# Or like a contact book — you look up a NAME (key) to find a PHONE NUMBER (value).

# --- Creating a dictionary ---
student = {
    "name":   "Aarav",
    "age":    13,
    "grade":  7,
    "city":   "Chennai"
}

# --- Accessing a value by its KEY ---
print(student["name"])     # Aarav
print(student["age"])      # 13
print(student["grade"])    # 7

print()

# --- A dictionary can hold different types of values ---
profile = {
    "name":        "Diya",          # string
    "age":         12,               # integer
    "height":      4.8,              # float
    "is_enrolled": True,             # boolean
    "subjects":    ["Maths", "Science", "English"]   # list!
}

print(profile["name"])
print(profile["subjects"])

print()

# --- Key vocabulary ---
# {}         → curly braces — used to create a dictionary
# key        → the label used to look up data (must be unique!)
# value      → the data stored under a key
# :          → separates the key from its value
# ,          → separates each key-value pair
# dict[key]  → how you access a value

# --- Real-life analogy ---
# A school attendance register:
attendance = {
    "Aarav":   "Present",
    "Diya":    "Absent",
    "Karthik": "Present",
    "Riya":    "Present",
}

for name, status in attendance.items():
    print(f"  {name:10} : {status}")

# Think:
# 1. What real-world "dictionaries" (key→value lookups) do you use every day?
# 2. Why must keys be UNIQUE in a dictionary?
