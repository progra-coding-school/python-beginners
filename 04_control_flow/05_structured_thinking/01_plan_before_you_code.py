# Program Code: CF-ST-01
# Title: Diya's Canteen Order System
# Cognitive Skill: Structured Thinking (Plan first, then code)
# Topic: Control Flow in Python

# PLAN BEFORE CODING:
# Step 1: Show menu (print prices)
# Step 2: Keep taking orders until user types 'done'
# Step 3: For each item, check if it's in the menu (if-elif-else)
# Step 4: Add valid items to total; warn for invalid items
# Step 5: Display final bill

# MENU PRICES
idli_price = 15
dosa_price = 30
sambar_rice_price = 40
juice_price = 25

print("=== Diya's Canteen ===")
print(f"Idli: Rs.{idli_price}")
print(f"Dosa: Rs.{dosa_price}")
print(f"Sambar Rice: Rs.{sambar_rice_price}")
print(f"Juice: Rs.{juice_price}")
print("Type 'done' when finished ordering.\n")

total = 0
items_ordered = []

# Step 2-4: Loop until 'done'
while True:
    item = input("Enter item: ").lower().strip()

    if item == "done":
        break
    elif item == "idli":
        total += idli_price
        items_ordered.append("Idli")
    elif item == "dosa":
        total += dosa_price
        items_ordered.append("Dosa")
    elif item == "sambar rice":
        total += sambar_rice_price
        items_ordered.append("Sambar Rice")
    elif item == "juice":
        total += juice_price
        items_ordered.append("Juice")
    else:
        print(f"'{item}' is not on the menu. Try again.")

# Step 5: Bill
print("\n--- Your Order ---")
for i, o in enumerate(items_ordered, 1):
    print(f"  {i}. {o}")
print(f"Total: Rs.{total}")
print("Thank you!")

# Think:
# 1. What happens if the user types 'done' as the first item?
# 2. Can you add quantity support? (e.g. "2 idli" = Rs.30)
