# Program Code: OUT-PS-02
# Title: Receipt Printer
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Output in Python

# Big question: How do we display a clean, real-looking shop receipt?
# Break it into output sections — one section at a time.

# Step 1: Shop and customer info
shop_name    = "Amma's Kirana Store"
customer     = input("Customer name: ")
phone        = input("Phone number: ")

# Step 2: Items purchased
print("\nEnter items (press Enter with no name to finish):")
items = []
while True:
    item_name = input("  Item name (or Enter to stop): ")
    if item_name == "":
        break
    item_price = float(input(f"  Price of {item_name} (Rs): "))
    item_qty   = int(input(f"  Quantity: "))
    items.append((item_name, item_price, item_qty))

# Step 3: Calculate totals
subtotal = sum(price * qty for _, price, qty in items)
discount = subtotal * 0.05 if subtotal > 500 else 0
gst      = (subtotal - discount) * 0.05
total    = subtotal - discount + gst

# Step 4: Print the receipt
width = 36
print()
print("=" * width)
print(f"{shop_name:^{width}}")
print(f"{'Serving you with love!':^{width}}")
print("-" * width)
print(f"  Customer : {customer}")
print(f"  Phone    : {phone}")
print("-" * width)
print(f"  {'Item':<14} {'Qty':>3} {'Price':>7} {'Total':>7}")
print("-" * width)

for name, price, qty in items:
    line_total = price * qty
    print(f"  {name:<14} {qty:>3} {price:>7.2f} {line_total:>7.2f}")

print("-" * width)
print(f"  {'Subtotal':<22} {subtotal:>7.2f}")
if discount > 0:
    print(f"  {'Discount (5%)':<22} -{discount:>6.2f}")
print(f"  {'GST (5%)':<22} {gst:>7.2f}")
print("=" * width)
print(f"  {'TOTAL':<22} Rs.{total:>6.2f}")
print("=" * width)
print(f"{'Thank you! Visit again!':^{width}}")
print("=" * width)

# Think:
# 1. What would you add to show the date and time on the receipt?
# 2. How would you show "SAVINGS: Rs.X" if the discount was applied?
