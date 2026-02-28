# Program Code: OUT-KN-04
# Title: print() Options — sep and end
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

# --- Mixing strings and numbers using comma ---
print("Name:", "Aarav", "  Age:", 13, "  Grade:", 7)

print()

# --- Using str() to join numbers in text ---
name  = "Aarav"
age   = 13
grade = 7
print("My name is " + name + " and I am " + str(age) + " years old.")
print("I am in Grade " + str(grade) + " at Progra School.")

print()

# --- str() lets you join numbers with text ---
price    = 120
quantity = 3
print("Total cost: Rs." + str(price * quantity))
print("Pi rounded: " + str(round(3.14159, 2)))

print()

# Think:
# 1. How would you print a date in this format: 22/02/2026 ?
# 2. What does print(5 + 3) display? What about print("5" + "3")?
