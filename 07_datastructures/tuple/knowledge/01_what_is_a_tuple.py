# Program Code: TU-KN-01
# Title: What Is a Tuple?
# Cognitive Skill: Knowledge
# Topic: Tuples in Python

# A TUPLE is a collection that is:
#   1. ORDERED    — items have a fixed position (index 0, 1, 2 ...)
#   2. IMMUTABLE  — once created, it CANNOT be changed
#   3. ALLOWS DUPLICATES — same value can appear more than once

# --- Creating a tuple with () ---
colours = ("red", "green", "blue")
print("Colours tuple:", colours)
print("Type:", type(colours))

print()

# --- Tuple with different data types ---
student = ("Aarav", 13, 7, True)     # name, age, grade, active
print("Student:", student)

print()

# --- Single-item tuple — needs a trailing comma! ---
single_wrong = ("hello")        # this is just a string
single_right = ("hello",)       # this is a tuple

print("type('hello')  :", type(single_wrong))   # <class 'str'>
print("type('hello',) :", type(single_right))   # <class 'tuple'>

print()

# --- Tuple without parentheses (tuple packing) ---
point = 10, 20          # parentheses are optional when packing
print("Point tuple:", point)
print("Type:", type(point))

print()

# --- Real-life analogy ---
print("=== Real-life analogy ===")
print("Think of a tuple like a SEALED ENVELOPE.")
print("Once you seal it, you can READ the contents but not CHANGE them.")
print("A student's date of birth — it never changes → perfect for a tuple!")
print()

dob = (15, 8, 2012)    # day, month, year
print("Date of birth:", dob)

# Think:
# 1. Why would you store coordinates (x, y) as a tuple rather than a list?
# 2. What happens if you try to do colours[0] = 'yellow'? Try it!
