# Program Code: OP-ST-03
# Title: Organise the Calculations
# Cognitive Skill: Structured Thinking (Data Organisation)
# Topic: Operators in Python

# Complex programs have many calculations.
# Organise them in logical groups — one purpose per section.

# PROBLEM: Plan a school trip budget

print("=== School Trip Budget Planner ===")
print()

# --- GROUP 1: Inputs ---
print("--- Trip Details ---")
num_students = int(input("Number of students: "))
num_teachers = int(input("Number of teachers: "))
destination = input("Destination: ")

# --- GROUP 2: Transport calculations ---
print("\n--- Transport ---")
bus_capacity = 45
buses_needed = (num_students + num_teachers) // bus_capacity
if (num_students + num_teachers) % bus_capacity > 0:
    buses_needed += 1   # one more bus for the remaining people

cost_per_bus = int(input(f"Cost per bus (Rs): "))
transport_cost = buses_needed * cost_per_bus

print(f"Total people: {num_students + num_teachers}")
print(f"Buses needed: {buses_needed}")
print(f"Transport cost: Rs.{transport_cost}")

# --- GROUP 3: Food calculations ---
print("\n--- Food ---")
cost_per_meal = int(input("Cost per meal per person (Rs): "))
meals_per_day = 3
days = int(input("Number of days: "))
food_cost = (num_students + num_teachers) * cost_per_meal * meals_per_day * days
print(f"Food cost ({days} days, {meals_per_day} meals/day): Rs.{food_cost}")

# --- GROUP 4: Entry and activities ---
print("\n--- Entry & Activities ---")
entry_fee_per_student = int(input("Entry fee per student (Rs): "))
entry_cost = num_students * entry_fee_per_student
print(f"Entry cost: Rs.{entry_cost}")

# --- GROUP 5: Total and per-student cost ---
print("\n--- Budget Summary ---")
total_cost = transport_cost + food_cost + entry_cost
per_student_cost = total_cost // num_students
extra_per_student = total_cost % num_students  # leftover Rs that can't be split evenly

print(f"Total trip cost: Rs.{total_cost}")
print(f"Cost per student: Rs.{per_student_cost}")
if extra_per_student > 0:
    print(f"Rs.{extra_per_student} to be covered by school fund")

# --- GROUP 6: Affordability check ---
print("\n--- Affordability ---")
budget_per_student = int(input("Maximum budget per student (Rs): "))
is_affordable = per_student_cost <= budget_per_student
overshoot = per_student_cost - budget_per_student

if is_affordable:
    savings = budget_per_student - per_student_cost
    print(f"Trip is affordable! Rs.{savings} savings per student.")
else:
    print(f"Over budget by Rs.{overshoot} per student.")
    print("Consider: fewer days, cheaper transport, or smaller group.")

# Think:
# 1. What new group of calculations would you add for 'souvenir/shopping budget'?
# 2. How would you calculate the total if the school subsidises 20% of the cost?
