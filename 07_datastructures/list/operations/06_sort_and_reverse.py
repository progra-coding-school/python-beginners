# Program Code: 07-operations-06
# Title: Sorting and Reversing a List

# Sorting numbers
marks = [85, 42, 97, 63, 71]
print("Original marks:", marks)

# sort() - Ascending order (smallest to largest)
marks.sort()
print("Sorted (ascending):", marks)

# sort(reverse=True) - Descending order (largest to smallest)
marks.sort(reverse=True)
print("Sorted (descending):", marks)

# Sorting strings (alphabetical order)
names = ["Ravi", "Anita", "Kumar", "Deepa"]
print("\nOriginal names:", names)

names.sort()
print("Sorted (A to Z):", names)

# reverse() - Reverses the current order (does NOT sort)
names.reverse()
print("Reversed:", names)
