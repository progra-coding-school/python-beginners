# Program Code: CF-PS-01
# Title: Movie Ticket Price Calculator
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Control Flow in Python

# Big question: Calculate the correct ticket price based on age and day.
# Break it into decisions — one condition at a time.

# Step 1: Get inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))
day = input("Enter day (weekday/weekend): ").lower()

# Step 2: Base price by age group
if age < 5:
    price = 0
    category = "Child (free)"
elif age <= 12:
    price = 80
    category = "Child"
elif age <= 60:
    price = 150
    category = "Adult"
else:
    price = 100
    category = "Senior"

# Step 3: Weekend surcharge
if day == "weekend":
    price = price + 30
    surcharge_note = " (includes Rs.30 weekend surcharge)"
else:
    surcharge_note = ""

# Step 4: Display ticket
print(f"\n--- Ticket for {name} ---")
print(f"Category: {category}")
print(f"Day: {day.capitalize()}")
print(f"Price: Rs.{price}{surcharge_note}")

# Think:
# 1. What new condition would you add for a 'student discount' (age 13-22)?
# 2. Can you add a loyalty card condition: if has_card → 10% off?
