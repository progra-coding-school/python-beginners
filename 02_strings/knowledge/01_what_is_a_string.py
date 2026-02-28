# Program Code: STR-KN-01
# Title: What is a String? — Text Lives in Quotes!
# Cognitive Skill: Knowledge (Acquiring the concept)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav wants to write a program that prints his name,
# his school name, and his favourite cricket player.
# How do we work with TEXT in Python?
# That's where STRINGS come in!
# ============================================================

# ============================================================
# WHAT IS A STRING?
# A string is a piece of TEXT written inside quotes.
# It can be a name, a word, a sentence, or even a single letter.
# In Python, anything inside quotes (" " or ' ') is a STRING.
# ============================================================

print("=" * 50)
print("       WELCOME TO STRINGS IN PYTHON!")
print("=" * 50)

# -------------------------------------------------------
# Example 1: A name is a string
# -------------------------------------------------------
print("\nStudent name     : Aarav")

# -------------------------------------------------------
# Example 2: A school name is a string
# -------------------------------------------------------
print("School name      : Progra Kids Coding School")

# -------------------------------------------------------
# Example 3: A cricket player name is a string
# -------------------------------------------------------
print("Favourite player : Virat Kohli")

# -------------------------------------------------------
# Example 4: A single letter is also a string
# -------------------------------------------------------
print("Grade            : A")

# -------------------------------------------------------
# Example 5: A full sentence is a string
# -------------------------------------------------------
print("Message          : Keep coding and keep smiling!")

print("\n" + "=" * 50)
print("  KEY IDEA: Anything in quotes is a STRING!")
print("=" * 50)

# ============================================================
# QUICK FACTS ABOUT STRINGS:
# ✅ Strings are written inside single quotes 'hello'
#    or double quotes "hello"
# ✅ Strings can hold letters, numbers, symbols, spaces
# ✅ A string of zero characters is called an EMPTY STRING: ""
# ✅ The type of a string is: str
# ============================================================

print("\nType of 'Aarav'  :", type("Aarav"))
print("Type of 'A'      :", type("A"))

print("\n" + "-" * 50)
print("  EMPTY STRING example:")
print("  Type:", type(""), "   Length:", len(""))
print("-" * 50)

# ============================================================
# REFLECTION:
# 1. What is the difference between 42 and "42"?
# 2. Can a string contain numbers? Try: print("12B, MG Road")
# 3. What does type("Hello") return?
# ============================================================
