# Program Code: CF-UN-01
# Title: Why Control Flow Matters
# Cognitive Skill: Understanding
# Topic: Control Flow in Python

# ── WITHOUT control flow — rigid, no decisions, no repetition ─────────────
print("Hello")
print("My Name")
print("Is")
print("Daniel")
print("Jeganathan")
print("I am the teacher for this class")

# Problem: this always prints the same thing.
# No matter what happens, the output never changes.

# ── WITH control flow — code adapts ───────────────────────────────────────
print("--- With an if-else ---")
marks = 85
if marks >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")

# Change marks to 20 and the result changes automatically!

# ── WITHOUT loops — repetition is painful ─────────────────────────────────
print("--- Without a loop (printing 5 times) ---")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")

# ── WITH a loop — one block handles all repetition ────────────────────────
print("--- With a loop (same result, 1 line) ---")
for i in range(5):
    print("Hello World")

# Real-world impact — without loops, 100 students = 100 lines
print("--- With a loop (100 students) ---")
for i in range(1, 6):      # showing 1-5 as a sample
    print("Student", i)

# Real example: ATM PIN check
print("--- ATM PIN check ---")
correct_pin = "1234"
entered_pin = input("Enter your PIN: ")
if entered_pin == correct_pin:
    print("Access granted.")
else:
    print("Wrong PIN. Access denied.")

# Think:
# 1. Name a real app (Swiggy, WhatsApp, etc.) and describe 3 if-else decisions it makes.
# 2. Aarav wants to print marks for all 40 students.
#    Should he use a loop or 40 print statements? Why?
