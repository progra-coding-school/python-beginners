# Quotes and Strings
# Text must be wrapped in quotes to be a string. You can use single, double, or triple quotes.
# Each style has a purpose — choosing the right one avoids SyntaxErrors.

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
print("It's a beautiful day!")      # works — apostrophe inside double quotes
# print('It's a beautiful day!')    # SyntaxError — apostrophe ends the single-quote string

# Use single quotes when your text contains double quotes
print('She said "Hello!"')          # works — double quotes inside single quotes
# print("She said "Hello!"")        # SyntaxError — inner " ends the string early

print()

# --- Triple quotes: for multiline text ---
# Triple quotes let a string span multiple lines without \n
print('''My name is Aarav.
I am 13 years old.
I love coding!''')

print()

print("""Progra Kids Coding School
Teaching kids to think,
solve problems and code!""")

print()

# --- String repetition ---
# * on a string repeats it that many times (same as numbers!)
print("-" * 25)
print("Progra" * 3)
print("-" * 25)

print()

# --- Escape characters (special characters inside strings) ---
# Backslash \ gives the next character a special meaning
print("First line\nSecond line")   # \n → new line character
print("Name:\tAarav")              # \t → tab space
print("He said \"Namaste!\"")      # \" → literal double quote inside double-quoted string

# Think:
# 1. How would you print: She said "It's great!"  (has both ' and ")
# 2. What does \n do inside a print() statement?
