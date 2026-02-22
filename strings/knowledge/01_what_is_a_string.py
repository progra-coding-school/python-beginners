# Program Code: STR-KN-01
# Title: What is a String? — Text Lives in Quotes!
# Cognitive Skill: Knowledge (Acquiring the concept)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav wants to write a program that stores his name,
# his school name, and his favourite cricket player.
# He tried storing numbers before — but how do we store TEXT?
# That's where STRINGS come in!
# ============================================================

# ============================================================
# WHAT IS A STRING?
# A string is a piece of TEXT stored inside quotes.
# It can be a name, a word, a sentence, or even a single letter.
# In Python, anything inside quotes (" " or ' ') is a STRING.
# ============================================================

print("=" * 50)
print("       WELCOME TO STRINGS IN PYTHON!")
print("=" * 50)

# -------------------------------------------------------
# Example 1: Storing a name
# -------------------------------------------------------
student_name = "Aarav"
print(f"\nStudent name  : {student_name}")

# -------------------------------------------------------
# Example 2: Storing a school name
# -------------------------------------------------------
school_name = "Progra Kids Coding School"
print(f"School name   : {school_name}")

# -------------------------------------------------------
# Example 3: Storing a cricket player name
# -------------------------------------------------------
favourite_player = "Virat Kohli"
print(f"Favourite player : {favourite_player}")

# -------------------------------------------------------
# Example 4: Storing a single letter
# -------------------------------------------------------
grade = "A"
print(f"Grade         : {grade}")

# -------------------------------------------------------
# Example 5: Storing a full sentence
# -------------------------------------------------------
message = "Keep coding and keep smiling!"
print(f"Message       : {message}")

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

print(f"\nType of student_name : {type(student_name)}")
print(f"Type of grade        : {type(grade)}")

print("\n" + "-" * 50)
print("  EMPTY STRING example:")
empty = ""
print(f"  empty = '' → Type: {type(empty)}, Length: {len(empty)}")
print("-" * 50)

# ============================================================
# REFLECTION:
# 1. What is the difference between 42 and "42"?
# 2. Can a string contain numbers? Try: address = "12B, MG Road"
# 3. What happens if you forget the quotes? Try: name = Aarav
# ============================================================
