# Program Code: OUT-PS-02
# Title: Receipt Printer
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Output in Python

# Big question: How do we display a clean, real-looking shop receipt?
# Break it into output sections — one section at a time.

# Helper to format money with 2 decimal places
def money(n):
    n = round(n, 2)
    s = str(n)
    if "." not in s:
        return s + ".00"
    decimals = s.split(".")[1]
    if len(decimals) == 1:
        return s + "0"
    return s

# Step 1: Shop and customer info
shop_name = "Amma's Kirana Store"
customer  = input("Customer name: ")
phone     = input("Phone number: ")

# Step 2: Items purchased
print("\nEnter items (press Enter with no name to finish):")
items = []
while True:
    item_name = input("  Item name (or Enter to stop): ")
    if item_name == "":
        break
    item_price = float(input("  Price of " + item_name + " (Rs): "))
    item_qty   = int(input("  Quantity: "))
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
print(shop_name.center(width))
print("Serving you with love!".center(width))
print("-" * width)
print("  Customer : " + customer)
print("  Phone    : " + phone)
print("-" * width)
print("  " + "Item".ljust(14) + " " + "Qty".rjust(3) + " " + "Price".rjust(7) + " " + "Total".rjust(7))
print("-" * width)

for name, price, qty in items:
    line_total = price * qty
    print("  " + name.ljust(14) + " " + str(qty).rjust(3) + " " + money(price).rjust(7) + " " + money(line_total).rjust(7))

print("-" * width)
print("  " + "Subtotal".ljust(22) + " " + money(subtotal).rjust(7))
if discount > 0:
    print("  " + "Discount (5%)".ljust(22) + " -" + money(discount).rjust(6))
print("  " + "GST (5%)".ljust(22) + " " + money(gst).rjust(7))
print("=" * width)
print("  " + "TOTAL".ljust(22) + " Rs." + money(total).rjust(6))
print("=" * width)
print("Thank you! Visit again!".center(width))
print("=" * width)

# Think:
# 1. What would you add to show the date and time on the receipt?
# 2. How would you show "SAVINGS: Rs.X" if the discount was applied?
