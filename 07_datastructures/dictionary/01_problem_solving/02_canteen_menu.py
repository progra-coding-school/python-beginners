# Program Code: DC-PS-02
# Title: Canteen Menu and Bill Calculator
# Cognitive Skill: Problem Solving
# Topic: Dictionaries in Python

# Problem:
# The school canteen has a menu with prices.
# A student orders multiple items.
# Calculate the total bill and show an itemised receipt.

# --- Step 1: Define the menu ---
menu = {
    "idli":       15,
    "dosa":       30,
    "vada":       20,
    "chai":       10,
    "sambar rice": 40,
    "juice":      25,
}

print("=== School Canteen Menu ===")
for item, price in menu.items():
    print(f"  {item:15} Rs.{price}")

print()

# --- Step 2: Student's order ---
# Dictionary: item → quantity ordered
order = {
    "idli":  2,
    "chai":  1,
    "juice": 2,
}

# --- Step 3: Check for items not in menu ---
print("=== Checking order ===")
valid_order   = {}
invalid_items = []

for item, qty in order.items():
    if item in menu:
        valid_order[item] = qty
    else:
        invalid_items.append(item)

if invalid_items:
    print(f"Sorry, these items are not available: {invalid_items}")

print()

# --- Step 4: Generate receipt ---
print("=== Receipt ===")
total = 0

for item, qty in valid_order.items():
    price    = menu[item]
    subtotal = price * qty
    total   += subtotal
    print(f"  {item:15} x{qty}  =  Rs.{subtotal}")

print(f"{'─' * 35}")
print(f"  {'TOTAL':20}     Rs.{total}")

# --- Step 5: Can Diya afford it? ---
diya_budget = 60
print()
if total <= diya_budget:
    print(f"Diya has Rs.{diya_budget}. She can afford the order!")
    print(f"Change returned: Rs.{diya_budget - total}")
else:
    print(f"Diya has Rs.{diya_budget}. She needs Rs.{total - diya_budget} more.")

# Think:
# 1. How would you add a 5% discount for orders above Rs.50?
# 2. How would you update the menu price of 'chai' from 10 to 12?
