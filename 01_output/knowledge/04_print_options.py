# Program Code: OUT-KN-04
# Title: print() Options — sep, end, and f-strings
# Cognitive Skill: Knowledge
# Topic: Output in Python

# print() has powerful options to control HOW things are displayed.

# --- Multiple arguments with comma ---
print("Aarav", "Diya", "Karthik")    # Aarav Diya Karthik (space by default)

# --- sep: change the separator between items ---
print("Aarav", "Diya", "Karthik", sep=", ")     # Aarav, Diya, Karthik
print("2024", "01", "15", sep="-")               # 2024-01-15 (like a date!)
print("www", "progra", "com", sep=".")           # www.progra.com
print(10, 20, 30, sep=" | ")                     # 10 | 20 | 30

print()

# --- end: change what comes AFTER the print (default is a new line) ---
print("Hello", end=" ")
print("World!")                    # Both on same line: Hello World!

print("A", end=" → ")
print("B", end=" → ")
print("C")                         # A → B → C

print(1, end=", ")
print(2, end=", ")
print(3)                           # 1, 2, 3

print()

# --- f-strings: embed variables directly in output ---
name  = "Aarav"
age   = 13
grade = 7

# Without f-string (harder to read)
print("My name is", name, "and I am", age, "years old.")

# With f-string (clean and readable)
print(f"My name is {name} and I am {age} years old.")
print(f"I am in Grade {grade} at Progra School.")

print()

# --- f-strings can include calculations ---
price = 120
quantity = 3
print(f"Total cost: Rs.{price * quantity}")
print(f"Pi rounded: {3.14159:.2f}")      # .2f → 2 decimal places

print()

# --- Combining sep, end, and f-strings ---
students = ["Aarav", "Diya", "Karthik"]
for i, student in enumerate(students, 1):
    print(f"{i}. {student}", end="   ")
print()

# Think:
# 1. How would you print a date in this format: 22/02/2026 ?
# 2. What does print(f"5 + 3 = {5 + 3}") display?
