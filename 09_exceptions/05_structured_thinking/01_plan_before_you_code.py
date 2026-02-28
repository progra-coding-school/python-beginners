# Program Code: EX-ST-01
# Title: Plan Before You Code
# Cognitive Skill: Structured Thinking
# Topic: Exceptions in Python

# Task: Build a canteen order system that never crashes.
# Before writing code, plan all possible failure points.

# ─── PLANNING TEMPLATE ───────────────────────────────────────────
# Problem  : Process canteen orders — item name and quantity.
# Inputs   : item name (str), quantity (str from user)
# Outputs  : Order confirmation or clear error message
# Failure points to handle:
#   1. Quantity is not a number          → ValueError
#   2. Quantity is negative or zero      → ValueError (raise manually)
#   3. Item not in the menu              → KeyError / custom check
#   4. Quantity exceeds available stock  → custom check
# Steps    :
#   1. Define the menu with prices and stock
#   2. Parse and validate the quantity
#   3. Check item exists in menu
#   4. Check sufficient stock
#   5. Confirm order and update stock
# ─────────────────────────────────────────────────────────────────

print("=== Canteen Order System ===")

# --- Step 1: Menu ---
menu = {
    "idli"  : {"price": 15, "stock": 10},
    "dosa"  : {"price": 30, "stock":  5},
    "chai"  : {"price": 10, "stock": 20},
    "vada"  : {"price": 20, "stock":  0},   # out of stock!
}

# --- Step 2–5: Place an order with full error handling ---
def place_order(item_name, qty_str):
    print(f"\nOrder: {qty_str}x '{item_name}'")
    try:
        # Step 2: parse quantity
        qty = int(qty_str)
        if qty <= 0:
            raise ValueError("Quantity must be at least 1.")

        # Step 3: check item exists
        if item_name not in menu:
            raise KeyError(f"'{item_name}' is not on the menu.")

        # Step 4: check stock
        item = menu[item_name]
        if item["stock"] < qty:
            raise ValueError(
                f"Only {item['stock']} '{item_name}' left. Requested {qty}."
            )

        # Step 5: confirm
        total  = item["price"] * qty
        item["stock"] -= qty
        print(f"  Order confirmed! {qty}x {item_name} = Rs.{total}")
        print(f"  Stock remaining: {item['stock']}")

    except ValueError as e:
        print(f"  Invalid order: {e}")
    except KeyError as e:
        print(f"  Menu error: {e}")

# --- Demo ---
place_order("idli",   "3")      # valid
place_order("dosa",   "10")     # exceeds stock
place_order("chai",   "abc")    # not a number
place_order("vada",   "2")      # out of stock
place_order("pizza",  "1")      # not on menu
place_order("chai",   "-2")     # negative quantity
place_order("chai",   "5")      # valid (after others)

# Think:
# 1. Write the failure points list for a "school fee payment" system.
# 2. Why is it important to validate quantity BEFORE checking stock?
