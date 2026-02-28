# Program Code: STR-KN-04
# Title: String Operations — Add, Repeat, Check, Measure!
# Cognitive Skill: Knowledge (Acquiring the concept)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav's Progra class is building a scoreboard display.
# They need to:
#   - Join (add) text together to make a full name or sentence
#   - Repeat a pattern to create a border
#   - Check if a player's name is in the team list
#   - Find out how long a string is
# Let's learn the 4 KEY OPERATIONS on strings!
# ============================================================

print("=" * 55)
print("    4 KEY STRING OPERATIONS IN PYTHON")
print("=" * 55)

# -------------------------------------------------------
# OPERATION 1: Concatenation (+) — Joining strings
# Think of it like gluing two pieces of text together
# -------------------------------------------------------
print("\n--- OPERATION 1: Concatenation (+) ---")

first_name = "Aarav"
last_name  = "Sharma"
full_name  = first_name + " " + last_name   # Space in between!

print("First name  : " + first_name)
print("Last name   : " + last_name)
print("Full name   : " + full_name)

# Real use: Building a greeting message
city     = "Chennai"
greeting = "Vanakkam from " + city + "!"
print("Greeting    : " + greeting)

# ⚠️ IMPORTANT: You can only add string + string
# ❌ WRONG:  "Age: " + 14       → Error! (14 is a number, not a string)
# ✅ RIGHT:  "Age: " + str(14)  → Works! str() converts it to "14"
print("Age message : " + "Age: " + str(14))

# -------------------------------------------------------
# OPERATION 2: Repetition (*) — Repeat a string
# Think of it like copy-pasting multiple times
# -------------------------------------------------------
print("\n--- OPERATION 2: Repetition (*) ---")

line     = "-" * 30
star_row = "* " * 10
cheer    = "Go Chennai! " * 3

print(line)
print(star_row)
print(cheer)

# Real use: Creating a scoreboard border
print("\n" + "=" * 40)
print("       CRICKET SCOREBOARD")
print("=" * 40)
print("  Team       : Chennai Super Kings")
print("  Score      : 186 / 4")
print("  Overs      : 20.0")
print("=" * 40)

# -------------------------------------------------------
# OPERATION 3: Membership (in / not in) — Check if exists
# Think of it like checking if an item is in a bag
# -------------------------------------------------------
print("\n--- OPERATION 3: Membership (in / not in) ---")

team_list = "Aarav, Diya, Mani, Priya, Ravi"

print("Team list : " + team_list)
print("Is 'Diya' in the team?   →", "Diya" in team_list)
print("Is 'Ravi' in the team?   →", "Ravi" in team_list)
print("Is 'Kavya' in the team?  →", "Kavya" in team_list)
print("Is 'Kavya' NOT in team?  →", "Kavya" not in team_list)

# -------------------------------------------------------
# OPERATION 4: len() — Find the length of a string
# Counts every character including spaces!
# -------------------------------------------------------
print("\n--- OPERATION 4: len() — String Length ---")

print("len('Python')           =", len("Python"))
print("len('Aarav Sharma')    =", len("Aarav Sharma"))
print("len('I love coding!')  =", len("I love coding!"))

# Real use: Password length check
password = input("\nEnter a password to check its length: ")
print("Your password has", len(password), "characters.")
if len(password) >= 8:
    print("✅ Strong password (8 or more characters)")
else:
    print("❌ Weak password (needs at least 8 characters)")

# -------------------------------------------------------
# SUMMARY
# -------------------------------------------------------
print("\n" + "=" * 55)
print("  OPERATION QUICK REFERENCE")
print("=" * 55)
print("  +         → Concatenate (join) strings")
print("  *         → Repeat a string N times")
print("  in        → Check if text exists inside a string")
print("  not in    → Check if text does NOT exist")
print("  len()     → Count total characters in a string")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. What does "ha" * 5 produce?
# 2. Why does "Age: " + 14 fail? How do you fix it?
# 3. Does "diya" in "Diya and Aarav" return True or False?
#    (Hint: think about uppercase/lowercase!)
# 4. What is len("") (empty string)?
# ============================================================
