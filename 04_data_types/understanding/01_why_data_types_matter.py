# Program Code: DT-UN-01
# Title: Why Data Types Matter
# Cognitive Skill: Understanding
# Topic: Data Types in Python

# PROBLEM: What happens when you ignore types?

# Attempt 1: storing age as a string
age = "13"
# age + 1     → ERROR: cannot add str and int

# Attempt 2: storing name as a number (impossible)
# name = Aarav   → ERROR: Aarav is not a number

# WITH the right types — everything works
name = "Aarav"     # str — for text
age = 13           # int — for whole numbers
height = 5.4       # float — for decimals
is_eligible = True # bool — for yes/no

print("Name:", name)
print("Age:", age)
print("Age next year:", age + 1)  # works!
print("Height:", height)
print("Eligible:", is_eligible)

# REAL BUG: input() gives a STRING even if user types a number
user_input = "20"                    # this is what input() gives
# total = 100 + user_input          # ERROR!
total = 100 + int(user_input)        # correct!
print("Total:", total)

# ANOTHER REAL EXAMPLE: price display vs. price calculation
price_display = "49.99"              # for showing on screen
price_value = float(price_display)  # for calculations
discounted = price_value * 0.9
print("Discounted price:", discounted)

# Think:
# 1. If you store a phone number as int, what happens to a number like 9876543210?
#    (Hint: try it!) Why is str better for phone numbers?
# 2. Name one variable where float is better than int. Explain why.
