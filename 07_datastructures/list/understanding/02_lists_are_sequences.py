# Program Code: LIST-UN-02
# Title: Lists are Sequences — Every Item Has an Address!
# Cognitive Skill: Understanding (Deepening the concept)
# Topic: Lists in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav lives in a big apartment building.
# Every flat has a number — Flat 0, Flat 1, Flat 2...
# If someone says "go to Flat 3", you know exactly where to go!
#
# A Python LIST works the same way.
# Every item in a list has a NUMBER called an INDEX.
# The index is the item's ADDRESS inside the list.
#
# Let's learn how to use these addresses to access,
# understand, and navigate a list like a pro!
# ============================================================

print("=" * 55)
print("   LISTS ARE SEQUENCES — EVERY ITEM HAS AN ADDRESS!")
print("=" * 55)

# ============================================================
# THE APARTMENT BUILDING ANALOGY
# ============================================================

print("""
ANALOGY: Aarav's Apartment Building
--------------------------------------
Imagine a building with 5 flats in a row.
Each flat has a FLAT NUMBER starting from 0 (not 1!).

  Flat 0    Flat 1    Flat 2    Flat 3    Flat 4
 +--------+---------+---------+---------+---------+
 | Aarav  |  Diya   |  Kabir  |  Meera  |  Rohan  |
 +--------+---------+---------+---------+---------+

A Python list is exactly like this building.
Each item sits in a numbered slot called an INDEX.
The INDEX always starts at 0, not 1!
""")

# ============================================================
# PART 1: POSITIVE INDEXING (Left to Right, starting at 0)
# ============================================================

print("=" * 55)
print("   PART 1: POSITIVE INDEXING (Left → Right)")
print("=" * 55)

student_names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]

# -----------------------------------------------------------
# ASCII Diagram of the list with positive index positions
# -----------------------------------------------------------
print("\nOur list:")
print()
print("  +----------+----------+----------+----------+----------+")
print('  | "Aarav"  |  "Diya"  | "Kabir"  | "Meera"  | "Rohan"  |')
print("  +----------+----------+----------+----------+----------+")
print("       0          1          2          3          4        ← Positive Index")
print()
print("  The FIRST item is always at index 0 (not 1!)")
print("  The LAST item  is always at index: len(list) - 1")
print()

# -----------------------------------------------------------
# Accessing items using positive index
# -----------------------------------------------------------
print("-" * 40)
print("Accessing Items with Positive Index:")
print("-" * 40)

print(f"  student_names[0] = '{student_names[0]}'   → First student")
print(f"  student_names[1] = '{student_names[1]}'    → Second student")
print(f"  student_names[2] = '{student_names[2]}'   → Third student")
print(f"  student_names[3] = '{student_names[3]}'   → Fourth student")
print(f"  student_names[4] = '{student_names[4]}'   → Fifth (last) student")

# ============================================================
# PART 2: NEGATIVE INDEXING (Right to Left, starting at -1)
# ============================================================

print("\n" + "=" * 55)
print("   PART 2: NEGATIVE INDEXING (Right → Left)")
print("=" * 55)

print("""
Python also lets you count FROM THE END using negative numbers.
This is super useful when you want the LAST item quickly!
""")

# -----------------------------------------------------------
# ASCII Diagram with BOTH positive and negative indices
# -----------------------------------------------------------
print("Full index map for our list:")
print()
print("  +----------+----------+----------+----------+----------+")
print('  | "Aarav"  |  "Diya"  | "Kabir"  | "Meera"  | "Rohan"  |')
print("  +----------+----------+----------+----------+----------+")
print("       0          1          2          3          4        ← Positive Index")
print("      -5         -4         -3         -2         -1        ← Negative Index")
print()
print("  -1  always means the LAST item")
print("  -2  means second from the end")
print("  -len(list) means the FIRST item (from the back)")
print()

# -----------------------------------------------------------
# Accessing items using negative index
# -----------------------------------------------------------
print("-" * 40)
print("Accessing Items with Negative Index:")
print("-" * 40)

print(f"  student_names[-1] = '{student_names[-1]}'   → Last student")
print(f"  student_names[-2] = '{student_names[-2]}'   → Second from last")
print(f"  student_names[-3] = '{student_names[-3]}'   → Third from last")
print(f"  student_names[-4] = '{student_names[-4]}'    → Fourth from last")
print(f"  student_names[-5] = '{student_names[-5]}'   → First student (from back)")

# -----------------------------------------------------------
# Handy trick: Get first and last without knowing the length
# -----------------------------------------------------------
print("\n--- Handy Trick: First and Last Item ---")
first_student = student_names[0]
last_student  = student_names[-1]
print(f"  First student : student_names[0]  = '{first_student}'")
print(f"  Last student  : student_names[-1] = '{last_student}'")
print("  Note: [-1] works no matter how long the list is!")

