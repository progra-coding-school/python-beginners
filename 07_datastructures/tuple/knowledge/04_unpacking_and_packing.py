# Program Code: TU-KN-04
# Title: Unpacking and Packing
# Cognitive Skill: Knowledge
# Topic: Tuples in Python

# Packing: bundling multiple values INTO a tuple
# Unpacking: pulling values OUT of a tuple into variables

# --- Packing ---
print("=== Packing ===")
student = "Aarav", 13, 7           # packs into a tuple automatically
print("Packed:", student)
print("Type  :", type(student))

print()

# --- Unpacking ---
print("=== Unpacking ===")
name, age, grade = student          # exactly 3 variables for 3 items
print("Name :", name)
print("Age  :", age)
print("Grade:", grade)

print()

# --- Unpacking coordinates ---
print("=== Coordinate unpacking ===")
point = (10, 25)
x, y  = point
print(f"x = {x}, y = {y}")

print()

# --- Swap using tuple packing/unpacking ---
print("=== Classic swap ===")
a, b = 100, 200
print(f"Before: a={a}, b={b}")
a, b = b, a              # Python uses tuple packing/unpacking under the hood
print(f"After : a={a}, b={b}")

print()

# --- Star (*) unpacking — collect the rest ---
print("=== Star unpacking ===")
scores = (85, 92, 78, 66, 90, 74)
first, *middle, last = scores
print("First  :", first)
print("Middle :", middle)    # list of everything between first and last
print("Last   :", last)

print()

# --- Ignore values with _ ---
print("=== Ignoring values ===")
record = ("Aarav", 13, "Chennai", "Grade 7")
name, _, city, _ = record          # _ means "I don't need this"
print(f"Name: {name}, City: {city}")

print()

# --- Returning multiple values from a function ---
print("=== Function returning multiple values ===")
def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple

low, high = min_max([45, 12, 89, 34, 67])
print(f"Min: {low}, Max: {high}")

# Think:
# 1. What happens if you have 3 variables but try to unpack a 4-item tuple?
# 2. How does a, b = b, a work without a temp variable? What is Python doing?
