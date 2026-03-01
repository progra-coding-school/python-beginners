# Why Output Matters
# A program that shows nothing is useless to the user.
# Output is how your program communicates results, guides actions, and presents data.

# --- Without output — the program runs but the user sees nothing ---
# These calculations happen silently inside Python:
# 85 + 90 + 78 = 253
# 253 / 3 = 84.3
# ... all correct, but the user sees nothing!

print("(The program ran, but you saw nothing. Was it useful? No!)")
print()

# --- With output — the program talks to the user ---
# Same data, now presented clearly so the user can understand it
print("Student:  Aarav")
print("Age:      13")
print("Total:    253/300")
print("Average:  84.3")
if 84.3 >= 80:
    print("Result:   Distinction!")
else:
    print("Result:   Pass")
print()

# --- Output serves 3 purposes ---

# 1. INFORM — tell the user what happened
print("1. INFORM — tell the user what happened")
print("   e.g., 'Payment of Rs.500 received successfully!'")
print()

# 2. GUIDE — show what to do next (like a menu or prompt)
print("2. GUIDE — show what to do next")
print("   e.g., 'Enter your PIN:'")
print()

# 3. PRESENT — display data in a readable, structured way
print("3. PRESENT — display data in a readable way")
print("   e.g., a formatted report card or receipt")
print()

# --- Without formatting vs with formatting ---
# Bad output is technically correct but unusable; good output is clear and scannable

# Bad — raw, unreadable: numbers with no context
print("bad:", "Aarav", 85, 90, 78, 253, 84.3)

# Good — same data, structured with labels and spacing
print("good:")
print("  Name:    Aarav")
print("  Maths:   85")
print("  Science: 90")
print("  English: 78")
print("  Total:   253 / 300")
print("  Average: 84.3")

# Think:
# 1. Think of an app on your phone. What 3 types of output does it show you?
# 2. What would happen if Google Maps showed no output when you searched for directions?
