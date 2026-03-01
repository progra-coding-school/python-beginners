# Program Code: LIST-KN-02
# Title: Adding Items to a List
# Cognitive Skill: Knowledge (Syntax and usage)
# Topic: Lists in Python

# Start with a team list
cricket_team = ["Aarav", "Kabir", "Rohan"]
print("Team:", cricket_team)

# append() — adds to the END
cricket_team.append("Meera")
print("After append('Meera'):", cricket_team)

# insert() — adds at a specific position
cricket_team.insert(1, "Diya")     # insert at index 1
print("After insert(1, 'Diya'):", cricket_team)

# extend() — adds multiple items at once
new_players = ["Riya", "Dev"]
cricket_team.extend(new_players)
print("After extend(['Riya', 'Dev']):", cricket_team)

print()

# The difference
print("append()  — adds ONE item to the end")
print("insert()  — adds ONE item at a specific position")
print("extend()  — adds MULTIPLE items to the end")
print()

# append vs extend — a common confusion
fruits = ["apple", "banana"]
fruits.append(["mango", "orange"])   # adds the list AS ONE item
print("append with a list:", fruits)  # ['apple', 'banana', ['mango', 'orange']]

fruits2 = ["apple", "banana"]
fruits2.extend(["mango", "orange"])  # adds items one by one
print("extend with a list:", fruits2) # ['apple', 'banana', 'mango', 'orange']
