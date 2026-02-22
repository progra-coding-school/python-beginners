# Program Code: LP-ST-01
# Title: Plan Before You Code — Library Fine Calculator
# Cognitive Skill: Structured Thinking (Planning)
# Topic: Loops in Python

# Always plan your loop BEFORE writing code:
# - What are we looping OVER? (a list, a range, until a condition)
# - What happens EACH iteration?
# - What do we ACCUMULATE or TRACK?
# - When do we STOP?

# PROBLEM: Calculate library fines for all borrowers.
#
# PLAN:
# DATA: list of (student_name, book_title, days_overdue)
# LOOP: for each borrower in the list
#   - Calculate fine: days_overdue * Rs.2 per day
#   - Flag if fine > Rs.50 (heavy fine)
# ACCUMULATE: total fines collected
# OUTPUT: individual fine + total summary

# ---- CODE FOLLOWS THE PLAN ----

borrowers = [
    ("Aarav",   "Python for Kids",    3),
    ("Diya",    "Maths Made Easy",    0),
    ("Karthik", "Science Explorer",  15),
    ("Riya",    "Story of Pi",        7),
    ("Aman",    "Code Your World",    0),
    ("Priya",   "History of India",  28),
]

FINE_PER_DAY   = 2      # Rs.2 per overdue day
HEAVY_FINE_LIMIT = 50   # Flag if fine exceeds Rs.50

print("=== Library Fine Report ===")
print(f"  {'Name':12} {'Book':22} {'Days':5} {'Fine':8} {'Status'}")
print("  " + "-" * 60)

total_fines = 0
heavy_fine_count = 0

for name, book, days in borrowers:
    fine = days * FINE_PER_DAY
    total_fines += fine

    if days == 0:
        status = "On time"
    elif fine > HEAVY_FINE_LIMIT:
        status = "HEAVY FINE"
        heavy_fine_count += 1
    else:
        status = "Overdue"

    print(f"  {name:12} {book:22} {days:5}   Rs.{fine:4}  {status}")

print("  " + "-" * 60)
print(f"  Total fines collected: Rs.{total_fines}")
print(f"  Heavy fine cases:      {heavy_fine_count}")

if heavy_fine_count > 0:
    print(f"\n  ⚠ {heavy_fine_count} student(s) have heavy fines. Please follow up.")

# Think:
# 1. How would you modify this to sort by highest fine first?
# 2. What loop change would you make to apply a 50% discount for first-time offenders?
