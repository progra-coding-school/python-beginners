# Two-Day Attendance Checker
# Problem: a 2-day workshop — track who attended each day using set operations.
# Answer: who came both days, day-1 only, day-2 only, at least one day, and who missed both.

# --- Data ---
full_class = {"Aarav", "Diya", "Karthik", "Riya", "Ananya", "Vivek", "Priya", "Arjun"}

day1 = {"Aarav", "Diya", "Karthik", "Ananya", "Priya"}
day2 = {"Diya", "Riya", "Karthik", "Vivek", "Ananya"}

print("2-Day Workshop Attendance:")
print("Full class :", sorted(full_class))
print("Day 1      :", sorted(day1))
print("Day 2      :", sorted(day2))
print()

# --- Q1: Attended BOTH days ---
# Intersection — only students who appear in BOTH day sets
both_days = day1 & day2
print("Attended BOTH days        :", sorted(both_days))
print("  →", len(both_days), "students get full certificate")

print()

# --- Q2: Day 1 ONLY ---
# day1 - day2 removes anyone who also came on day 2
day1_only = day1 - day2
print("Day 1 only (missed Day 2) :", sorted(day1_only))

# --- Q3: Day 2 ONLY ---
day2_only = day2 - day1
print("Day 2 only (missed Day 1) :", sorted(day2_only))

print()

# --- Q4: At least one day ---
# Union — anyone who appeared on day1 OR day2 (or both)
at_least_one = day1 | day2
print("Attended at least one day :", sorted(at_least_one))
print("  →", len(at_least_one), "students attended something")

print()

# --- Q5: Missed BOTH days ---
# Subtract all attendees from the full class — whoever is left was absent both days
missed_both = full_class - at_least_one
print("Missed BOTH days          :", sorted(missed_both))
print("  →", len(missed_both), "students need to be contacted")

print()

# --- Summary Report ---
print("Summary Report:")
print("  Full class size     :", len(full_class))
print("  Full certificate    :", len(both_days))
print("  Partial attendance  :", len(at_least_one - both_days))
print("  Absent both days    :", len(missed_both))

# Think:
# 1. How would you extend this for a 5-day workshop to find who attended ALL 5 days?
# 2. Which students should receive a "follow-up" email? Write the logic.
