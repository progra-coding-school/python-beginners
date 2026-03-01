# Plan Before You Code
# Task: build a "Who is absent today?" checker using set operations.
# Before writing code, answer the planning questions — then implement step by step.

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

print("Daily Attendance Checker:")

# --- Step 1: Full class ---
full_class = {"Aarav", "Diya", "Karthik", "Riya", "Ananya", "Vivek", "Priya", "Arjun"}

# --- Step 2: Today's attendees ---
present_today = {"Aarav", "Diya", "Karthik", "Ananya", "Priya"}

# --- Step 3: Who is absent? ---
# Set difference: full_class - present_today = students NOT yet present
absent = full_class - present_today
print("Present  (" + str(len(present_today)) + "):", sorted(present_today))
print("Absent   (" + str(len(absent)) + ")     :", sorted(absent))

# --- Step 4: Percentage ---
percentage = (len(present_today) / len(full_class)) * 100
print("Attendance:", str(round(percentage, 1)) + "%")

# --- Step 5: Edge case — unknown name in swipe list ---
# A badge swipe might include someone not on the class roll — filter them out
print()
print("Edge case: Unknown student:")
swipes = {"Aarav", "Diya", "Karthik", "Ananya", "Priya", "Unknown_Student"}
valid_present = swipes & full_class           # only those actually in the class
unknown       = swipes - full_class           # anyone NOT in the class
print("Valid attendees :", sorted(valid_present))
print("Unknown swipes  :", unknown)

# --- Edge case — everyone present ---
# Check before printing "missing" — handle the happy path cleanly
print()
print("Edge case: Full attendance:")
if absent:
    print("Missing:", sorted(absent))
else:
    print("Full attendance today! Everyone is present.")

# Think:
# 1. Write the 5-step plan for a "Find common members across 3 clubs" problem.
# 2. What would change in Step 3 if you wanted who was present yesterday but absent today?
