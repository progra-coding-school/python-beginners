# Program Code: 07-operations-02
# Title: Adding Items to a List

# Three ways to add items: append, insert, extend

colors = ["red", "blue", "green"]
print("Original list:", colors)

# 1. append() - Adds one item at the END
colors.append("yellow")
print("After append('yellow'):", colors)

# 2. insert() - Adds one item at a SPECIFIC POSITION
colors.insert(1, "pink")
print("After insert(1, 'pink'):", colors)

# 3. extend() - Adds MULTIPLE items at the END
colors.extend(["black", "white"])
print("After extend(['black', 'white']):", colors)
