# Program Code: 07-operations-07
# Title: Slicing a List

# Slicing lets you pick a PORTION of the list
# Syntax: list[start:end]  (end is NOT included)

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print("Full list:", numbers)

# Get items from index 1 to 4 (index 4 is NOT included)
print("numbers[1:4] =>", numbers[1:4])

# Get first 3 items
print("numbers[:3]  =>", numbers[:3])

# Get items from index 4 to end
print("numbers[4:]  =>", numbers[4:])

# Get last 3 items
print("numbers[-3:] =>", numbers[-3:])

# Get every 2nd item
print("numbers[::2] =>", numbers[::2])
