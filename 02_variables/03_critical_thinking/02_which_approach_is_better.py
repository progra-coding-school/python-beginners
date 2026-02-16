# Program Code: CS-CT-02
# Title: Which Approach is Better?
# Cognitive Skill: Critical Thinking (Evaluating and comparing)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# In programming, there is often MORE THAN ONE way to solve
# a problem. But which way is BETTER?
# Here are 3 problems, each solved in TWO different ways.
# Your job: Read both, think, and decide which is better - and WHY.
# There is no single "right" answer. What matters is your REASONING!
# ============================================================

print("=== Which Approach is Better? ===")
print("Two solutions for each problem. YOU decide which is better!")
print()

# ===== PROBLEM 1: Aarav's Monthly Savings =====
print("=" * 50)
print("PROBLEM 1: Aarav's Monthly Savings")
print("Aarav earns Rs.500 pocket money. He spends Rs.200 on")
print("snacks and Rs.100 on books. How much does he save?")
print("=" * 50)
print()

print("--- Approach A: One Big Formula ---")
print('  pocket_money = 500')
print('  savings = 500 - 200 - 100')
print('  print("Savings:", savings)')
print()

print("--- Approach B: Step by Step ---")
print('  pocket_money = 500')
print('  snacks_expense = 200')
print('  books_expense = 100')
print('  total_expense = snacks_expense + books_expense')
print('  savings = pocket_money - total_expense')
print('  print("Savings:", savings)')
print()

# Both give the same answer!
savings_a = 500 - 200 - 100

pocket_money = 500
snacks_expense = 200
books_expense = 100
total_expense = snacks_expense + books_expense
savings_b = pocket_money - total_expense

print(f"Approach A result: Rs.{savings_a}")
print(f"Approach B result: Rs.{savings_b}")
print(f"Both give the SAME answer!")
print()

choice = input("Which approach is better? (A or B): ").upper()
print()
print("THINK ABOUT THIS:")
print("- Approach A is SHORTER (fewer lines)")
print("- Approach B is CLEARER (each expense has a name)")
print("- If Aarav adds a NEW expense (games = Rs.50),")
print("  which approach is easier to MODIFY?")
print("- Approach B! You just add one variable and update total_expense.")
print("- In real coding, CLARITY often beats SHORTNESS.")

input("\nPress Enter for Problem 2...")
print()

# ===== PROBLEM 2: Converting Temperature =====
print("=" * 50)
print("PROBLEM 2: Converting Celsius to Fahrenheit")
print("Formula: F = (C * 9/5) + 32")
print("=" * 50)
print()

print("--- Approach A: Using raw numbers ---")
print('  celsius = 37')
print('  fahrenheit = (37 * 9/5) + 32')
print('  print(fahrenheit)')
print()

print("--- Approach B: Using the variable ---")
print('  celsius = 37')
print('  fahrenheit = (celsius * 9/5) + 32')
print('  print(fahrenheit)')
print()

choice = input("Which approach is better? (A or B): ").upper()
print()
print("THINK ABOUT THIS:")
print("- Both give 98.6 when celsius is 37")
print("- But in Approach A, the number 37 is used directly")
print("  If you change celsius to 100, the formula STILL uses 37!")
print("  That is a BUG waiting to happen!")
print("- Approach B uses the VARIABLE 'celsius' in the formula")
print("  Change the value once, everything updates correctly.")
print("- RULE: Once you store a value in a variable, USE the variable!")

input("\nPress Enter for Problem 3...")
print()

# ===== PROBLEM 3: Student Info =====
print("=" * 50)
print("PROBLEM 3: Printing Student Information")
print("=" * 50)
print()

print("--- Approach A: Separate prints ---")
print('  name = "Diya"')
print('  age = 10')
print('  grade = "5th"')
print('  print("Name:", name)')
print('  print("Age:", age)')
print('  print("Grade:", grade)')
print()

print("--- Approach B: One f-string ---")
print('  name = "Diya"')
print('  age = 10')
print('  grade = "5th"')
print('  print(f"{name}, age {age}, studies in {grade} grade")')
print()

choice = input("Which approach is better? (A or B): ").upper()
print()
print("THINK ABOUT THIS:")
print("- This time, BOTH approaches are valid!")
print("- Approach A is better if you want each detail on its own line")
print("- Approach B is better if you want a natural sentence")
print("- The 'best' approach depends on what OUTPUT you want!")
print("- LESSON: Sometimes there is no single best answer.")
print("  A good programmer chooses based on the SITUATION.")

# ============================================================
# REFLECTION PROMPTS:
# 1. In Problem 1, why is "clear" code often better than "short" code?
# 2. In Problem 2, what is wrong with putting raw numbers in formulas
#    when you already have a variable for that number?
# 3. A friend says "The best code is always the shortest code."
#    Do you agree or disagree? Give an example to support your answer.
# ============================================================
