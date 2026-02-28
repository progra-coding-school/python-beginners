# Program Code: STR-KN-03
# Title: String Methods — Superpowers for Your Text!
# Cognitive Skill: Knowledge (Acquiring the concept)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav's school is building a student management system.
# They need to:
#   - Fix name formatting (ALL CAPS, all small, Proper Case)
#   - Remove extra spaces from typed names
#   - Search if a student is in a group
#   - Count how many times a letter appears
# Strings come with BUILT-IN TOOLS called METHODS to do this!
# ============================================================

print("=" * 55)
print("    STRING METHODS — YOUR TEXT SUPERPOWERS!")
print("=" * 55)

name = "  aarav sharma  "   # Note: extra spaces on both sides

# -------------------------------------------------------
# METHOD 1: strip() — Remove extra spaces
# -------------------------------------------------------
print("\n--- strip() — Remove Extra Spaces ---")
clean_name = name.strip()
print("Before strip : '" + name + "'")
print("After strip  : '" + clean_name + "'")

# -------------------------------------------------------
# METHOD 2: upper() — Convert to UPPERCASE
# -------------------------------------------------------
print("\n--- upper() — ALL CAPITAL LETTERS ---")
shout = clean_name.upper()
print("upper() → '" + shout + "'")

# -------------------------------------------------------
# METHOD 3: lower() — Convert to lowercase
# -------------------------------------------------------
print("\n--- lower() — all small letters ---")
whisper = clean_name.lower()
print("lower() → '" + whisper + "'")

# -------------------------------------------------------
# METHOD 4: title() — Proper Case (First Letter Capital)
# -------------------------------------------------------
print("\n--- title() — Proper Name Format ---")
proper = clean_name.title()
print("title() → '" + proper + "'")

# -------------------------------------------------------
# METHOD 5: replace() — Swap one word for another
# -------------------------------------------------------
print("\n--- replace() — Find and Replace ---")
sentence = "I love cricket and cricket is my passion"
new_sentence = sentence.replace("cricket", "coding")
print("Original : " + sentence)
print("Replaced : " + new_sentence)

# -------------------------------------------------------
# METHOD 6: find() — Find position of a word
# -------------------------------------------------------
print("\n--- find() — Find Position of a Word ---")
team     = "Chennai Super Kings"
position = team.find("Super")
print("Team     : " + team)
print("'Super' found at position :", position)
print("(Returns -1 if not found)")

not_found = team.find("Mumbai")
print("'Mumbai' found at position :", not_found)

# -------------------------------------------------------
# METHOD 7: count() — Count how many times something appears
# -------------------------------------------------------
print("\n--- count() — Count Occurrences ---")
sentence2  = "Amma makes amazing and awesome aloo!"
vowel_count = sentence2.count("a")
print("Sentence     : " + sentence2)
print("Count of 'a' :", vowel_count)

# -------------------------------------------------------
# METHOD 8: startswith() / endswith()
# -------------------------------------------------------
print("\n--- startswith() and endswith() ---")
school = "Progra Kids Coding School"
print("Starts with 'Progra'  :", school.startswith("Progra"))
print("Ends with 'School'    :", school.endswith("School"))

# -------------------------------------------------------
# METHOD 9: split() — Break sentence into words
# -------------------------------------------------------
print("\n--- split() — Break into a List of Words ---")
player_names = "Aarav, Diya, Priya, Mani"
players_list = player_names.split(", ")
print("Original   : " + player_names)
print("Split list :", players_list)

# -------------------------------------------------------
# SUMMARY TABLE
# -------------------------------------------------------
print("\n" + "=" * 55)
print("  METHOD QUICK REFERENCE")
print("=" * 55)
print("  strip()        → Remove spaces at start/end")
print("  upper()        → ALL CAPS")
print("  lower()        → all small")
print("  title()        → First Letter Capital")
print("  replace(a, b)  → Replace a with b")
print("  find(x)        → Position of x (-1 if not found)")
print("  count(x)       → How many times x appears")
print("  startswith(x)  → Does it start with x?")
print("  endswith(x)    → Does it end with x?")
print("  split(x)       → Break into list by separator x")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. What does "Aarav".upper() return?
# 2. How would you count how many 'a's are in your name?
# 3. What does find() return if the word is NOT found?
# 4. Try: "  Hello World  ".strip().lower().replace("world","Python")
# ============================================================
