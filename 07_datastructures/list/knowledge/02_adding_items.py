# Adding Items to a List
# Three ways to grow a list:
#   append(item)       → adds ONE item to the END
#   insert(i, item)    → adds ONE item at a specific position
#   extend(other_list) → adds ALL items from another list at once

# Start with a small team — we will grow it using all three methods
cricket_team = ["Aarav", "Kabir", "Rohan"]
print("Team:", cricket_team)

# append() — adds ONE item to the END of the list
# Most common way to grow a list one item at a time
cricket_team.append("Meera")
print("After append('Meera'):", cricket_team)

# insert() — adds ONE item at a specific index position
# Everything from that index onwards shifts one place to the right
cricket_team.insert(1, "Diya")     # insert "Diya" at index 1
print("After insert(1, 'Diya'):", cricket_team)

# extend() — adds ALL items from another list
# Much faster than appending one by one when you have multiple items
new_players = ["Riya", "Dev"]
cricket_team.extend(new_players)
print("After extend(['Riya', 'Dev']):", cricket_team)

print()

# Quick reminder — which method to use when?
print("append()  — adds ONE item to the end")
print("insert()  — adds ONE item at a specific position")
print("extend()  — adds MULTIPLE items to the end")
print()

# KEY CONFUSION: append vs extend when passing a list
# append([list]) treats the whole list as ONE item → creates a nested list
# extend([list]) unpacks the list and adds items one by one → flat list
fruits = ["apple", "banana"]
fruits.append(["mango", "orange"])   # adds ["mango", "orange"] as ONE item
print("append with a list:", fruits)  # ['apple', 'banana', ['mango', 'orange']]

fruits2 = ["apple", "banana"]
fruits2.extend(["mango", "orange"])  # adds mango and orange as separate items
print("extend with a list:", fruits2) # ['apple', 'banana', 'mango', 'orange']
