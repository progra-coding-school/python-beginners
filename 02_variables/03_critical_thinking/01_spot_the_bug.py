# Program Code: CS-CT-01
# Title: Debug Detective - Spot the Bug!
# Cognitive Skill: Critical Thinking (Evaluating code for errors)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav wrote some Python programs but they have BUGS!
# A bug is a mistake in the code that makes it not work.
# Can you be a detective and find each bug?
# Read the code carefully, think about what is wrong,
# and explain the fix!
# ============================================================

# ------------------------------------------------------------
# HOW TO PLAY:
# 1. Read each buggy code carefully
# 2. Think: What is wrong? WHY is it wrong?
# 3. Type your answer
# 4. The program reveals the bug and the fix
# ------------------------------------------------------------

score = 0

print("=== Debug Detective: Spot the Bug! ===")
print("Aarav wrote code, but each one has a bug.")
print("Can you find them all?")
print()

# ----- BUG 1: Using a variable before creating it -----
print("--- Bug 1 ---")
print("Aarav wrote this code:")
print()
print('  print(greeting)')
print('  greeting = "Vanakkam!"')
print()
answer = input("What is the bug? (Hint: order matters): ")
print()
print("THE BUG: Aarav tried to PRINT 'greeting' BEFORE creating it!")
print("Python reads code top to bottom. You must CREATE a variable")
print("BEFORE you use it.")
print()
print("THE FIX:")
print('  greeting = "Vanakkam!"')
print('  print(greeting)')
score = score + 1
print()
input("Press Enter for Bug 2...")
print()

# ----- BUG 2: Misspelled variable name -----
print("--- Bug 2 ---")
print("Aarav wrote this code:")
print()
print('  student_name = "Diya"')
print('  print(studnet_name)')
print()
answer = input("What is the bug? (Hint: look very carefully at the spelling): ")
print()
print("THE BUG: Aarav wrote 'studnet_name' instead of 'student_name'!")
print("'student' is spelled wrong as 'studnet'.")
print("Python treats them as TWO DIFFERENT variables!")
print()
print("THE FIX:")
print('  student_name = "Diya"')
print('  print(student_name)    # spelling matches!')
score = score + 1
print()
input("Press Enter for Bug 3...")
print()

# ----- BUG 3: Accidental overwrite -----
print("--- Bug 3 ---")
print("Aarav wanted to store BOTH his Maths and Science marks:")
print()
print('  marks = 85')
print('  marks = 92')
print('  print("Maths:", marks)')
print('  print("Science:", marks)')
print()
answer = input("What is the bug? (Hint: what happened to 85?): ")
print()
print("THE BUG: Both subjects show 92! The value 85 was OVERWRITTEN.")
print("When you assign a new value to the same variable, the old value is GONE!")
print()
print("THE FIX: Use DIFFERENT variable names!")
print('  maths_marks = 85')
print('  science_marks = 92')
print('  print("Maths:", maths_marks)')
print('  print("Science:", science_marks)')
score = score + 1
print()
input("Press Enter for Bug 4...")
print()

# ----- BUG 4: String + Number error -----
print("--- Bug 4 ---")
print("Aarav wrote this code:")
print()
print('  age = input("Enter your age: ")')
print('  birth_year = 2025 - age')
print('  print("You were born in", birth_year)')
print()
answer = input("What is the bug? (Hint: what type does input() give?): ")
print()
print("THE BUG: input() always gives a STRING, not a number!")
print("You cannot subtract a string from 2025.")
print("Python will give a TypeError!")
print()
print("THE FIX: Convert to integer using int()!")
print('  age = int(input("Enter your age: "))')
print('  birth_year = 2025 - age')
print('  print("You were born in", birth_year)')
score = score + 1
print()
input("Press Enter for Bug 5...")
print()

# ----- BUG 5: Wrong variable in calculation -----
print("--- Bug 5 ---")
print("Aarav wrote a shop billing program:")
print()
print('  price_per_item = 50')
print('  quantity = 3')
print('  discount = 10')
print('  total = price_per_item * quantity')
print('  final_price = total - price_per_item    # Apply discount')
print()
answer = input("What is the bug? (Hint: read the comment, look at the code): ")
print()
print("THE BUG: Aarav wanted to subtract the DISCOUNT (10)")
print("but accidentally subtracted PRICE_PER_ITEM (50) instead!")
print("He used the WRONG variable!")
print()
print("THE FIX:")
print('  final_price = total - discount    # Now subtracting the correct variable!')
score = score + 1
print()

# Final Score
print("=" * 40)
print(f"BUGS FOUND: {score} / 5")
print("You are a Debug Detective!")
print("=" * 40)

# ============================================================
# REFLECTION PROMPTS:
# 1. Which bug was hardest to spot? Why?
# 2. Bug 5 had NO error message - it just gave the WRONG answer.
#    Why are "silent bugs" (wrong answer, no error) the most
#    dangerous kind of bug?
# 3. How can you PREVENT bugs? Think of 2 habits that help.
#    (Hint: meaningful names, checking your work, testing)
# ============================================================
