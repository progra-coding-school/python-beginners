# Program Code: OUT-KN-03
# Title: Quotes and Strings
# Cognitive Skill: Knowledge
# Topic: Output in Python

# In Python, text must be wrapped in quotes to be a string.
# You can use single quotes, double quotes, or triple quotes.

# --- Single quotes ---
print('Hello from single quotes!')
print('My name is Karthik')

# --- Double quotes ---
print("Hello from double quotes!")
print("My name is Karthik")

# Both work the same — choose one and be consistent!

print()

# --- When to use which ---
# Use double quotes when your text contains an apostrophe (')
print("It's a beautiful day!")      # ✓ works
# print('It's a beautiful day!')    # ✗ SyntaxError — apostrophe breaks it

# Use single quotes when your text contains double quotes
print('She said "Hello!"')          # ✓ works
# print("She said "Hello!"")        # ✗ SyntaxError

print()

# --- Triple quotes: for multiline text ---
# Triple single quotes
print('''My name is Aarav.
I am 13 years old.
I love coding!''')

print()

# Triple double quotes
print("""Progra Kids Coding School
Teaching kids to think,
solve problems and code!""")

print()

# --- String repetition ---
print("-" * 25)
print("Progra" * 3)
print("-" * 25)

print()

# --- Escape characters (special characters inside strings) ---
print("First line\nSecond line")   # \n → new line
print("Name:\tAarav")              # \t → tab space
print("He said \"Namaste!\"")      # \" → quote inside double quotes

# Think:
# 1. How would you print: She said "It's great!"  (has both ' and ")
# 2. What does \n do inside a print() statement?
