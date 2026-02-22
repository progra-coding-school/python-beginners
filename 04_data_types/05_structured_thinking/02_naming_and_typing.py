# Program Code: DT-ST-02
# Title: Naming and Typing Go Together
# Cognitive Skill: Structured Thinking (Naming conventions)
# Topic: Data Types in Python

# Good variable names should hint at their type.
print("=== Good Naming Practices by Type ===\n")

# INTEGERS — names suggest counting or whole quantities
student_count = 35
total_runs = 247
birth_year = 2010

# FLOATS — names suggest measurement or precision
average_temperature = 28.5
price_per_kg = 45.75
gpa_score = 9.1

# STRINGS — names suggest text / identity
student_name = "Kavya"
city_name = "Coimbatore"
subject_code = "MAT101"

# BOOLEANS — names start with is_, has_, can_, should_
is_registered = True
has_paid = False
can_vote = False
is_above_average = True

print("Count variables (int):")
print(f"  student_count = {student_count}")
print(f"  total_runs = {total_runs}")

print("\nMeasurement variables (float):")
print(f"  average_temperature = {average_temperature}")
print(f"  price_per_kg = {price_per_kg}")

print("\nText variables (str):")
print(f"  student_name = {student_name}")
print(f"  city_name = {city_name}")

print("\nYes/No variables (bool):")
print(f"  is_registered = {is_registered}")
print(f"  has_paid = {has_paid}")

# BAD names — avoid these!
# x = 13             # What is x?
# data = "Chennai"   # Too vague
# temp = True        # temp usually means temperature!

# Think:
# 1. Suggest better names for: a = 9.8, b = True, c = "Raj"
# 2. What naming prefix tells you a variable is likely bool?
