# Program Code: CS-ST-02
# Title: Naming Matters - Good Names vs Bad Names
# Cognitive Skill: Structured Thinking (Systematic naming conventions)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Imagine you open a book and all the chapters are named
# "Chapter A", "Chapter B", "Chapter C"...
# Would you know what each chapter is about? NO!
# Variable names work the same way.
# Bad names make code CONFUSING. Good names make code CLEAR.
# Let's experience the difference!
# ============================================================

print("=== Naming Matters: Good Names vs Bad Names ===")
print()

# ===== PART 1: Can you understand this? =====
print("=" * 50)
print("PART 1: Read this code. What does it DO?")
print("=" * 50)
print()
print("  x = 12")
print("  y = 8")
print("  z = x + y")
print("  a = z / 2")
print("  print(a)")
print()

# Run the bad-names version
x = 12
y = 8
z = x + y
a = z / 2
print(f"  Output: {a}")
print()

answer = input("Can you guess what this program calculates? : ")
print()

# Now reveal with good names!
print("Here is the SAME program with GOOD names:")
print()
print("  aarav_age = 12")
print("  diya_age = 8")
print("  total_age = aarav_age + diya_age")
print("  average_age = total_age / 2")
print("  print(average_age)")
print()

aarav_age = 12
diya_age = 8
total_age = aarav_age + diya_age
average_age = total_age / 2
print(f"  Output: {average_age}")
print()
print("NOW you can see it calculates the AVERAGE AGE!")
print("Same code. Same result. But GOOD names tell the story!")

input("\nPress Enter for Part 2...")
print()

# ===== PART 2: The Confusion Challenge =====
print("=" * 50)
print("PART 2: Decode the Confusing Code!")
print("=" * 50)
print()
print("Aarav wrote this program with TERRIBLE names.")
print("Can you figure out what each variable represents?")
print()
print("  p = 250")
print("  q = 3")
print("  r = 50")
print("  s = p * q")
print("  t = s - r")
print("  print(t)")
print()

p = 250
q = 3
r = 50
s = p * q
t = s - r
print(f"  Output: {t}")
print()
print("HINTS: It is a shopping calculation.")
print("  - Someone is buying items at a shop")
print("  - There is a price, quantity, and discount")
print()
input("Think about it... Press Enter to see the answer...")
print()

print("With GOOD names:")
print()
print("  price_per_item = 250")
print("  quantity = 3")
print("  discount = 50")
print("  subtotal = price_per_item * quantity")
print("  final_price = subtotal - discount")
print("  print(final_price)")
print()

price_per_item = 250
quantity = 3
discount = 50
subtotal = price_per_item * quantity
final_price = subtotal - discount
print(f"  Output: {final_price}")
print()
print("Same logic, but now ANYONE can understand it!")

input("\nPress Enter for Part 3...")
print()

# ===== PART 3: YOU Fix the Names =====
print("=" * 50)
print("PART 3: YOU Rename the Variables!")
print("=" * 50)
print()
print("Here is a marks calculator with bad names:")
print()
print("  a1 = 85")
print("  a2 = 90")
print("  a3 = 78")
print("  a4 = 92")
print("  a5 = 88")
print("  t = a1 + a2 + a3 + a4 + a5")
print("  p = t / 5")
print()

a1 = 85
a2 = 90
a3 = 78
a4 = 92
a5 = 88
t = a1 + a2 + a3 + a4 + a5
p = t / 5

print(f"  Total: {t}, Percentage: {p}")
print()
print("Your turn! What BETTER names would you give?")
print()

name_a1 = input("  Better name for a1 (85 in first subject)?  : ")
name_a2 = input("  Better name for a2 (90 in second subject)? : ")
name_t = input("  Better name for t (sum of all marks)?       : ")
name_p = input("  Better name for p (average/percentage)?     : ")
print()

print("Great thinking! Here is a GOOD version:")
print()
print("  maths_marks = 85")
print("  science_marks = 90")
print("  english_marks = 78")
print("  tamil_marks = 92")
print("  social_marks = 88")
print("  total_marks = maths_marks + science_marks + english_marks + tamil_marks + social_marks")
print("  percentage = total_marks / 5")
print()
print("NAMING RULES to remember:")
print("  1. Use descriptive names (maths_marks, NOT a1)")
print("  2. Use snake_case (total_marks, NOT totalmarks)")
print("  3. Names should tell WHAT the variable stores")
print("  4. If someone reads your code, they should understand it")

# ============================================================
# REFLECTION PROMPTS:
# 1. Which version was easier to understand - bad names or good names?
#    How much TIME did you waste trying to decode bad names?
#
# 2. "Code is read more often than it is written."
#    What does this mean? Why should we care about naming?
#
# 3. Think of your school notebook. If you wrote notes with no
#    headings and no labels, could you study from it?
#    Variable names are like LABELS for your data!
# ============================================================
