# print() Options — sep and end
# print() has two powerful keyword arguments: sep (separator) and end (line ending).
# Mastering these lets you format output precisely on one line or across lines.

# --- Multiple arguments with comma ---
# By default, comma-separated arguments are printed with a space between them
print("Aarav", "Diya", "Karthik")    # Aarav Diya Karthik (space by default)

# --- sep: change the separator between items ---
# sep replaces the default space between each printed item
print("Aarav", "Diya", "Karthik", sep=", ")     # Aarav, Diya, Karthik
print("2024", "01", "15", sep="-")               # 2024-01-15 (date format!)
print("www", "progra", "com", sep=".")           # www.progra.com
print(10, 20, 30, sep=" | ")                     # 10 | 20 | 30

print()

# --- end: change what comes AFTER the print (default is \n — a new line) ---
# end="" removes the newline so the NEXT print() continues on the SAME line
print("Hello", end=" ")
print("World!")                    # Both on same line: Hello World!

print("A", end=" → ")
print("B", end=" → ")
print("C")                         # A → B → C — chained on one line

print(1, end=", ")
print(2, end=", ")
print(3)                           # 1, 2, 3

print()

# --- Mixing strings and numbers using comma ---
# Comma automatically handles the space — no str() conversion needed
print("Name:", "Aarav", "  Age:", 13, "  Grade:", 7)

print()

# --- Using str() to join numbers into text strings ---
# + only works with strings; str() converts any value to a string first
name  = "Aarav"
age   = 13
grade = 7
print("My name is " + name + " and I am " + str(age) + " years old.")
print("I am in Grade " + str(grade) + " at Progra School.")

print()

# --- str() lets you join numbers with text using + ---
# Useful when you need exact spacing without the automatic space from comma
price    = 120
quantity = 3
print("Total cost: Rs." + str(price * quantity))
print("Pi rounded: " + str(round(3.14159, 2)))

print()

# Think:
# 1. How would you print a date in this format: 22/02/2026 ?
# 2. What does print(5 + 3) display? What about print("5" + "3")?
