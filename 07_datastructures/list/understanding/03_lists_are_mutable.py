# Program Code: LIST-UN-03
# Title: Lists are Mutable — They Can Change!
# Cognitive Skill: Understanding (Deepening the concept)
# Topic: Lists in Python

# ============================================================
# PROBLEM STATEMENT:
# Diya gets a new school ID card every year.
# Once it is PRINTED, you cannot erase and rewrite her name
# — you would need to print a BRAND NEW card.
#
# Strings in Python work the same way — once created,
# you cannot change them directly. They are IMMUTABLE.
#
# But a WHITEBOARD is different!
# Diya can write her name, erase it, rewrite it, add more
# text, clear a section — all on the SAME board.
#
# Python LISTS work like a whiteboard — you can change them
# freely at any time. This is called MUTABILITY.
#
# Let's understand the difference deeply!
# ============================================================

print("=" * 55)
print("   LISTS ARE MUTABLE — THEY CAN CHANGE!")
print("=" * 55)

print("""
  ANALOGY:
  String → Printed ID card    (locked, cannot edit directly)
  List   → Whiteboard         (open, can update anytime!)
""")

# ============================================================
# PART 1: STRINGS ARE IMMUTABLE — Cannot Change Directly
# ============================================================

print("=" * 55)
print("   PART 1: STRINGS ARE IMMUTABLE (The ID Card)")
print("=" * 55)

print("""
Diya's ID card has her name printed as "diya" (lowercase typo).
She wants to fix just the first letter: 'd' → 'D'.
Can she change it directly on the card? NO!
""")

student_name_string = "diya"
print(f"  student_name_string = '{student_name_string}'")
print()
print("  Trying: student_name_string[0] = 'D'")
print()

try:
    student_name_string[0] = "D"       # Attempt to change one character
except TypeError as error_message:
    print(f"  ERROR: {error_message}")
    print("  Python does NOT allow changing characters in a string!")
    print("  Strings are IMMUTABLE — carved in stone once created.")

print()
print("  The RIGHT way: Create a new corrected string instead.")
corrected_name = "D" + student_name_string[1:]     # New string built from parts
print(f"  corrected_name = 'D' + student_name_string[1:] = '{corrected_name}'")
print("  (The original string 'diya' was never changed. A NEW string was made.)")

# ============================================================
# PART 2: LISTS ARE MUTABLE — Change Freely!
# ============================================================

print("\n" + "=" * 55)
print("   PART 2: LISTS ARE MUTABLE (The Whiteboard)")
print("=" * 55)

print("""
Kabir's class whiteboard shows the student roster.
He can UPDATE names, ADD new students, and REMOVE names.
All on the SAME list — no need to create a new one!
""")

class_roster = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
print(f"  Initial roster : {class_roster}")
print()

# -----------------------------------------------------------
# UPDATE: Change an existing item
# -----------------------------------------------------------
print("-" * 40)
print("Update: 'Kabir' transferred — 'Priya' joins in his place")
print("-" * 40)

class_roster[2] = "Priya"              # Change item at index 2
print(f"  After update   : {class_roster}")
print("  (The list itself changed — no new variable needed!)")

# -----------------------------------------------------------
# ADD: Append a new item to the end
# -----------------------------------------------------------
print("\n" + "-" * 40)
print("Add: 'Arjun' joins the class today")
print("-" * 40)

class_roster.append("Arjun")           # Add to the end
print(f"  After append   : {class_roster}")
print(f"  New length     : {len(class_roster)}")

# -----------------------------------------------------------
# INSERT: Add item at a specific position
# -----------------------------------------------------------
print("\n" + "-" * 40)
print("Insert: 'Kavya' joins — she sits at position 1")
print("-" * 40)

class_roster.insert(1, "Kavya")        # Insert at index 1, shift rest right
print(f"  After insert   : {class_roster}")

# -----------------------------------------------------------
# REMOVE: Remove a specific item by value
# -----------------------------------------------------------
print("\n" + "-" * 40)
print("Remove: 'Rohan' left the school")
print("-" * 40)

class_roster.remove("Rohan")           # Remove first occurrence of "Rohan"
print(f"  After remove   : {class_roster}")
print(f"  New length     : {len(class_roster)}")

# -----------------------------------------------------------
# POP: Remove item at a specific index
# -----------------------------------------------------------
print("\n" + "-" * 40)
print("Pop: Remove the last student from the list")
print("-" * 40)

removed_student = class_roster.pop()   # Removes and returns the last item
print(f"  Removed        : '{removed_student}'")
print(f"  After pop      : {class_roster}")

print("\n  --> All of this happened on the SAME list variable!")
print("      No new variable. The list was updated in place.")

