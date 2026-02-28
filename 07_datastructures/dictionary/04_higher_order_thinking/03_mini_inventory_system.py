# Program Code: DC-HOT-03
# Title: Mini Inventory System
# Cognitive Skill: Higher Order Thinking
# Topic: Dictionaries in Python

# Design challenge:
# Build a shop inventory tracker.
# Each product has: price and quantity.
# Support: restock, sell, check low stock, total value.

# --- Inventory: product → {price, qty} ---
inventory = {
    "pens":      {"price": 10,  "qty": 50},
    "notebooks": {"price": 45,  "qty": 30},
    "erasers":   {"price":  5,  "qty": 80},
    "rulers":    {"price": 20,  "qty": 15},
    "colours":   {"price": 60,  "qty":  8},
}

# --- Functions ---

def display_inventory():
    print(f"  {'Product':<12} {'Price':>7} {'Qty':>5} {'Value':>8}")
    print(f"  {'─'*12} {'─'*7} {'─'*5} {'─'*8}")
    for product, data in inventory.items():
        value = data["price"] * data["qty"]
        print(f"  {product:<12} Rs.{data['price']:>4} {data['qty']:>5}  Rs.{value:>5}")

def total_inventory_value():
    return sum(d["price"] * d["qty"] for d in inventory.values())

def sell(product, qty):
    if product not in inventory:
        print(f"  '{product}' not in inventory.")
        return
    if inventory[product]["qty"] < qty:
        print(f"  Not enough stock for '{product}'. Available: {inventory[product]['qty']}")
        return
    inventory[product]["qty"] -= qty
    earned = inventory[product]["price"] * qty
    print(f"  Sold {qty} '{product}' for Rs.{earned}.")

def restock(product, qty):
    if product in inventory:
        inventory[product]["qty"] += qty
        print(f"  Restocked '{product}' by {qty}. New qty: {inventory[product]['qty']}")
    else:
        print(f"  '{product}' not found. Use add_product() to create it first.")

def low_stock_alert(threshold=10):
    print(f"  Products with stock below {threshold}:")
    found = False
    for product, data in inventory.items():
        if data["qty"] < threshold:
            print(f"    ⚠  {product}: only {data['qty']} left!")
            found = True
    if not found:
        print("    All products are well stocked.")

# --- Demo ---
print("=== Shop Inventory System ===")
print()

print("--- Current Inventory ---")
display_inventory()
print(f"\n  Total inventory value: Rs.{total_inventory_value()}")
print()

print("--- Selling items ---")
sell("pens", 20)
sell("colours", 5)
sell("rulers", 20)    # exceeds stock
print()

print("--- After sales ---")
display_inventory()
print(f"\n  Total inventory value: Rs.{total_inventory_value()}")
print()

print("--- Low stock check ---")
low_stock_alert(threshold=10)
print()

print("--- Restocking colours ---")
restock("colours", 50)
low_stock_alert(threshold=10)

# Think:
# 1. How would you add a discount field to each product?
# 2. If the shop had 500 products, would a dictionary still be the right choice? Why?
