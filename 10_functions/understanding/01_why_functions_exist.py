# Program Code: FN-UN-01
# Title: Why Functions Exist
# Cognitive Skill: Understanding
# Topic: Functions in Python

# Without functions: code is repeated, hard to fix, hard to read.
# With functions: write once, use anywhere — clean and powerful.

print("=== WITHOUT Functions — Repeated Code ===")
# Calculate grade for 3 students — writing same logic 3 times!
marks1 = 85
if marks1 >= 90:
    grade1 = "A+"
elif marks1 >= 80:
    grade1 = "A"
elif marks1 >= 35:
    grade1 = "B"
else:
    grade1 = "FAIL"
print(f"Aarav: {marks1} → {grade1}")

marks2 = 62
if marks2 >= 90:
    grade2 = "A+"
elif marks2 >= 80:
    grade2 = "A"
elif marks2 >= 35:
    grade2 = "B"
else:
    grade2 = "FAIL"
print(f"Diya:  {marks2} → {grade2}")

marks3 = 28
if marks3 >= 90:
    grade3 = "A+"
elif marks3 >= 80:
    grade3 = "A"
elif marks3 >= 35:
    grade3 = "B"
else:
    grade3 = "FAIL"
print(f"Riya:  {marks3} → {grade3}")

print()
print("Problem: If the grade boundary changes, we must fix it in 3 places!")
print()

print("=== WITH Functions — Write Once, Use Anywhere ===")

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 35:
        return "B"
    else:
        return "FAIL"

print(f"Aarav: 85 → {get_grade(85)}")
print(f"Diya:  62 → {get_grade(62)}")
print(f"Riya:  28 → {get_grade(28)}")

print()
print("Benefit: If the boundary changes → fix in ONE place. Done!")
print()

# --- 3 Reasons Functions Exist ---
print("=== Why Functions? ===")
print("1. REUSE: Write once, call as many times as needed")
print("2. READABILITY: Code reads like sentences — get_grade(85)")
print("3. EASY TO FIX: Change logic in ONE place, affects all calls")

# Think:
# 1. In a restaurant billing app, which 3 things would you make into functions?
# 2. What would break if Python didn't have functions?
