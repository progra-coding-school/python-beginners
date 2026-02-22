# Program Code: STR-UN-03
# Title: Strings Are Immutable — You Can't Change Them Directly!
# Cognitive Skill: Understanding (Deepening the concept)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav made a spelling mistake: he typed "Pythen" instead of "Python".
# He thinks he can change just the 4th letter like this:
#     word[4] = "o"
# But Python says NO! Let's understand WHY — and how to fix it correctly.
# ============================================================

print("=" * 55)
print("   STRINGS ARE IMMUTABLE — A FIXED LOCKER!")
print("=" * 55)

# -------------------------------------------------------
# WHAT IS IMMUTABILITY?
# Once a string is created, you CANNOT change individual characters.
# The string is "locked" — like a name badge that's already printed.
# -------------------------------------------------------

print("""
ANALOGY:
Imagine your school name badge is printed.
You can't erase just one letter from it.
If you need a correction — you print a BRAND NEW badge!

Python strings work the same way.
""")

# -------------------------------------------------------
# DEMONSTRATION: Trying to change a character → ERROR
# -------------------------------------------------------
print("--- What happens if we try to change a character? ---")

word = "Pythen"
print(f"Word with typo : '{word}'")
print()
print("Trying: word[4] = 'o'")
print()

try:
    word[4] = "o"           # This will cause a TypeError!
except TypeError as e:
    print(f"❌ ERROR: {e}")
    print("   Python does NOT allow changing individual characters!")

# -------------------------------------------------------
# THE RIGHT WAY: Create a NEW string
# -------------------------------------------------------
print("\n--- The Right Way: Build a New String ---")

# Method 1: Concatenation (join parts)
correct_word = word[:4] + "o" + word[5:]
print(f"Method 1 (slicing + concat) : '{correct_word}'")

# Method 2: replace() method
correct_word2 = word.replace("e", "o")
print(f"Method 2 (replace)          : '{correct_word2}'")

# -------------------------------------------------------
# KEY CONCEPT: Reassigning a variable
# -------------------------------------------------------
print("\n--- Reassigning is Fine! ---")

greeting = "Hello"
print(f"Before : greeting = '{greeting}'")

# You CAN point the variable to a new string
greeting = greeting.upper()
print(f"After  : greeting = '{greeting}'")

print("""
This is NOT changing the string 'Hello'.
Python created a NEW string 'HELLO' and
pointed the variable 'greeting' to the new one!

Old string 'Hello' → still exists in memory (Python handles it)
New string 'HELLO' → greeting now points here
""")

# -------------------------------------------------------
# REAL WORLD EXAMPLE: Fixing a student's name
# -------------------------------------------------------
print("--- Real Use: Fixing a Typed Name ---")

typed_name = "aARAV"          # Badly formatted input
print(f"Typed name   : '{typed_name}'")

fixed_name = typed_name.title()     # Creates a NEW corrected string
print(f"Fixed name   : '{fixed_name}'")

print("""
Note: .title() didn't CHANGE 'aARAV'.
It created a NEW string 'Aarav'.
We stored that new string back into fixed_name.
""")

print("=" * 55)
print("  KEY IDEAS:")
print("  • Strings CANNOT be changed character by character")
print("  • Any method (upper, replace, etc.) returns a NEW string")
print("  • You can reassign a variable to point to the new string")
print("  • This behaviour is called IMMUTABILITY")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. What is "immutable"? Give a real-life example.
# 2. If name = "Aarav" and you do name.upper(), what is name now?
# 3. How would you fix "Pythn" to "Python" using slicing?
# 4. Does replace() change the original string or return a new one?
# ============================================================
