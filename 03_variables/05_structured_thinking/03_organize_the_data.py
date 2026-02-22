# Program Code: VAR-ST-03
# Title: Pongal Festival Expense Tracker
# Cognitive Skill: Structured Thinking (Organizing data)
# Topic: Variables in Python

# Strategy: group related variables using prefixes
# puja_ for puja items, food_ for food, deco_ for decorations, gift_ for gifts

# Puja items
print("--- Puja Items ---")
puja_camphor = int(input("Camphor (Rs): "))
puja_incense = int(input("Incense sticks (Rs): "))
puja_turmeric = int(input("Turmeric and Kumkum (Rs): "))
puja_flowers = int(input("Flowers (Rs): "))
puja_total = puja_camphor + puja_incense + puja_turmeric + puja_flowers
print("Puja total:", puja_total)

# Food items
print("--- Food Items ---")
food_rice = int(input("Rice (Rs): "))
food_jaggery = int(input("Jaggery (Rs): "))
food_milk = int(input("Milk (Rs): "))
food_dal = int(input("Dal (Rs): "))
food_vegetables = int(input("Vegetables (Rs): "))
food_total = food_rice + food_jaggery + food_milk + food_dal + food_vegetables
print("Food total:", food_total)

# Decorations
print("--- Decorations ---")
deco_kolam = int(input("Kolam powder (Rs): "))
deco_mango_leaves = int(input("Mango leaves (Rs): "))
deco_sugarcane = int(input("Sugarcane (Rs): "))
deco_total = deco_kolam + deco_mango_leaves + deco_sugarcane
print("Decoration total:", deco_total)

# Gifts
print("--- Gifts ---")
gift_amma = int(input("Gift for Amma (Rs): "))
gift_appa = int(input("Gift for Appa (Rs): "))
gift_siblings = int(input("Gift for siblings (Rs): "))
gift_total = gift_amma + gift_appa + gift_siblings
print("Gift total:", gift_total)

# Grand total
grand_total = puja_total + food_total + deco_total + gift_total
print("Puja:", puja_total)
print("Food:", food_total)
print("Decorations:", deco_total)
print("Gifts:", gift_total)
print("Grand total:", grand_total)
print("Happy Pongal!")

# Think:
# 1. We had 15+ variables but it wasn't confusing. Why? (Look at the prefixes.)
# 2. What if we had named everything item1, item2...item15?
#    Would you know which is kolam and which is jaggery?
