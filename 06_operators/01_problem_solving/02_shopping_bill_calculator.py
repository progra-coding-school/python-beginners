# Program Code: OP-PS-02
# Title: Amma's Shopping Bill Calculator
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Operators in Python

# Big question: What is the final bill after discounts and tax?
# Break it into smaller steps — one calculation at a time.

print("=== Shopping Bill Calculator ===")
print()

# Step 1: Get item prices
item1_name = input("Item 1 name: ")
item1_price = float(input(f"Price of {item1_name} (Rs): "))

item2_name = input("Item 2 name: ")
item2_price = float(input(f"Price of {item2_name} (Rs): "))

item3_name = input("Item 3 name: ")
item3_price = float(input(f"Price of {item3_name} (Rs): "))

# Step 2: Calculate subtotal
subtotal = item1_price + item2_price + item3_price
print(f"\nSubtotal: Rs.{subtotal}")

# Step 3: Apply discount (10% off if subtotal > 500)
if subtotal > 500:
    discount_percent = 10
    discount_amount = (subtotal * discount_percent) / 100
    print(f"Discount ({discount_percent}%): - Rs.{discount_amount}")
else:
    discount_amount = 0
    print("No discount (buy above Rs.500 to get 10% off)")

after_discount = subtotal - discount_amount

# Step 4: Add GST (5%)
gst_percent = 5
gst_amount = (after_discount * gst_percent) / 100
print(f"GST ({gst_percent}%): + Rs.{round(gst_amount, 2)}")

# Step 5: Final bill
final_bill = after_discount + gst_amount

# Step 6: Check if bill is even or odd (to see if exact change is needed)
is_exact_change = final_bill % 1 == 0

print(f"\n--- Final Bill ---")
print(f"{item1_name}: Rs.{item1_price}")
print(f"{item2_name}: Rs.{item2_price}")
print(f"{item3_name}: Rs.{item3_price}")
print(f"Total to pay: Rs.{round(final_bill, 2)}")

# Think:
# 1. What formula would you use to calculate per-person cost if 4 people are sharing?
# 2. How would you calculate how much change to return for a Rs.1000 note?
