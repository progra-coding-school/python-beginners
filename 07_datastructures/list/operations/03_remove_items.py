# Program Code: 07-operations-03
# Title: Removing Items from a List

# Three ways to remove items: remove, pop, clear

animals = ["cat", "dog", "rabbit", "fish", "bird"]
print("Original list:", animals)

# 1. remove() - Removes by VALUE (removes the first match)
animals.remove("rabbit")
print("After remove('rabbit'):", animals)

# 2. pop() - Removes by INDEX and gives back the removed item
removed = animals.pop(1)
print("After pop(1), removed:", removed)
print("List now:", animals)

# 3. pop() without index - Removes the LAST item
last = animals.pop()
print("After pop(), removed:", last)
print("List now:", animals)

# 4. clear() - Removes ALL items (makes the list empty)
animals.clear()
print("After clear():", animals)
