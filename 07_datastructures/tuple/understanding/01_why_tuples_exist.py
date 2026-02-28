# Program Code: TU-UN-01
# Title: Why Tuples Exist
# Cognitive Skill: Understanding
# Topic: Tuples in Python

# Tuples exist to represent DATA THAT SHOULD NOT CHANGE.
# They signal intent: "this is fixed — don't modify it."

# --- Problem: accidental modification ---
print("=== Problem with a list — can be modified accidentally ===")

# Using a list for a date of birth
dob_list = [15, 8, 2012]
print("Original DOB:", dob_list)

# Somewhere later in a big program...
dob_list[2] = 2013    # accident! birth year changed
print("After accident:", dob_list)    # data is now wrong!

print()

print("=== With a tuple — modification is impossible ===")
dob_tuple = (15, 8, 2012)
try:
    dob_tuple[2] = 2013     # TypeError — tuples are immutable
except TypeError as e:
    print("TypeError:", e)
print("Tuple unchanged:", dob_tuple)    # still correct

print()

# --- Tuples as dictionary keys ---
print("=== Tuples can be dict keys; lists cannot ===")
# Real use: GPS map — location (lat, lon) → place name

locations = {
    (13.0827, 80.2707): "Chennai",
    (12.9716, 77.5946): "Bengaluru",
    (17.3850, 78.4867): "Hyderabad",
}

point = (13.0827, 80.2707)
print("Location:", locations[point])

# Lists would cause TypeError here
try:
    bad = {[13.0827, 80.2707]: "Chennai"}
except TypeError as e:
    print("List as key — TypeError:", e)

print()

# --- Semantic clarity: tuple signals "this is a fixed record" ---
print("=== Semantic meaning of tuples ===")
# A student RECORD — name + age + grade is a fixed snapshot
student_record = ("Aarav", 13, 7)
print("Student record (immutable snapshot):", student_record)

# A shopping cart CONTENTS — can change
cart = ["mango", "banana", "apple"]
cart.append("grapes")
print("Shopping cart (mutable list):", cart)

print()
print("=== 3 Reasons Tuples Exist ===")
print("1. IMMUTABILITY  — protect data that must not change")
print("2. DICT KEYS     — hashable, so usable as dictionary keys")
print("3. MULTIPLE RETURNS — functions naturally return tuples")

# Think:
# 1. Name 3 real-life values that should NEVER change (good tuple candidates).
# 2. If tuples can't be changed, how would you "update" a tuple value?
