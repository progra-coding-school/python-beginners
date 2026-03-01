# Mini Inventory System
# A nested dictionary tracks a shop's entire stock.
# Structure: product name → {"price": ..., "qty": ...}
# KEY IDEA: each product's data is grouped together in its own inner dict.
# Operations: display, sell (reduce qty), restock (increase qty), low-stock alert.

# Inventory: product → {price per unit, quantity in stock}
inventory = {
    "pens":      {"price": 10,  "qty": 50},
    "notebooks": {"price": 45,  "qty": 30},
    "erasers":   {"price":  5,  "qty": 80},
    "rulers":    {"price": 20,  "qty": 15},
    "colours":   {"price": 60,  "qty":  8},
}

def display_inventory():
    # Show each product with its price, quantity, and total value
    print("  " + "Product".ljust(12) + "Price".rjust(8) + "Qty".rjust(5) + "Value".rjust(9))
    print("  " + "-" * 34)
    for product, data in inventory.items():
        value = data["price"] * data["qty"]
        print("  " + product.ljust(12) +
              ("Rs." + str(data["price"])).rjust(8) +
              str(data["qty"]).rjust(5) +
              ("Rs." + str(value)).rjust(9))

def total_inventory_value():
    # sum() with a generator — multiply price × qty for each product and add all up
    return sum(d["price"] * d["qty"] for d in inventory.values())

def sell(product, qty):
    if product not in inventory:
        print("  '" + product + "' not in inventory.")
        return
    if inventory[product]["qty"] < qty:
        print("  Not enough stock for '" + product + "'. Available:", inventory[product]["qty"])
        return
    inventory[product]["qty"] -= qty           # reduce stock by amount sold
    earned = inventory[product]["price"] * qty
    print("  Sold", qty, "'" + product + "' for Rs." + str(earned) + ".")

def restock(product, qty):
    if product in inventory:
        inventory[product]["qty"] += qty       # increase stock
        print("  Restocked '" + product + "' by", qty, "— new qty:", inventory[product]["qty"])
    else:
        print("  '" + product + "' not found. Add it first before restocking.")

def low_stock_alert(threshold=10):
    # Warn about any product with fewer units than the threshold
    print("  Products with stock below", str(threshold) + ":")
    found = False
    for product, data in inventory.items():
        if data["qty"] < threshold:
            print("    ! " + product + ": only", data["qty"], "left!")
            found = True
    if not found:
        print("    All products are well stocked.")

print("Shop Inventory System")
print()

print("Current Inventory:")
display_inventory()
print("  Total inventory value: Rs." + str(total_inventory_value()))
print()

print("Selling items:")
sell("pens", 20)
sell("colours", 5)
sell("rulers", 20)    # exceeds stock — prints a warning instead of crashing
print()

print("After sales:")
display_inventory()
print("  Total inventory value: Rs." + str(total_inventory_value()))
print()

print("Low stock check:")
low_stock_alert(threshold=10)
print()

print("Restocking colours:")
restock("colours", 50)
low_stock_alert(threshold=10)
