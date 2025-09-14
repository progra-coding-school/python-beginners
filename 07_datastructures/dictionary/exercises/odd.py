"""
Program: Operations on a Dictionary of Odd Numbers
Description:
    Create a dictionary 'odd_numbers' of odd numbers between 1 and 10,
    where the key is the number and the value is the number in words.
    Perform common dictionary operations: access, add, delete, check membership,
    loop through items, get keys/values, and clear the dictionary.
"""

# Step 1: Create the dictionary
odd_numbers = {
    1: "One",
    3: "Three",
    5: "Five",
    7: "Seven",
    9: "Nine"
}
print("Initial dictionary:", odd_numbers)

# Step 2: Access a value by key
print("Value for key 3:", odd_numbers[3])

# Step 3: Add a new key-value pair
odd_numbers[11] = "Eleven"
print("After adding 11:", odd_numbers)

# Step 4: Delete a key-value pair
del odd_numbers[5]   # Remove key 5
print("After deleting 5:", odd_numbers)

# Step 5: Check membership of a key
print("Is 7 in dictionary?", 7 in odd_numbers)         # True
print("Is 2 not in dictionary?", 2 not in odd_numbers) # True

# Step 6: Loop through items
print("All key-value pairs:")
for num, word in odd_numbers.items():
    print(f"{num} → {word}")

# Step 7: Get all keys and values
print("Keys:", odd_numbers.keys())
print("Values:", odd_numbers.values())

# Step 8: Clear the dictionary
odd_numbers.clear()
print("After clearing:", odd_numbers)



