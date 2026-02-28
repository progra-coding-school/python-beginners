# Program Code: SE-ST-01
# Title: Plan Before You Code
# Cognitive Skill: Structured Thinking
# Topic: Sets in Python

# Task: Build a "Who is absent today?" checker.
# Before writing code, answer the planning questions.

# ─── PLANNING TEMPLATE ───────────────────────────────────────────
# Problem  : Given a class roll and today's attendees, find who is absent.
# Inputs   : Full class set, today's present set
# Outputs  : Absent students, attendance percentage
# Structure: Two sets — full_class and present; difference gives absent
# Steps    :
#   1. Define the full class as a set
#   2. Define who is present today as a set
#   3. Use set difference to find absent students
#   4. Calculate attendance percentage
#   5. Display the report
# Edge cases: What if everyone is present? What if an unknown name appears?
# ─────────────────────────────────────────────────────────────────

print("=== Daily Attendance Checker ===")

# --- Step 1: Full class ---
full_class = {"Aarav", "Diya", "Karthik", "Riya", "Ananya", "Vivek", "Priya", "Arjun"}

# --- Step 2: Today's attendees ---
present_today = {"Aarav", "Diya", "Karthik", "Ananya", "Priya"}

# --- Step 3: Who is absent? ---
absent = full_class - present_today
print(f"Present  ({len(present_today)}): {sorted(present_today)}")
print(f"Absent   ({len(absent)})     : {sorted(absent)}")

# --- Step 4: Percentage ---
percentage = (len(present_today) / len(full_class)) * 100
print(f"Attendance: {percentage:.1f}%")

# --- Step 5: Edge case — unknown name in swipe list ---
print()
print("=== Edge case: Unknown student ===")
swipes = {"Aarav", "Diya", "Karthik", "Ananya", "Priya", "Unknown_Student"}
valid_present = swipes & full_class           # only those in the class
unknown       = swipes - full_class           # anyone NOT in class
print(f"Valid attendees : {sorted(valid_present)}")
print(f"Unknown swipes  : {unknown}")

# --- Edge case — everyone present ---
print()
print("=== Edge case: Full attendance ===")
if absent:
    print(f"Missing: {sorted(absent)}")
else:
    print("Full attendance today! Everyone is present.")

# Think:
# 1. Write the 5-step plan for a "Find common members across 3 clubs" problem.
# 2. What would change in Step 3 if you wanted who was present yesterday but absent today?
