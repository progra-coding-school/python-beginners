# Program Code: CS-PS-01
# Title: Diya's Birthday Party Planner
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Diya wants to throw a birthday party for her friends.
# But she has no idea how much it will cost!
# The total cost feels like one BIG question.
# Can you help her break it into SMALLER questions?
# ============================================================

# ------------------------------------------------------------
# DECOMPOSITION PLAN:
# Big Question: "How much will the party cost?"
#
# Smaller Questions:
#   1. How much will the FOOD cost?
#   2. How much will the CAKE cost?
#   3. How much will the DECORATIONS cost?
#   4. How much will the RETURN GIFTS cost?
#
# Each small question = one variable!
# ------------------------------------------------------------

print("=== Diya's Birthday Party Planner ===")
print()

# STEP 1: Gather information (break into smaller pieces)
number_of_friends = int(input("How many friends is Diya inviting? : "))

# STEP 2: Solve each small question separately
# Small Question 1: Food cost
cost_per_plate = int(input("Cost of food per plate (in Rs): "))
food_cost = number_of_friends * cost_per_plate
print(f"Food cost for {number_of_friends} friends = Rs.{food_cost}")

# Small Question 2: Cake cost
cake_cost = int(input("Cost of the birthday cake (in Rs): "))
print(f"Cake cost = Rs.{cake_cost}")

# Small Question 3: Decoration cost
decoration_cost = int(input("Cost of decorations - balloons, ribbons (in Rs): "))
print(f"Decoration cost = Rs.{decoration_cost}")

# Small Question 4: Return gifts cost
cost_per_gift = int(input("Cost of each return gift (in Rs): "))
gift_cost = number_of_friends * cost_per_gift
print(f"Return gifts for {number_of_friends} friends = Rs.{gift_cost}")

# STEP 3: Combine all the small answers into the big answer
print()
print("=" * 40)
print("PARTY BUDGET BREAKDOWN")
print("=" * 40)
total_cost = food_cost + cake_cost + decoration_cost + gift_cost
print(f"Food:        Rs.{food_cost}")
print(f"Cake:        Rs.{cake_cost}")
print(f"Decorations: Rs.{decoration_cost}")
print(f"Return Gifts:Rs.{gift_cost}")
print("-" * 40)
print(f"TOTAL COST:  Rs.{total_cost}")
print("=" * 40)

# ============================================================
# REFLECTION PROMPTS:
# 1. How many smaller questions did we break the big question into?
# 2. What new variable would you add if Diya also wanted
#    a magician show at the party?
# 3. Can you think of another big question in real life
#    that you could break into smaller pieces?
#    (Hint: Planning a school trip? Buying school supplies?)
# ============================================================
