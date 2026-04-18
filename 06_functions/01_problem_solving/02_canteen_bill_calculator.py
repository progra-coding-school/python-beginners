# Program Code: FN-PS-02
# Title: Canteen Bill Calculator
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Functions in Python

# Big question: How do we build a canteen billing system?
# Break it into one function per job.

# --- Menu prices ---
MENU = {
    "idli":    15,
    "dosa":    30,
    "rice":    40,
    "sambar":  10,
    "chai":    10,
    "juice":   25,
}

def show_menu():
    print("\n--- Canteen Menu ---")
    for item, price in MENU.items():
        print("  " + item.capitalize() + "  Rs." + str(price))
    print("-" * 20)

def get_item_price(item_name):
    item_name = item_name.lower()
    if item_name in MENU:
        return MENU[item_name]
    else:
        return 0   # item not found

def calculate_subtotal(items_ordered):
    # items_ordered = list of (item_name, quantity) tuples
    subtotal = 0
    for item, qty in items_ordered:
        price = get_item_price(item)
        subtotal += price * qty
    return subtotal

def apply_discount(subtotal):
    if subtotal >= 100:
        discount = subtotal * 0.10    # 10% off for orders >= Rs.100
        return discount
    return 0

def calculate_gst(amount):
    return amount * 0.05    # 5% GST

def print_bill(customer_name, items_ordered):
    subtotal = calculate_subtotal(items_ordered)
    discount = apply_discount(subtotal)
    after_discount = subtotal - discount
    gst = calculate_gst(after_discount)
    total = after_discount + gst

    print("    PROGRA CANTEEN BILL")
    print("    Customer:", customer_name)
    print("=" * 35)
    for item, qty in items_ordered:
        price = get_item_price(item)
        print("  " + item.capitalize() + " x" + str(qty) + "  Rs." + str(price * qty))
    print("-" * 35)
    print("  Subtotal:          Rs." + str(round(subtotal, 2)))
    if discount > 0:
        print("  Discount (10%):  - Rs." + str(round(discount, 2)))
    print("  GST (5%):        + Rs." + str(round(gst, 2)))
    print("  TOTAL:             Rs." + str(round(total, 2)))
    print("=" * 35)

# --- Run the canteen app ---
show_menu()

name = input("Your name: ")
order = []
while True:
    item = input("Add item (or 'done' to finish): ").lower()
    if item == "done":
        break
    if get_item_price(item) == 0:
        print("Item not found in menu.")
        continue
    qty = int(input("How many " + item + "s? "))
    order.append((item, qty))

print_bill(name, order)

# Think:
# 1. Which function would you change to add a new item to the menu?
# 2. What new function would you add to calculate change from a Rs.500 note?
