# Program Code: TU-FC-03
# Title: Memory Recall Challenge
# Cognitive Skill: Focus and Concentration
# Topic: Tuples in Python

# Study the tuples below for 30 seconds.
# Then scroll down and answer questions FROM MEMORY.
# Run to verify!

# ─── Memorise these tuples ───────────────────────────────────────
students = (
    (101, "Aarav",   7, "Chennai",    85),
    (102, "Diya",    6, "Madurai",    92),
    (103, "Karthik", 8, "Coimbatore", 78),
    (104, "Riya",    7, "Trichy",     88),
    (105, "Ananya",  6, "Chennai",    95),
)
# Fields: (id, name, grade, city, score)

print("=== Study These Records (30 seconds) ===")
print(f"  {'ID':>4}  {'Name':<10} {'Grade':>5} {'City':<12} {'Score':>5}")
print(f"  {'─'*4}  {'─'*10} {'─'*5} {'─'*12} {'─'*5}")
for rec in students:
    print(f"  {rec[0]:>4}  {rec[1]:<10} {rec[2]:>5} {rec[3]:<12} {rec[4]:>5}")

print()
print("─" * 50)
print("Answer from memory — then verify by running!")
print("─" * 50)
print()

# --- Q1: How many student records? ---
print(f"Q1: Total records = {len(students)}")

# --- Q2: What is Diya's score? ---
diya = next(r for r in students if r[1] == "Diya")
print(f"Q2: Diya's score  = {diya[4]}")

# --- Q3: Which student is in Grade 8? ---
grade8 = [r[1] for r in students if r[2] == 8]
print(f"Q3: Grade 8       = {grade8}")

# --- Q4: What city is student ID 104 from? ---
s104 = next(r for r in students if r[0] == 104)
print(f"Q4: ID 104 city   = {s104[3]}")

# --- Q5: Who has the highest score? ---
top = max(students, key=lambda r: r[4])
print(f"Q5: Top scorer    = {top[1]} ({top[4]})")

# --- Q6: How many students are from Chennai? ---
chennai_count = sum(1 for r in students if r[3] == "Chennai")
print(f"Q6: From Chennai  = {chennai_count}")

# --- Q7: Average score? ---
avg = sum(r[4] for r in students) / len(students)
print(f"Q7: Average score = {avg:.1f}")

print()
print("─" * 50)
print("Score yourself:")
print("  7/7 → Exceptional focus!")
print("  5-6 → Great — minor lapses.")
print("  3-4 → Good — re-study with 45 seconds next time.")
print("  0-2 → Slow down — read row by row and visualise.")

# Think:
# 1. Which field was hardest to remember — ID, city, or score? Why?
# 2. How would a real database let you look up a record by ID instantly?
