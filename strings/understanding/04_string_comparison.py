# Program Code: STR-UN-04
# Title: String Comparison — Are These Texts the Same?
# Cognitive Skill: Understanding (Deepening the concept)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Progra's quiz app needs to check if the student's answer
# matches the correct answer. But there's a twist:
# "Python" and "python" look similar — but ARE they equal?
# Let's understand how Python COMPARES strings!
# ============================================================

print("=" * 55)
print("   STRING COMPARISON — ARE THEY REALLY EQUAL?")
print("=" * 55)

# -------------------------------------------------------
# PART 1: Equality Check (== and !=)
# -------------------------------------------------------
print("\n--- Part 1: Equal (==) and Not Equal (!=) ---")

correct_answer = "Python"
student_answer1 = "Python"
student_answer2 = "python"
student_answer3 = "PYTHON"

print(f"Correct answer   : '{correct_answer}'")
print(f"Student answer 1 : '{student_answer1}'  → Match? {student_answer1 == correct_answer}")
print(f"Student answer 2 : '{student_answer2}'  → Match? {student_answer2 == correct_answer}")
print(f"Student answer 3 : '{student_answer3}'  → Match? {student_answer3 == correct_answer}")

print("\n⚠️  Python is CASE-SENSITIVE! 'Python' ≠ 'python' ≠ 'PYTHON'")

# -------------------------------------------------------
# FIX: Case-Insensitive Comparison
# -------------------------------------------------------
print("\n--- Case-Insensitive Comparison (use .lower()) ---")

correct = "Python"
typed   = "PYTHON"

# Compare after converting both to lowercase
if typed.lower() == correct.lower():
    print(f"'{typed}' matches '{correct}' (ignoring case) ✅")
else:
    print(f"'{typed}' does NOT match '{correct}' ❌")

# -------------------------------------------------------
# PART 2: Membership Check (in / not in)
# -------------------------------------------------------
print("\n--- Part 2: Membership Check (in / not in) ---")

team = "Aarav, Diya, Mani, Priya"
print(f"Team list : {team}")
print()

search1 = "Diya"
search2 = "Kavya"

print(f"Is '{search1}' in the team?  → {search1 in team}")
print(f"Is '{search2}' in the team?  → {search2 in team}")
print(f"Is '{search2}' NOT in team?  → {search2 not in team}")

# -------------------------------------------------------
# PART 3: Alphabetical Comparison (< > <= >=)
# Python compares strings alphabetically (like a dictionary)
# -------------------------------------------------------
print("\n--- Part 3: Alphabetical Order (< and >) ---")

name1 = "Aarav"
name2 = "Diya"
name3 = "Mani"

print(f"'{name1}' < '{name2}'  → {name1 < name2}   (A comes before D)")
print(f"'{name2}' < '{name3}'  → {name2 < name3}   (D comes before M)")
print(f"'{name3}' > '{name1}'  → {name3 > name1}   (M comes after A)")

# Sort names alphabetically
names = ["Mani", "Aarav", "Priya", "Diya"]
print(f"\nOriginal order : {names}")
names.sort()
print(f"Sorted order   : {names}")

# -------------------------------------------------------
# REAL USE: Quiz Answer Checker
# -------------------------------------------------------
print("\n--- Real Use: Quiz Answer Checker ---")
print("-" * 40)

questions = [
    ("What is the capital of India?", "New Delhi"),
    ("Who is called the God of Cricket?", "Sachin Tendulkar"),
]

score = 0
for question, correct in questions:
    print(f"\nQ: {question}")
    user_answer = input("Your answer: ")

    if user_answer.strip().lower() == correct.lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {correct}")

print(f"\nYour Score: {score}/{len(questions)}")

print("\n" + "=" * 55)
print("  KEY IDEAS:")
print("  • == checks exact match (case-sensitive)")
print("  • Use .lower() on both sides for case-insensitive check")
print("  • 'in' checks if text exists inside a string")
print("  • < > compare strings alphabetically")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. Is "Aarav" == "aarav" True or False? How do you fix it?
# 2. What does 'Mani' > 'Diya' return and why?
# 3. How do you check if "cricket" is mentioned in a sentence?
# 4. What does .strip() do before comparing? Why is it useful?
# ============================================================
