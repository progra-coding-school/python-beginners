# Program Code: CL-ST-01
# Title: Plan Before You Code
# Cognitive Skill: Structured Thinking
# Topic: Classes and Objects in Python

# Task: Design a Canteen class before writing any code.

# ─── PLANNING TEMPLATE ───────────────────────────────────────────
# Problem  : A school canteen needs to manage its menu and process orders.
# Class    : Canteen
#
# Attributes (what it HAS):
#   - name        : str  — canteen name
#   - menu        : dict — item → {price, stock}
#   - total_sales : float — running total
#
# Methods (what it CAN DO):
#   - add_item(name, price, stock)  — add a new menu item
#   - order(item, qty)              — process an order
#   - restock(item, qty)            — add more stock
#   - display_menu()                — print current menu
#   - report()                      — print sales summary
#
# Edge cases:
#   - Order item not on menu
#   - Order quantity exceeds stock
#   - Restock negative quantity
# ─────────────────────────────────────────────────────────────────

class Canteen:
    def __init__(self, name):
        self.name        = name
        self.menu        = {}
        self.total_sales = 0

    def add_item(self, item, price, stock):
        self.menu[item] = {"price": price, "stock": stock}
        print(f"  Added '{item}' — Rs.{price}, {stock} in stock.")

    def display_menu(self):
        print(f"\n  === {self.name} Menu ===")
        print(f"  {'Item':<15} {'Price':>6} {'Stock':>6}")
        print(f"  {'─'*15} {'─'*6} {'─'*6}")
        for item, info in self.menu.items():
            print(f"  {item:<15} Rs.{info['price']:>3} {info['stock']:>6}")

    def order(self, item, qty):
        if item not in self.menu:
            print(f"  '{item}' is not on the menu.")
            return 0
        info = self.menu[item]
        if qty > info["stock"]:
            print(f"  Only {info['stock']} '{item}' left. Cannot fulfill {qty}.")
            return 0
        cost = info["price"] * qty
        info["stock"] -= qty
        self.total_sales += cost
        print(f"  Order: {qty}x {item} = Rs.{cost}")
        return cost

    def restock(self, item, qty):
        if item not in self.menu:
            print(f"  '{item}' not found.")
            return
        if qty <= 0:
            print("  Restock quantity must be positive.")
            return
        self.menu[item]["stock"] += qty
        print(f"  Restocked '{item}' by {qty}.")

    def report(self):
        print(f"\n  === Sales Report — {self.name} ===")
        print(f"  Total Sales: Rs.{self.total_sales}")
        low = [i for i, d in self.menu.items() if d["stock"] < 5]
        if low:
            print(f"  Low stock alert: {low}")

# --- Demo ---
canteen = Canteen("Progra School Canteen")

canteen.add_item("idli",   15, 20)
canteen.add_item("dosa",   30, 10)
canteen.add_item("chai",   10, 30)
canteen.add_item("vada",   20,  4)

canteen.display_menu()
print()

canteen.order("idli", 3)
canteen.order("dosa", 2)
canteen.order("chai", 5)
canteen.order("vada", 5)       # exceeds stock
canteen.order("pizza", 1)      # not on menu

canteen.restock("vada", 10)
canteen.report()

# Think:
# 1. Write the planning template for a "Cricket Team" class before coding it.
# 2. Why is it useful to plan attributes and methods BEFORE writing any code?
