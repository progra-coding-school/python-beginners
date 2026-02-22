# Program Code: VAR-PS-01
# Title: Diya's Birthday Party Planner
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Variables in Python

# Big question: How much will the party cost?
# Break it into smaller questions — one variable each.

number_of_friends = int(input("How many friends is Diya inviting? "))

cost_per_plate = int(input("Cost of food per plate (Rs): "))
food_cost = number_of_friends * cost_per_plate
print("Food cost:", food_cost)

cake_cost = int(input("Cost of the birthday cake (Rs): "))
print("Cake cost:", cake_cost)

decoration_cost = int(input("Cost of decorations (Rs): "))
print("Decoration cost:", decoration_cost)

cost_per_gift = int(input("Cost of each return gift (Rs): "))
gift_cost = number_of_friends * cost_per_gift
print("Gift cost:", gift_cost)

total_cost = food_cost + cake_cost + decoration_cost + gift_cost
print("Total party cost:", total_cost)

# Think:
# 1. What new variable would you add if Diya also wanted a magician?
# 2. What other big problems in life can be broken into smaller parts?
