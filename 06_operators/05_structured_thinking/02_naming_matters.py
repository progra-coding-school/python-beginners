# Program Code: OP-ST-02
# Title: Naming Matters — Clear vs Confusing Operator Code
# Cognitive Skill: Structured Thinking (Naming Conventions)
# Topic: Operators in Python

# Good naming makes operator expressions readable.
# Bad naming makes them a mystery to everyone (including future-you!).

# --- Example 1: Cricket calculation ---

# BAD — what do x, y, z mean?
x = 5
y = 3
z = 12
r = x * 4 + y * 6 + z
print("Bad code result:", r)

# GOOD — self-documenting names
fours_hit = 5
sixes_hit = 3
singles = 12
boundary_runs = (fours_hit * 4) + (sixes_hit * 6)
total_runs = boundary_runs + singles
print("Good code result:", total_runs)
print()

# --- Example 2: Discount calculation ---

# BAD
p = 1200
d = p * 15 / 100
f = p - d
print("Final:", f)

# GOOD
original_price = 1200
discount_percent = 15
discount_amount = original_price * discount_percent / 100
final_price = original_price - discount_amount
print(f"Original: Rs.{original_price}")
print(f"Discount ({discount_percent}%): Rs.{discount_amount}")
print(f"Final price: Rs.{final_price}")
print()

# --- Example 3: Eligibility check ---

# BAD — what is a, b, c?
a = 82
b = 90
c = True
if a >= 75 and b >= 75 and c:
    print("OK")

# GOOD
maths_marks = 82
english_marks = 90
attendance_ok = True
if maths_marks >= 75 and english_marks >= 75 and attendance_ok:
    print("Student is eligible for the scholarship!")
print()

# --- Golden Rules ---
print("=== Naming Rules for Operator Expressions ===")
print("1. Use full words: 'discount_amount' not 'd'")
print("2. Break long formulas: store intermediate results in named variables")
print("3. Boolean variables: use is_, has_, can_ prefix")
print("   e.g., is_eligible, has_ticket, can_vote")
print("4. Avoid magic numbers: store 0.12 as 'pf_rate = 0.12'")
print()

# BAD: magic number
salary = 50000
deduction = salary * 0.12    # what is 0.12?

# GOOD: named constant
PF_RATE = 0.12
pf_deduction = salary * PF_RATE
print(f"PF deduction at {int(PF_RATE*100)}%: Rs.{pf_deduction}")

# Think:
# 1. Rename these variables clearly: a=10, b=3, c=a*b, d=c+7
# 2. What prefix would you use for a variable that stores "is the exam online"?
