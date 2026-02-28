# Program Code: STR-UN-01
# Title: Strings Are Sequences — Every Letter Has an Address!
# Cognitive Skill: Understanding (Deepening the concept)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Imagine a row of lockers in school.
# Each locker has a NUMBER (address) starting from 0.
# A string works the SAME WAY!
# Each character in a string has a POSITION called an INDEX.
# Let's understand why this matters and how to use it!
# ============================================================

print("=" * 55)
print("   STRINGS ARE SEQUENCES — EVERY LETTER HAS A SPOT!")
print("=" * 55)

# -------------------------------------------------------
# VISUALISING A STRING AS A SEQUENCE
# -------------------------------------------------------
name = "AARAV"

print("\nString: '" + name + "'")
print("\nThink of it like lockers:")
print()
print("  +---+---+---+---+---+")
print("  | A | A | R | A | V |")
print("  +---+---+---+---+---+")
print("    0   1   2   3   4   ← INDEX (position number)")
print()
print("  The first locker is ALWAYS number 0 (not 1!)")

# -------------------------------------------------------
# ACCESSING CHARACTERS USING INDEX
# -------------------------------------------------------
print("\n--- Accessing Characters by Index ---")

print("name[0] = '" + name[0] + "'  → First character")
print("name[1] = '" + name[1] + "'  → Second character")
print("name[2] = '" + name[2] + "'  → Third character")
print("name[3] = '" + name[3] + "'  → Fourth character")
print("name[4] = '" + name[4] + "'  → Fifth (last) character")

# -------------------------------------------------------
# EXPERIMENT: Print each character one by one
# -------------------------------------------------------
print("\n--- Printing '" + name + "' character by character ---")
print("Character at 0 : " + name[0])
print("Character at 1 : " + name[1])
print("Character at 2 : " + name[2])
print("Character at 3 : " + name[3])
print("Character at 4 : " + name[4])

# -------------------------------------------------------
# REAL USE: Get the first letter of a name
# -------------------------------------------------------
print("\n--- Real Use: Initials Generator ---")

first_name = "Aarav"
last_name  = "Sharma"

initial_f = first_name[0]    # First letter of first name
initial_l = last_name[0]     # First letter of last name

initials = initial_f + "." + initial_l + "."
print("Name     : " + first_name + " " + last_name)
print("Initials : " + initials)

# -------------------------------------------------------
# REAL USE: Check first character
# -------------------------------------------------------
print("\n--- Check if Name Starts with 'A' ---")

student = "Aarav"
if student[0] == "A":
    print("'" + student + "' starts with A — Team Alpha!")
else:
    print("'" + student + "' is in a different team.")

# -------------------------------------------------------
# UNDERSTANDING: Strings have a fixed length
# -------------------------------------------------------
print("\n--- Length and Valid Index Range ---")
word = "Python"
print("String : '" + word + "'")
print("Length :", len(word))
print("Valid indexes : 0 to", len(word) - 1)
print("  First char : word[0]           = '" + word[0] + "'")
print("  Last char  : word[5]           = '" + word[5] + "'")
print("  Last char  : word[len(word)-1] = '" + word[len(word)-1] + "'")

print("\n" + "=" * 55)
print("  KEY IDEA: Strings are sequences.")
print("  Each character has an index starting from 0.")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. What is the index of 'R' in "AARAV"?
# 2. If a string has 7 characters, what is the last valid index?
# 3. What happens if you try "AARAV"[10]? Try it!
# 4. How would you print just the first 3 characters of "Chennai"?
# ============================================================
