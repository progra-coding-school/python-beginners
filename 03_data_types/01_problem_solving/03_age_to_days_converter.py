# Program Code: DT-PS-03
# Title: Age to Days Converter
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Data Types in Python

# Big question: Convert a person's age into total days lived.
# Break it into parts — one calculation per step.

# Step 1: Get inputs
name = input("Enter your name: ")
years = int(input("Enter your age in years: "))
months = int(input("Enter extra months (0-11): "))
days_extra = int(input("Enter extra days (0-30): "))

# Step 2: Convert each to days
years_in_days = years * 365
months_in_days = months * 30
total_days = years_in_days + months_in_days + days_extra

# Step 3: Convert to other units
weeks = total_days // 7
hours = total_days * 24
minutes = hours * 60

# Step 4: Display results
print(f"\n{name} has lived approximately:")
print(f"  {total_days} days")
print(f"  {weeks} weeks")
print(f"  {hours} hours")
print(f"  {minutes} minutes")

# Think:
# 1. Why are years, months, days all int and not float?
# 2. What if someone is 13.5 years old? How would you handle it?
# 3. We used 365 days/year and 30 days/month. Is this accurate? How would you improve it?
