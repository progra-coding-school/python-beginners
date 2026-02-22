# Program Code: STR-UN-02
# Title: Indexing and Slicing — Pick Any Part of a String!
# Cognitive Skill: Understanding (Deepening the concept)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Amma is cutting a sugarcane stick.
# She can cut from the front, the middle, or the back.
# Python strings work the same way!
# - INDEXING: Pick one character
# - SLICING : Pick a PORTION (slice) of the string
# ============================================================

print("=" * 55)
print("     INDEXING AND SLICING — CUT YOUR STRING!")
print("=" * 55)

city = "CHENNAI"

# -------------------------------------------------------
# VISUALISING POSITIVE AND NEGATIVE INDEXING
# -------------------------------------------------------
print(f"\nString: '{city}'")
print()
print("  +---+---+---+---+---+---+---+")
print("  | C | H | E | N | N | A | I |")
print("  +---+---+---+---+---+---+---+")
print("    0   1   2   3   4   5   6     ← Positive Index")
print("   -7  -6  -5  -4  -3  -2  -1    ← Negative Index")
print()

# -------------------------------------------------------
# PART 1: POSITIVE INDEXING (count from front)
# -------------------------------------------------------
print("--- Positive Indexing (0, 1, 2...) ---")
print(f"city[0]  = '{city[0]}'  → First character")
print(f"city[3]  = '{city[3]}'  → Fourth character")
print(f"city[6]  = '{city[6]}'  → Last character")

# -------------------------------------------------------
# PART 2: NEGATIVE INDEXING (count from back)
# Tip: -1 is always the LAST character!
# -------------------------------------------------------
print("\n--- Negative Indexing (-1, -2, -3...) ---")
print(f"city[-1] = '{city[-1]}'  → Last character")
print(f"city[-2] = '{city[-2]}'  → Second from last")
print(f"city[-7] = '{city[-7]}'  → First character")

# -------------------------------------------------------
# PART 3: SLICING — string[start : end]
# Takes characters from start up to (but NOT including) end
# -------------------------------------------------------
print("\n--- Slicing: string[start:end] ---")
word = "CRICKET"

print(f"\nString: '{word}'")
print()
print("  +---+---+---+---+---+---+---+")
print("  | C | R | I | C | K | E | T |")
print("  +---+---+---+---+---+---+---+")
print("    0   1   2   3   4   5   6")
print()

print(f"word[0:3]  = '{word[0:3]}'   → Index 0, 1, 2")
print(f"word[3:7]  = '{word[3:7]}'  → Index 3, 4, 5, 6")
print(f"word[1:5]  = '{word[1:5]}'  → Index 1, 2, 3, 4")

# -------------------------------------------------------
# PART 4: SLICING SHORTCUTS
# -------------------------------------------------------
print("\n--- Slicing Shortcuts ---")
print(f"word[:3]   = '{word[:3]}'    → From start to index 2 (first 3)")
print(f"word[4:]   = '{word[4:]}'    → From index 4 to end")
print(f"word[:]    = '{word[:]}'  → Entire string (copy)")
print(f"word[-3:]  = '{word[-3:]}'    → Last 3 characters")
print(f"word[::2]  = '{word[::2]}'   → Every 2nd character (step=2)")
print(f"word[::-1] = '{word[::-1]}' → Reverse the string!")

# -------------------------------------------------------
# REAL USE: Extract parts of data
# -------------------------------------------------------
print("\n--- Real Use: Extracting Information ---")

student_code = "STU-2025-AARAV"
print(f"Student Code : {student_code}")
print(f"Prefix       : {student_code[:3]}")     # STU
print(f"Year         : {student_code[4:8]}")     # 2025
print(f"Name         : {student_code[9:]}")      # AARAV

print()
date = "21-02-2026"
print(f"Date   : {date}")
print(f"Day    : {date[:2]}")
print(f"Month  : {date[3:5]}")
print(f"Year   : {date[6:]}")

print("\n" + "=" * 55)
print("  KEY IDEAS:")
print("  • Positive index → count from front (0, 1, 2...)")
print("  • Negative index → count from back (-1, -2...)")
print("  • Slice [start:end] → end is NOT included!")
print("  • [::-1] → reverse a string!")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. What does "Python"[-1] return?
# 2. What does "Chennai"[2:5] return?
# 3. How do you get the last 3 characters of any string?
# 4. What does "Hello"[::-1] produce?
# ============================================================