# ============================================================
# PART 3: WHAT HAPPENS WITH AN INVALID INDEX?
# ============================================================

print("\n" + "=" * 55)
print("   PART 3: WHAT IF THE INDEX DOESN'T EXIST?")
print("=" * 55)

print(f"""
Our list has {len(student_names)} students.
Valid positive indices: 0 to {len(student_names) - 1}
Valid negative indices: -{len(student_names)} to -1

What if Aarav tries to visit Flat 10 in a 5-flat building?
There IS no Flat 10! Python raises an IndexError.
""")

# -----------------------------------------------------------
# Demonstrate IndexError safely using try-except
# -----------------------------------------------------------
print("-" * 40)
print("Trying student_names[10] on a 5-item list:")
print("-" * 40)

try:
    invalid_access = student_names[10]    # Index 10 does not exist!
except IndexError as error_message:
    print(f"  ERROR caught: {error_message}")
    print("  Python says: There is no item at index 10!")
    print("  Valid range is 0 to 4 (or -5 to -1).")

print()

print("-" * 40)
print("Trying student_names[-10] on a 5-item list:")
print("-" * 40)

try:
    invalid_negative_access = student_names[-10]    # -10 is also out of range
except IndexError as error_message:
    print(f"  ERROR caught: {error_message}")
    print("  Negative index -10 is also out of range for a 5-item list!")

# ============================================================
# PART 4: len() AND THE VALID INDEX RANGE
# ============================================================

print("\n" + "=" * 55)
print("   PART 4: len() AND VALID INDEX RANGE")
print("=" * 55)

list_length = len(student_names)

print(f"\n  List             : {student_names}")
print(f"  Number of items  : len(student_names) = {list_length}")
print()
print("  Valid Positive Indices:")
print(f"    Smallest → 0")
print(f"    Largest  → len(list) - 1  =  {list_length} - 1  =  {list_length - 1}")
print()
print("  Valid Negative Indices:")
print(f"    Smallest → -len(list)  =  -{list_length}")
print(f"    Largest  → -1")
print()

# -----------------------------------------------------------
# Show every item with its positive AND negative index
# -----------------------------------------------------------
print("-" * 40)
print("All items with both index styles:")
print("-" * 40)
print(f"  {'Positive Index':<18} {'Negative Index':<18} {'Item'}")
print(f"  {'-'*15:<18} {'-'*15:<18} {'-'*10}")

for positive_index in range(list_length):
    negative_index = positive_index - list_length
    item_value     = student_names[positive_index]
    print(f"  {positive_index:<18} {negative_index:<18} '{item_value}'")

# ============================================================
# REAL-WORLD EXAMPLE: Cricket Team Batting Order
# ============================================================

print("\n" + "=" * 55)
print("   REAL-WORLD: Cricket Team Batting Order")
print("=" * 55)

batting_order = ["Rohit", "Shubman", "Virat", "KL Rahul", "Hardik",
                 "Jadeja", "Pant", "Ashwin", "Bumrah", "Siraj", "Mohammed"]

print(f"\n  Batting order : {batting_order}")
print(f"  Total players : {len(batting_order)}")
print()
print(f"  Opening batsman (index 0)   : {batting_order[0]}")
print(f"  Number 3 batsman (index 2)  : {batting_order[2]}")
print(f"  Last batsman (index -1)     : {batting_order[-1]}")
print(f"  Second-last (index -2)      : {batting_order[-2]}")

print()
print("  Printing the top 3 batsmen:")
for position in range(3):
    print(f"    Position {position + 1}: {batting_order[position]}")

print("\n" + "=" * 55)
print("   KEY IDEAS")
print("=" * 55)
print("""
  - A list is a SEQUENCE — items are stored IN ORDER
  - Each item has an INDEX (its address in the list)
  - Positive index: starts at 0 from the LEFT
  - Negative index: starts at -1 from the RIGHT
  - Valid range:  0  to  len-1  (positive)
                 -1  to  -len   (negative)
  - Going outside this range → IndexError!
  - Use [-1] to always get the last item, no matter the size
""")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. A list has 8 items. What is the valid range of positive
#    indices? What is the valid range of negative indices?
# 2. Why does Python start counting from 0 instead of 1?
#    (Hint: think about how computers store memory in slots.)
# 3. You have a list of 20 cricket players. How would you
#    access the last player using a negative index?
#    Would you rather use index 19 or index -1? Why?
# 4. What error does Python raise when you use an index that
#    is out of range? How can you handle it safely in code?
# ============================================================
