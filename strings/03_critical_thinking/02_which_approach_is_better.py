# Program Code: STR-CT-02
# Title: Which Approach is Better? — Evaluate String Solutions!
# Cognitive Skill: Critical Thinking (Evaluating approaches)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Two students, Aarav and Diya, solved the same problems
# using different approaches. Which solution is CLEANER,
# SHORTER, and EASIER to understand?
# Evaluate both and explain your reasoning!
# ============================================================

print("=" * 55)
print("  WHICH APPROACH IS BETTER? — THINK AND EVALUATE!")
print("=" * 55)

# -------------------------------------------------------
# PROBLEM 1: Build a full name from first and last name
# -------------------------------------------------------
print("\n--- PROBLEM 1: Build Full Name ---")
print("Task: Combine first name and last name into full name")
print()

first = "aarav"
last  = "sharma"

print("  AARAV's Approach (Concatenation):")
print('  full_name = first.title() + " " + last.title()')
aarav_result = first.title() + " " + last.title()
print(f"  Result: '{aarav_result}'")

print()
print("  DIYA's Approach (f-string):")
print('  full_name = f"{first.title()} {last.title()}"')
diya_result = f"{first.title()} {last.title()}"
print(f"  Result: '{diya_result}'")

print()
input("  Which is better? Think first... press ENTER: ")
print("""
  Both produce the SAME result!
  → Diya's f-string is CLEANER and easier to read.
  → Aarav's concatenation works but is harder to read
    when there are many variables.
  ✅ WINNER: f-string (for readability)
""")

# -------------------------------------------------------
# PROBLEM 2: Check if "cricket" is in a sentence
# -------------------------------------------------------
print("=" * 55)
print("\n--- PROBLEM 2: Check if Word Exists ---")
print("Task: Check if 'cricket' is mentioned in the sentence")
print()

sentence = "Aarav loves cricket and plays every Sunday."

print("  AARAV's Approach (find):")
print('  result = sentence.find("cricket") != -1')
aarav_check = sentence.find("cricket") != -1
print(f"  Result: {aarav_check}")

print()
print("  DIYA's Approach (in keyword):")
print('  result = "cricket" in sentence')
diya_check  = "cricket" in sentence
print(f"  Result: {diya_check}")

print()
input("  Which is better? Think first... press ENTER: ")
print("""
  Both give the SAME result!
  → Diya's 'in' keyword is MORE READABLE (reads like English!)
  → Aarav's find() works but is more complex for a simple check.
  ✅ WINNER: 'in' keyword (for simple membership checks)
  📝 NOTE: Use find() when you also need the POSITION.
""")

# -------------------------------------------------------
# PROBLEM 3: Convert user input safely
# -------------------------------------------------------
print("=" * 55)
print("\n--- PROBLEM 3: Clean and Compare User Input ---")
print("Task: Check if user typed the correct answer 'Python'")
print()

user_typed = "  PYTHON  "

print("  AARAV's Approach:")
print('  if user_typed == "Python":')
print(f"    (user typed '{user_typed}' → Match? {user_typed == 'Python'})")

print()
print("  DIYA's Approach:")
print('  if user_typed.strip().lower() == "python":')
diya_check = user_typed.strip().lower() == "python"
print(f"    (user typed '{user_typed}' → Match? {diya_check})")

print()
input("  Which is better? Think first... press ENTER: ")
print("""
  → Aarav's approach MISSES the answer — too strict!
  → Diya's approach is ROBUST — handles spaces and case.
  ✅ WINNER: Diya's approach (defensive coding)
  📝 RULE: Always strip and lower-case before comparing user input.
""")

print("=" * 55)
print("  KEY LESSONS:")
print("  1. f-strings > concatenation for readability")
print("  2. 'in' > find() for simple membership checks")
print("  3. Always .strip().lower() before comparing user input")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. When would you prefer find() over 'in'?
# 2. Can you think of a case where concatenation is better?
# 3. What other ways can user input be "messy" to handle?
# ============================================================
