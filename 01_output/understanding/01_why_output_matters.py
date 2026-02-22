# Program Code: OUT-UN-01
# Title: Why Output Matters
# Cognitive Skill: Understanding
# Topic: Output in Python

# A program that doesn't show anything is useless to the user.
# Output is how your program communicates with the world.

print("=== WITHOUT output — silent program ===")

# This code runs but shows NOTHING:
name = "Aarav"
age = 13
total = 85 + 90 + 78
average = total / 3
# ... calculations happen inside, but the user sees nothing!

print("(The program ran, but you saw nothing. Was it useful? No!)")
print()

print("=== WITH output — program talks to the user ===")

name = "Aarav"
age = 13
marks = [85, 90, 78]
total = sum(marks)
average = total / len(marks)

print(f"Student:  {name}")
print(f"Age:      {age}")
print(f"Total:    {total}/300")
print(f"Average:  {average:.1f}")
if average >= 80:
    print("Result:   Distinction!")
else:
    print("Result:   Pass")
print()

print("=== Output serves 3 purposes ===")
print()

print("1. INFORM — tell the user what happened")
print("   e.g., 'Payment of Rs.500 received successfully!'")
print()

print("2. GUIDE — show what to do next")
print("   e.g., 'Enter your PIN:'")
print()

print("3. PRESENT — display data in a readable way")
print("   e.g., a formatted report card or receipt")
print()

# --- Without formatting vs with formatting ---
print("=== Bad output vs Good output ===")
print()

# Bad — raw, unreadable
print("bad:", "Aarav", 85, 90, 78, 253, 84.3)

# Good — clear and structured
print("good:")
print(f"  Name:    Aarav")
print(f"  Maths:   85")
print(f"  Science: 90")
print(f"  English: 78")
print(f"  Total:   253 / 300")
print(f"  Average: 84.3")

# Think:
# 1. Think of an app on your phone. What 3 types of output does it show you?
# 2. What would happen if Google Maps showed no output when you searched for directions?
