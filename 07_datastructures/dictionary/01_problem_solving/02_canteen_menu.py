# Canteen Menu and Bill Calculator
# Two dictionaries work together: menu (item → price) and order (item → quantity).
# Step-by-step problem:
#   1. Display the menu
#   2. Validate the order — check each item exists in the menu
#   3. Generate a receipt — price × quantity for each item
#   4. Check if the student's budget is enough

# Step 1: The menu dictionary — item name → price in rupees
menu = {
    "idli":        15,
    "dosa":        30,
    "vada":        20,
    "chai":        10,
    "sambar rice": 40,
    "juice":       25,
}

print("School Canteen Menu:")
for item, price in menu.items():
    print("  " + item.ljust(15) + " Rs." + str(price))

print()

# Step 2: The student's order — item → quantity ordered
order = {
    "idli":  2,
    "chai":  1,
    "juice": 2,
}

# Validate: split into valid items (in the menu) and invalid items (not on menu)
print("Checking order:")
valid_order   = {}
invalid_items = []

for item, qty in order.items():
    if item in menu:          # 'in' checks if the key exists in the dict
        valid_order[item] = qty
    else:
        invalid_items.append(item)

if invalid_items:
    print("Sorry, these items are not available:", invalid_items)

print()

# Step 3: Generate the receipt — price × quantity per item
print("Receipt:")
total = 0

for item, qty in valid_order.items():
    price    = menu[item]         # look up price from the menu dict
    subtotal = price * qty
    total   += subtotal
    print("  " + item.ljust(15) + " x" + str(qty) + "  =  Rs." + str(subtotal))

print("  " + "-" * 35)
print("  " + "TOTAL".ljust(20) + "     Rs." + str(total))

# Step 4: Check if Diya can afford her order
diya_budget = 60
print()
if total <= diya_budget:
    print("Diya has Rs." + str(diya_budget) + ". She can afford the order!")
    print("Change returned: Rs." + str(diya_budget - total))
else:
    print("Diya has Rs." + str(diya_budget) + ". She needs Rs." + str(total - diya_budget) + " more.")
