# Program Code: CF-PS-04
# Title: Fruit and Vegetable Price Finder
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Control Flow in Python

# Big question: Build a price lookup system for a local market.
# Break it down: get item → check each option → display price or error.

print("=== Local Market Price Finder ===\n")

# Step 1: Show available items
print("Available items:")
print("  Fruits  : apple, banana, mango, grapes, orange")
print("  Veggies : carrot, tomato, potato, onion, beans")
print()

# Step 2: Keep asking until user types 'done'
while True:
    item = input("Enter item name (or 'done' to exit): ").lower().strip()

    if item == "done":
        print("Thank you for visiting!")
        break

    # Step 3: Check item and display price (if-elif-else)
    elif item == "apple":
        print(f"  Apple    → ₹100 per kg")
    elif item == "banana":
        print(f"  Banana   → ₹40 per dozen")
    elif item == "mango":
        print(f"  Mango    → ₹120 per kg")
    elif item == "grapes":
        print(f"  Grapes   → ₹80 per kg")
    elif item == "orange":
        print(f"  Orange   → ₹60 per kg")
    elif item == "carrot":
        print(f"  Carrot   → ₹30 per kg")
    elif item == "tomato":
        print(f"  Tomato   → ₹25 per kg")
    elif item == "potato":
        print(f"  Potato   → ₹20 per kg")
    elif item == "onion":
        print(f"  Onion    → ₹35 per kg")
    elif item == "beans":
        print(f"  Beans    → ₹55 per kg")
    else:
        # Step 4: Handle unknown items
        print(f"  '{item}' is not in our list. Please try another item.")

# Think:
# 1. Why is a while loop used here instead of a for loop?
# 2. What happens if the user types "Apple" (capital A) instead of "apple"?
#    Why does .lower() fix this?
# 3. Can you add a quantity feature? (e.g. user enters "apple 2" → ₹200)
# 4. How would you store all the prices in a dictionary instead of elif chains?
