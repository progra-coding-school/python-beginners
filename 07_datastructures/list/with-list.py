# Program Code:07-02
# Exercise:with-list.py
# Instructions:
# Create a list called fruits and add 4 fruits.
# Print all fruits using a loop.
# Add a new fruit to the list.
# Change the second fruit to something else.
# Remove one fruit from the list.

fruits = ["apple", "banana", "mango", "orange"]
print(fruits)

#Accessing Items:
print(fruits[0])  # apple
print(fruits[2])  # mango

# ------------------ ADDING ITEMS ------------------

# append() - Add to the end
fruits.append("pineapple")
print("After append:", fruits)

# insert() - Add at specific index
fruits.insert(1, "kiwi")
print("After insert at index 1:", fruits)

# extend() - Add multiple items
fruits.extend(["grape", "melon"])
print("After extend:", fruits)

# ------------------ REMOVING ITEMS ------------------

# remove() - Remove by value
fruits.remove("banana")
print("After remove 'banana':", fruits)

# pop() - Remove by index (and return it)
removed_item = fruits.pop(2)
print(f"After pop index 2 (removed {removed_item}):", fruits)

# clear() - Remove all items
temp_list = fruits.copy()  # making a copy to clear separately
temp_list.clear()
print("After clear:", temp_list)

# ------------------ LOOPING LIST ------------------

for fruit in fruits:
    print(fruit)


# ------------------ SEARCHING & COUNTING ------------------

# index() - Find index of an item
print("Index of 'apple':", fruits.index("apple"))

# count() - Count occurrences
fruits.append("apple")
print("Count of 'apple':", fruits.count("apple"))

# ------------------ SORTING & REVERSING ------------------

# sort() - Ascending order
fruits.sort()
print("After sort (ascending):", fruits)

# sort(reverse=True) - Descending order
fruits.sort(reverse=True)
print("After sort (descending):", fruits)

# reverse() - Reverse current order
fruits.reverse()
print("After reverse:", fruits)

# ------------------ COPYING ------------------

# copy() - Make a shallow copy
new_fruits = fruits.copy()
print("Copy of fruits:", new_fruits)

# ------------------ OTHER USEFUL FUNCTIONS ------------------

# len()
print("Length of fruits list:", len(fruits))

# min() and max() (alphabetical order for strings)
print("Minimum (alphabetical):", min(fruits))
print("Maximum (alphabetical):", max(fruits))
