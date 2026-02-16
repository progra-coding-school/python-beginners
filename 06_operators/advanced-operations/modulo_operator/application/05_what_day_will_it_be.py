# File Name: 05_what_day_will_it_be.py

# Title: What Day Will It Be?
# Problem Statement:
# Today is a certain day of the week (e.g., Monday).
# Your friend says: "Let's meet after 'N' days!"
# Write a program to find out what day of the week it will be after N days.
#
# Hint: There are 7 days in a week. Use modulo (%) with 7.
#
# Example:
#   Today is Monday (Day 1). After 10 days => 10 % 7 = 3
#   Move 3 days from Monday => Thursday
#
# Days: 1=Monday, 2=Tuesday, 3=Wednesday, 4=Thursday,
#        5=Friday, 6=Saturday, 7=Sunday

# Solution:

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("Days: 1=Monday, 2=Tuesday, 3=Wednesday, 4=Thursday, 5=Friday, 6=Saturday, 7=Sunday")
today = int(input("Enter today's day number (1-7): "))
after_days = int(input("Enter how many days later: "))

# today is 1-based, so subtract 1 to get index, add after_days, then modulo 7
future_day_index = (today - 1 + after_days) % 7

print("Today is:", days_of_week[today - 1])
print("After", after_days, "days, it will be:", days_of_week[future_day_index])