# ============================================================
# PART 3: THE SHARED REFERENCE TRAP
# ============================================================

print("\n" + "=" * 55)
print("   PART 3: THE SHARED REFERENCE TRAP")
print("=" * 55)

print("""
IMPORTANT: When you assign one list variable to another,
you are NOT creating a copy — you are creating a SECOND
LABEL pointing to the SAME list in memory!

Think of it like two keys to the same locker.
If someone uses Key A to change what's inside, Key B
will also see the change — because it's the SAME locker!
""")

# -----------------------------------------------------------
# Show that both variables point to the same list object
# -----------------------------------------------------------
print("-" * 40)
print("Assigning: team_b = team_a (NOT a copy!)")
print("-" * 40)

team_a = ["Aarav", "Diya", "Meera"]
team_b = team_a                        # team_b is just another label for team_a

print(f"  team_a = {team_a}")
print(f"  team_b = {team_b}  (same list, different name)")
print()

# Change via team_b — both will reflect the change!
team_b.append("Rohan")

print(f"  After team_b.append('Rohan'):")
print(f"  team_b = {team_b}")
print(f"  team_a = {team_a}   <-- team_a ALSO changed!")
print()
print("  WHY? Because team_a and team_b both point to the SAME list.")
print("  Changing through one label changes the actual list.")
print("  So the other label sees the change too!")

# -----------------------------------------------------------
# Confirm with Python's id() — same object in memory
# -----------------------------------------------------------
print()
print(f"  id(team_a) = {id(team_a)}")
print(f"  id(team_b) = {id(team_b)}")
if id(team_a) == id(team_b):
    print("  Both ids are IDENTICAL → same object in memory!")

# ============================================================
# PART 4: HOW TO MAKE A PROPER COPY
# ============================================================

print("\n" + "=" * 55)
print("   PART 4: MAKING A REAL COPY OF A LIST")
print("=" * 55)

print("""
To work with an INDEPENDENT copy of a list, use:
  Method 1: list.copy()     → clean and explicit
  Method 2: list[:]         → slicing trick, same result

Both create a brand-new list with the same items.
Changes to the copy will NOT affect the original.
""")

original_squad = ["Aarav", "Diya", "Kabir"]

# -----------------------------------------------------------
# Method 1: .copy()
# -----------------------------------------------------------
print("-" * 40)
print("Method 1: copied_squad = original_squad.copy()")
print("-" * 40)

copied_squad = original_squad.copy()
copied_squad.append("Meera")           # Add only to the copy

print(f"  original_squad = {original_squad}   (unchanged!)")
print(f"  copied_squad   = {copied_squad}")
print(f"  id(original)   = {id(original_squad)}")
print(f"  id(copy)       = {id(copied_squad)}")
print("  Different ids → these are TWO SEPARATE lists now!")

# -----------------------------------------------------------
# Method 2: Slicing [:]
# -----------------------------------------------------------
print("\n" + "-" * 40)
print("Method 2: sliced_squad = original_squad[:]")
print("-" * 40)

sliced_squad = original_squad[:]       # Full slice = complete copy
sliced_squad.remove("Diya")           # Remove only from the copy

print(f"  original_squad = {original_squad}   (unchanged!)")
print(f"  sliced_squad   = {sliced_squad}")
print("  Slicing also creates an independent copy!")

# ============================================================
# SUMMARY: String vs List
# ============================================================

print("\n" + "=" * 55)
print("   SUMMARY: STRING vs LIST")
print("=" * 55)
print()
print(f"  {'Feature':<30} {'String':<20} {'List'}")
print(f"  {'-'*27:<30} {'-'*17:<20} {'-'*17}")
print(f"  {'Can change an item directly?':<30} {'NO (Immutable)':<20} {'YES (Mutable)'}")
print(f"  {'Can append new items?':<30} {'NO':<20} {'YES (append)'}")
print(f"  {'Can remove items?':<30} {'NO':<20} {'YES (remove/pop)'}")
print(f"  {'Analogy':<30} {'Printed ID card':<20} {'Whiteboard'}")
print()
print("  String is CARVED IN STONE.")
print("  List is WRITTEN ON A WHITEBOARD.")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. Aarav writes: friends = ["Diya", "Kabir"]
#                  backup  = friends
#                  backup.append("Rohan")
#    What does friends look like now? Why?
# 2. What is the difference between friends.copy() and
#    just writing backup = friends?
# 3. If strings are immutable, how does this code work:
#    name = "Aarav"
#    name = name.upper()
#    Is the original string "Aarav" changed? Explain.
# 4. Give one real-life situation where you would WANT both
#    variables to share the same list, and one situation
#    where you would NEED a separate copy.
# ============================================================
