# Program Code: 07-realworld-01
# Title: Grocery Shopping List

# Problem:
# Amma is going to the shop. She writes down items she needs.
# Sometimes she remembers more items and adds them.
# Sometimes she finds an item at home and removes it.
# Help Amma manage her grocery list!

grocery_list = ["rice", "dal", "oil", "salt"]
print("Amma's grocery list:", grocery_list)

# Amma remembers she needs milk and eggs
grocery_list.append("milk")
grocery_list.append("eggs")
print("After adding more items:", grocery_list)

# She found salt at home, no need to buy
grocery_list.remove("salt")
print("After removing salt:", grocery_list)

# She wants to buy sugar before dal (at index 1)
grocery_list.insert(1, "sugar")
print("After inserting sugar:", grocery_list)

# How many items to buy?
print("Total items to buy:", len(grocery_list))

# Print the shopping list nicely
print("\n--- Shopping List ---")
for i in range(len(grocery_list)):
    print(i + 1, ".", grocery_list[i])
