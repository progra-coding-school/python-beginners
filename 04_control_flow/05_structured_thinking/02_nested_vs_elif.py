# Program Code: CF-ST-02
# Title: Nested if vs elif — Which to Use?
# Cognitive Skill: Structured Thinking (Choosing the right structure)
# Topic: Control Flow in Python

# Knowing WHEN to nest and when to use elif is key to clean code.
print("=== Nested if vs elif ===\n")

# SCENARIO 1: Movie ticket — age AND membership (two independent conditions)
print("--- Scenario 1: Use NESTED if ---")
age = int(input("Enter age: "))
is_member = input("Are you a member? (yes/no): ").lower() == "yes"

if age >= 18:
    if is_member:
        price = 100
        print(f"Adult member price: Rs.{price}")
    else:
        price = 150
        print(f"Adult price: Rs.{price}")
else:
    if is_member:
        price = 60
        print(f"Child member price: Rs.{price}")
    else:
        price = 80
        print(f"Child price: Rs.{price}")

input("\nPress Enter for Scenario 2...")

# SCENARIO 2: Grade — many mutually exclusive options
print("\n--- Scenario 2: Use elif ---")
marks = int(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 35:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

# RULE OF THUMB:
# Use elif   → when conditions are mutually exclusive (only one can be True)
# Use nested → when you need to check a second condition only AFTER the first

# Think:
# 1. Could you rewrite Scenario 1 using elif instead of nested if? Try it!
# 2. What would happen if you used separate 'if' instead of 'elif' for grades?
