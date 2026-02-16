# Program Code: CS-ST-01
# Title: Amma's Chai Stall Calculator
# Cognitive Skill: Structured Thinking (Plan first, then code)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Amma is running a chai stall at the school fair!
# She sells Chai, Samosa, and Biscuits.
# She needs a calculator to figure out the total bill.
# But BEFORE we write code, we must PLAN!
# What variables do we need? How should we organize them?
# ============================================================

# ************************************************************
# PLANNING SECTION - READ THIS FIRST!
#
# A good coder plans BEFORE writing code, just like
# a builder draws a blueprint before building a house.
#
# STEP 1: What CATEGORIES of variables do I need?
#   Category 1: PRICES  (how much each item costs)
#   Category 2: QUANTITIES (how many the customer wants)
#   Category 3: TOTALS (cost for each item)
#   Category 4: FINAL BILL (everything combined)
#
# STEP 2: What VARIABLES go in each category?
#
#   PRICES:
#     chai_price       = 10 (Rs per cup)
#     samosa_price     = 15 (Rs per piece)
#     biscuit_price    = 5  (Rs per packet)
#
#   QUANTITIES (from customer input):
#     chai_qty         = ? (how many cups)
#     samosa_qty       = ? (how many samosas)
#     biscuit_qty      = ? (how many packets)
#
#   ITEM TOTALS:
#     chai_total       = chai_price x chai_qty
#     samosa_total     = samosa_price x samosa_qty
#     biscuit_total    = biscuit_price x biscuit_qty
#
#   FINAL:
#     bill_total       = chai_total + samosa_total + biscuit_total
#
# STEP 3: Total variables needed = 10
#
# Now we are READY to code! The plan is our guide.
# ************************************************************

print("=== Amma's Chai Stall - School Fair ===")
print()

# --- PRICES (Category 1) ---
# These are fixed - Amma decided the prices
chai_price = 10
samosa_price = 15
biscuit_price = 5

# Show the menu
print("-------- MENU --------")
print(f"  Chai    : Rs.{chai_price}/cup")
print(f"  Samosa  : Rs.{samosa_price}/piece")
print(f"  Biscuit : Rs.{biscuit_price}/packet")
print("----------------------")
print()

# --- QUANTITIES (Category 2) ---
# These come from the customer
print("What would you like to order?")
chai_qty = int(input(f"  How many Chai?    : "))
samosa_qty = int(input(f"  How many Samosa?  : "))
biscuit_qty = int(input(f"  How many Biscuit? : "))

# --- ITEM TOTALS (Category 3) ---
chai_total = chai_price * chai_qty
samosa_total = samosa_price * samosa_qty
biscuit_total = biscuit_price * biscuit_qty

# --- FINAL BILL (Category 4) ---
bill_total = chai_total + samosa_total + biscuit_total

# Print the bill
print()
print("=" * 35)
print("  AMMA'S CHAI STALL - BILL")
print("=" * 35)
print(f"  Chai    x{chai_qty}  = Rs.{chai_total}")
print(f"  Samosa  x{samosa_qty}  = Rs.{samosa_total}")
print(f"  Biscuit x{biscuit_qty}  = Rs.{biscuit_total}")
print("-" * 35)
print(f"  TOTAL      = Rs.{bill_total}")
print("=" * 35)
print("  Thank you! Come again!")

# ============================================================
# REFLECTION PROMPTS:
# 1. Look at the PLANNING SECTION above the code.
#    Did having a plan make the coding easier?
#    What if you had started coding without any plan?
#
# 2. We organized variables into 4 CATEGORIES:
#    Prices, Quantities, Item Totals, Final Bill.
#    Why is grouping things into categories helpful?
#    (Hint: Imagine finding a book in a library with no sections!)
#
# 3. Challenge: Amma wants to add "Vada" (Rs.12) to the menu.
#    Write the plan FIRST (what new variables do you need?),
#    THEN add the code. Planning habit = coding superpower!
# ============================================================
