# Program Code: OP-HOT-03
# Title: Operator Quiz Game
# Cognitive Skill: Higher Order Thinking (Creative Synthesis)
# Topic: Operators in Python

# A complete operator quiz game — tests ALL operator types!
# Synthesizes knowledge of arithmetic, comparison, logical, and precedence.

import random

print("╔═══════════════════════════════════╗")
print("║   Progra Operator Quiz Game!     ║")
print("╚═══════════════════════════════════╝")

name = input("Enter your name: ")
score = 0
total_questions = 8

print(f"\nWelcome, {name}! Answer all {total_questions} questions.\n")

# --- Q1: Arithmetic ---
print(f"Q1: What is 17 % 5?")
ans = input("Your answer: ").strip()
if ans == "2":
    print("Correct! 17 ÷ 5 = 3 remainder 2")
    score += 1
else:
    print("Wrong! 17 % 5 = 2 (remainder after dividing 17 by 5)")
print()

# --- Q2: Floor division ---
print(f"Q2: What is 29 // 4?")
ans = input("Your answer: ").strip()
if ans == "7":
    print("Correct! 29 ÷ 4 = 7.25 → floor = 7")
    score += 1
else:
    print("Wrong! 29 // 4 = 7 (remove decimal)")
print()

# --- Q3: Exponent ---
print(f"Q3: What is 2 ** 5?")
ans = input("Your answer: ").strip()
if ans == "32":
    print("Correct! 2^5 = 2×2×2×2×2 = 32")
    score += 1
else:
    print("Wrong! 2 ** 5 = 32")
print()

# --- Q4: Comparison ---
print(f"Q4: What does (10 == 10.0) return? (True/False)")
ans = input("Your answer: ").strip()
if ans.lower() == "true":
    print("Correct! Python considers 10 == 10.0 as True (int vs float, same value)")
    score += 1
else:
    print("Wrong! 10 == 10.0 → True (value is the same)")
print()

# --- Q5: Logical ---
print(f"Q5: What does (True and False or True) return? (True/False)")
ans = input("Your answer: ").strip()
actual = True and False or True
if ans.lower() == str(actual).lower():
    print(f"Correct! True and False = False. False or True = True.")
    score += 1
else:
    print(f"Wrong! True and False = False, then False or True = True")
print()

# --- Q6: Precedence ---
print(f"Q6: What is 2 + 3 * 4 - 1?")
ans = input("Your answer: ").strip()
actual = 2 + 3 * 4 - 1
if ans == str(actual):
    print(f"Correct! 3*4=12 first, then 2+12-1={actual}")
    score += 1
else:
    print(f"Wrong! 3*4=12 first, then 2+12-1={actual}")
print()

# --- Q7: Modulo use case ---
print(f"Q7: Which expression checks if a number n is even?")
print("  A: n % 2 == 0")
print("  B: n // 2 == 0")
print("  C: n / 2 == 0")
ans = input("Your answer (A/B/C): ").strip().upper()
if ans == "A":
    print("Correct! n % 2 == 0 → remainder is 0 → even")
    score += 1
else:
    print("Wrong! Answer is A: n % 2 == 0")
print()

# --- Q8: Logical reasoning ---
print(f"Q8: age = 14, has_ticket = True")
print(f"    What does (age >= 18 or has_ticket) return? (True/False)")
ans = input("Your answer: ").strip()
age = 14
has_ticket = True
actual = age >= 18 or has_ticket
if ans.lower() == str(actual).lower():
    print(f"Correct! age >= 18 → False. has_ticket → True. False or True = True")
    score += 1
else:
    print(f"Wrong! False or True = True")
print()

# Final score
print("═" * 40)
print(f"Final Score: {score} / {total_questions}")
if score == total_questions:
    print(f"PERFECT! Outstanding, {name}!")
elif score >= 6:
    print(f"Great job, {name}! You know your operators!")
elif score >= 4:
    print(f"Good effort, {name}! Review the ones you missed.")
else:
    print(f"Keep practising, {name}! Operators are key to Python!")
print("═" * 40)
