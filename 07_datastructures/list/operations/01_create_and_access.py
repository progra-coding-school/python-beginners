# Program Code: 07-operations-01
# Title: Create a List and Access Items

# A list is like a box with compartments.
# Each compartment has a position number called "index".
# Index starts from 0.

# Creating a list
fruits = ["apple", "banana", "mango", "orange", "grapes"]

# Print the whole list
print("All fruits:", fruits)

# Access items using index
print("First fruit (index 0):", fruits[0])
print("Second fruit (index 1):", fruits[1])
print("Third fruit (index 2):", fruits[2])

# Access from the end using negative index
print("Last fruit (index -1):", fruits[-1])
print("Second last fruit (index -2):", fruits[-2])

# How many items in the list?
print("Total fruits:", len(fruits))
