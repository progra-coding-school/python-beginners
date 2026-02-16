# Program Code: 07-operations-05
# Title: Searching and Counting in a List

vegetables = ["carrot", "potato", "tomato", "onion", "potato", "beans"]
print("Vegetables:", vegetables)

# 1. 'in' keyword - Check if an item EXISTS in the list
if "tomato" in vegetables:
    print("Yes! tomato is in the list")

if "mushroom" in vegetables:
    print("mushroom is in the list")
else:
    print("No! mushroom is NOT in the list")

# 2. index() - Find the POSITION of an item
position = vegetables.index("onion")
print("onion is at index:", position)

# 3. count() - Count how many TIMES an item appears
potato_count = vegetables.count("potato")
print("potato appears", potato_count, "times")
