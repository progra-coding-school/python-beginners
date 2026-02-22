# Program Code: OP-ST-01
# Title: Plan Before You Code — Salary Calculator
# Cognitive Skill: Structured Thinking (Planning)
# Topic: Operators in Python

# Before coding, always plan:
# 1. What are the INPUTS?
# 2. What CALCULATIONS are needed?
# 3. What COMPARISONS/LOGIC are needed?
# 4. What is the OUTPUT?

# PROBLEM: Calculate an employee's take-home salary.
#
# PLAN:
# INPUT:
#   - employee_name (str)
#   - basic_salary (float)
#   - years_of_service (int)
#
# CALCULATIONS (arithmetic):
#   - hra = basic_salary * 0.20          (20% of basic)
#   - da = basic_salary * 0.10           (10% of basic)
#   - gross_salary = basic_salary + hra + da
#   - pf_deduction = basic_salary * 0.12 (12% of basic)
#   - tax = gross_salary * 0.05          (5% tax)
#   - total_deductions = pf_deduction + tax
#   - net_salary = gross_salary - total_deductions
#
# LOGIC (comparison + logical):
#   - is_senior = years_of_service >= 5
#   - if is_senior: add Rs.2000 bonus
#   - if net_salary < 10000: no tax (small salary exemption)
#
# OUTPUT:
#   - Display full salary breakdown

# ---- CODE FOLLOWS THE PLAN ----

print("=== Employee Salary Calculator ===")
employee_name = input("Employee name: ")
basic_salary = float(input("Basic salary (Rs): "))
years_of_service = int(input("Years of service: "))

# Allowances (arithmetic)
hra = basic_salary * 0.20
da = basic_salary * 0.10
gross_salary = basic_salary + hra + da

# Deductions (arithmetic + comparison)
pf_deduction = basic_salary * 0.12

# Logic: small salary exemption
if gross_salary < 10000:
    tax = 0
else:
    tax = gross_salary * 0.05

total_deductions = pf_deduction + tax
net_salary = gross_salary - total_deductions

# Logic: senior bonus
is_senior = years_of_service >= 5
if is_senior:
    net_salary = net_salary + 2000
    bonus_note = "+ Rs.2000 (senior bonus)"
else:
    bonus_note = ""

# Output
print(f"\n--- Salary Slip: {employee_name} ---")
print(f"Basic Salary:     Rs. {basic_salary:.2f}")
print(f"HRA (20%):        Rs. {hra:.2f}")
print(f"DA (10%):         Rs. {da:.2f}")
print(f"Gross Salary:     Rs. {gross_salary:.2f}")
print(f"PF (12%):       - Rs. {pf_deduction:.2f}")
print(f"Tax (5%):       - Rs. {tax:.2f}")
print(f"Net Salary:       Rs. {net_salary:.2f} {bonus_note}")

# Think:
# 1. What two more deductions could a real salary slip have?
# 2. How would you add a performance rating bonus (e.g., rating 5 → 10% extra)?
