# Program Code: SE-PS-03
# Title: Two-Day Attendance Checker
# Cognitive Skill: Problem Solving
# Topic: Sets in Python

# Problem:
# The school held a 2-day workshop.
# Track who attended each day and answer:
# 1. Who came BOTH days? (full attendance)
# 2. Who came on DAY 1 only?
# 3. Who came on DAY 2 only?
# 4. Who came on AT LEAST one day?
# 5. Who MISSED both days? (from the full class list)

# --- Data ---
full_class = {"Aarav", "Diya", "Karthik", "Riya", "Ananya", "Vivek", "Priya", "Arjun"}

day1 = {"Aarav", "Diya", "Karthik", "Ananya", "Priya"}
day2 = {"Diya", "Riya", "Karthik", "Vivek", "Ananya"}

print("=== 2-Day Workshop Attendance ===")
print(f"Full class : {sorted(full_class)}")
print(f"Day 1      : {sorted(day1)}")
print(f"Day 2      : {sorted(day2)}")
print()

# --- Q1: Attended BOTH days ---
both_days = day1 & day2
print(f"Attended BOTH days        : {sorted(both_days)}")
print(f"  → {len(both_days)} students get full certificate")

print()

# --- Q2: Day 1 ONLY ---
day1_only = day1 - day2
print(f"Day 1 only (missed Day 2) : {sorted(day1_only)}")

# --- Q3: Day 2 ONLY ---
day2_only = day2 - day1
print(f"Day 2 only (missed Day 1) : {sorted(day2_only)}")

print()

# --- Q4: At least one day ---
at_least_one = day1 | day2
print(f"Attended at least one day : {sorted(at_least_one)}")
print(f"  → {len(at_least_one)} students attended something")

print()

# --- Q5: Missed BOTH days ---
missed_both = full_class - at_least_one
print(f"Missed BOTH days          : {sorted(missed_both)}")
print(f"  → {len(missed_both)} students need to be contacted")

print()

# --- Summary Report ---
print("=== Summary Report ===")
print(f"  Full class size     : {len(full_class)}")
print(f"  Full certificate    : {len(both_days)}")
print(f"  Partial attendance  : {len(at_least_one - both_days)}")
print(f"  Absent both days    : {len(missed_both)}")

# Think:
# 1. How would you extend this for a 5-day workshop to find who attended ALL 5 days?
# 2. Which students should receive a "follow-up" email? Write the logic.
