# Program Code: VAR-KN-04
# Title: Arithmetic Operators
# Cognitive Skill: Knowledge
# Topic: Variables in Python

# Amma buys 8 samosas at Rs. 5 each.

samosas = 8
price = 5

total_cost = samosas * price       # multiplication
print("Total cost:", total_cost)

change = 50 - total_cost           # subtraction
print("Change from Rs.50:", change)

per_person = total_cost / 2        # division — always gives float
print("Per person:", per_person)

full_boxes = samosas // 3          # floor division — whole number only
print("Full boxes of 3:", full_boxes)

leftover = samosas % 3             # modulo — remainder
print("Leftover:", leftover)

area = 4 ** 2                      # exponentiation — 4 squared
print("Area (4x4):", area)

# All 7 operators:
# +   addition
# -   subtraction
# *   multiplication
# /   division (always float: 10/2 = 5.0)
# //  floor division (whole number: 10//3 = 3)
# %   remainder (10%3 = 1)
# **  power (2**3 = 8)
