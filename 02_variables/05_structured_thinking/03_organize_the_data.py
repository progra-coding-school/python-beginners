# Program Code: CS-ST-03
# Title: Pongal Festival Expense Tracker
# Cognitive Skill: Structured Thinking (Organizing complex data systematically)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Amma is planning Pongal celebrations at home!
# There are SO many things to buy: rice, jaggery, flowers,
# sugarcane, kolam powder, new clothes, gifts...
# How do we organize ALL these expenses without getting confused?
# The SECRET: Group related things together using naming patterns!
# ============================================================

# ************************************************************
# ORGANIZING STRATEGY:
#
# We have 4 CATEGORIES of expenses:
#   1. PUJA items    -> prefix: puja_
#   2. FOOD items    -> prefix: food_
#   3. DECORATION    -> prefix: deco_
#   4. GIFTS         -> prefix: gift_
#
# By using prefixes, ALL puja items start with "puja_",
# ALL food items start with "food_", etc.
# This is like organizing your room: books on the shelf,
# clothes in the cupboard, toys in the box!
# ************************************************************

print("=== Pongal Festival Expense Tracker ===")
print("Let's organize Amma's Pongal shopping list!")
print()

# ---------- CATEGORY 1: PUJA ITEMS (prefix: puja_) ----------
print("--- Puja Items ---")
puja_camphor = int(input("  Camphor (Rs): "))
puja_incense = int(input("  Incense sticks (Rs): "))
puja_turmeric = int(input("  Turmeric & Kumkum (Rs): "))
puja_flowers = int(input("  Flowers for pooja (Rs): "))

puja_total = puja_camphor + puja_incense + puja_turmeric + puja_flowers
print(f"  Puja Total: Rs.{puja_total}")
print()

# ---------- CATEGORY 2: FOOD ITEMS (prefix: food_) ----------
print("--- Food Items ---")
food_rice = int(input("  Rice - new harvest (Rs): "))
food_jaggery = int(input("  Jaggery (Rs): "))
food_milk = int(input("  Milk (Rs): "))
food_dal = int(input("  Dal & Lentils (Rs): "))
food_vegetables = int(input("  Vegetables (Rs): "))

food_total = food_rice + food_jaggery + food_milk + food_dal + food_vegetables
print(f"  Food Total: Rs.{food_total}")
print()

# ---------- CATEGORY 3: DECORATIONS (prefix: deco_) ----------
print("--- Decorations ---")
deco_kolam = int(input("  Kolam powder & colors (Rs): "))
deco_mango_leaves = int(input("  Mango leaves (Rs): "))
deco_sugarcane = int(input("  Sugarcane (Rs): "))

deco_total = deco_kolam + deco_mango_leaves + deco_sugarcane
print(f"  Decoration Total: Rs.{deco_total}")
print()

# ---------- CATEGORY 4: GIFTS (prefix: gift_) ----------
print("--- Gifts ---")
gift_amma = int(input("  Gift for Amma (Rs): "))
gift_appa = int(input("  Gift for Appa (Rs): "))
gift_siblings = int(input("  Gift for siblings (Rs): "))

gift_total = gift_amma + gift_appa + gift_siblings
print(f"  Gift Total: Rs.{gift_total}")
print()

# ---------- GRAND TOTAL ----------
grand_total = puja_total + food_total + deco_total + gift_total

# Display organized summary
print("=" * 45)
print("    PONGAL EXPENSE SUMMARY")
print("=" * 45)
print(f"  Puja Items   : Rs.{puja_total}")
print(f"  Food Items   : Rs.{food_total}")
print(f"  Decorations  : Rs.{deco_total}")
print(f"  Gifts        : Rs.{gift_total}")
print("-" * 45)
print(f"  GRAND TOTAL  : Rs.{grand_total}")
print("=" * 45)
print()
print("Happy Pongal!")

# ============================================================
# REFLECTION PROMPTS:
# 1. We used 15+ variables but it was NOT confusing. Why?
#    (Hint: Look at the prefixes - puja_, food_, deco_, gift_)
#
# 2. What if we had named everything item1, item2, item3...
#    up to item15? Would you know which is kolam and which
#    is jaggery? WHY does grouping by prefix help?
#
# 3. This is like organizing a LIBRARY:
#    - Fiction books in one section
#    - Science books in another
#    - History books in another
#    How does your brain handle ORGANIZED information vs
#    MESSY information? Which is easier to work with?
# ============================================================
