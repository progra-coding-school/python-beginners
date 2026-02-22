# Program Code: STR-CT-01
# Title: Spot the Bug — Find the String Mistakes!
# Cognitive Skill: Critical Thinking (Bug identification)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav wrote some programs with strings, but they have bugs.
# Can you spot the mistake in each one?
# READ the code carefully, IDENTIFY the bug, then FIX it!
# ============================================================

print("=" * 55)
print("    SPOT THE BUG — STRING EDITION!")
print("=" * 55)

print("""
For each buggy program below:
  1. Read the code carefully
  2. Find the bug
  3. Press ENTER to see the bug explained
  4. See the fixed version
""")

# -------------------------------------------------------
# BUG 1: Wrong type for concatenation
# -------------------------------------------------------
print("\n" + "=" * 40)
print("BUG 1: What's wrong here?")
print("-" * 40)
print("""
name = "Aarav"
age  = 14
message = "My name is " + name + " and I am " + age + " years old."
print(message)
""")
input("Found the bug? Press ENTER for explanation: ")
print("""
❌ BUG: 'age' is an integer. You can't use '+' to join
   a string and an integer directly.

✅ FIX: Convert age to a string first using str(age)
   OR use an f-string (cleaner!)
""")
name = "Aarav"
age  = 14
# Fixed version:
message = "My name is " + name + " and I am " + str(age) + " years old."
print(f"  Fixed output: {message}")

# -------------------------------------------------------
# BUG 2: Case-sensitive comparison
# -------------------------------------------------------
print("\n" + "=" * 40)
print("BUG 2: What's wrong here?")
print("-" * 40)
print("""
password = "Progra2026"
user_input = "progra2026"

if user_input == password:
    print("Access granted!")
else:
    print("Wrong password!")

# Output: Wrong password!   ← but the user typed it correctly...
""")
input("Found the bug? Press ENTER for explanation: ")
print("""
❌ BUG: Comparison is case-sensitive.
   "Progra2026" ≠ "progra2026"
   But the user intended the same password!

✅ FIX: Compare after converting both to lowercase
   (if case doesn't matter in your password)
""")
password   = "Progra2026"
user_input = "progra2026"
if user_input.lower() == password.lower():
    print("  Fixed: Access granted!")

# -------------------------------------------------------
# BUG 3: Index out of range
# -------------------------------------------------------
print("\n" + "=" * 40)
print("BUG 3: What's wrong here?")
print("-" * 40)
print("""
city = "Chennai"
print(city[7])    # Trying to get the 8th character
""")
input("Found the bug? Press ENTER for explanation: ")
print("""
❌ BUG: "Chennai" has 7 characters (index 0 to 6).
   Index 7 does NOT exist → IndexError!

✅ FIX: Use city[-1] for the last character,
   or city[6] for the 7th character.
""")
city = "Chennai"
print(f"  city[-1] = '{city[-1]}'   (last character)")
print(f"  city[6]  = '{city[6]}'   (7th character)")

# -------------------------------------------------------
# BUG 4: Forgetting strip() on input
# -------------------------------------------------------
print("\n" + "=" * 40)
print("BUG 4: What's wrong here?")
print("-" * 40)
print("""
# Teacher stored the correct answer
correct = "Python"

# Student typed with accidental spaces
student_answer = "Python "    # extra space at end!

if student_answer == correct:
    print("Correct!")
else:
    print("Wrong!")    # ← student gets this even though they typed Python!
""")
input("Found the bug? Press ENTER for explanation: ")
print("""
❌ BUG: "Python " (with space) ≠ "Python"
   The extra space makes them different strings!

✅ FIX: Use .strip() to remove extra spaces from input
""")
correct        = "Python"
student_answer = "Python "
if student_answer.strip() == correct:
    print("  Fixed: Correct! ✅")

print("\n" + "=" * 55)
print("  BUGS SPOTTED:")
print("  1. str() needed when joining int with string")
print("  2. Case-sensitive comparison → use .lower()")
print("  3. Index out of range → check valid indexes")
print("  4. Spaces in input → use .strip()")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. Which bug was hardest to spot? Why?
# 2. How do you avoid Bug 4 in real programs?
# 3. Write a buggy string program and challenge a classmate!
# ============================================================
