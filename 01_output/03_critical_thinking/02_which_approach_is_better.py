# Which Approach Is Better?
# Same output — different ways to write it. Analyse which is clearest and why.
# Understanding trade-offs helps you choose the right tool for each situation.

name  = "Aarav"
age   = 13
score = 87.5

# =========================================================
# Scenario 1: Displaying student info
# =========================================================
print("Scenario 1: Displaying student info:")

# Approach A: Concatenation with + — full control over every character and space
print("Approach A: " + "Name: " + name + ", Age: " + str(age) + ", Score: " + str(score))

# Approach B: Comma-separated — quicker to write, auto-adds a space after each item
print("Approach B:", "Name:", name, "| Age:", age, "| Score:", score)

print("Both work! A gives you full control over spacing.")
print("Comma (,) is quicker but always adds a space after each item.")
print()

# =========================================================
# Scenario 2: Displaying a table row
# =========================================================
print("Scenario 2: Displaying a table row:")

subject = "Maths"
marks   = 85

# Approach A: Manual spaces — fragile; breaks when content length varies
print("  Maths                  85     A")

# Approach B: String methods — adapts to any length of content automatically
grade = "A" if marks >= 80 else "B"
print("  " + subject.ljust(15) + str(marks).rjust(5) + "     " + grade.rjust(5))

print("Best: B — .ljust() and .rjust() align columns neatly for any content length.")
print()

# =========================================================
# Scenario 3: Multiline output
# =========================================================
print("Scenario 3: Printing a poem:")

# Approach A: Multiple print() — clearest for beginners; easy to read and edit
print("Approach A:")
print("Roses are red,")
print("Violets are blue,")
print("Python is awesome,")
print("And so are you!")

# Approach B: Single print with \n — compact but harder to edit individual lines
print("Approach B:")
print("Roses are red,\nViolets are blue,\nPython is awesome,\nAnd so are you!")

# Approach C: Triple quotes — cleanest for long text blocks
print("Approach C:")
print("""Roses are red,
Violets are blue,
Python is awesome,
And so are you!""")

print("All 3 produce the same output.")
print("A is clearest for beginners.")
print("C is cleanest for long text.")
print()

# =========================================================
# Decision Guide
# =========================================================
print("When to use which?")
print("Comma (,)    → quick mixing of values, adds space automatically")
print("Plus (+)     → joining strings, needs str() for numbers")
print('Triple """   → multiline text blocks')
print(".ljust(n)    → left-align text in a column of n characters")
print(".rjust(n)    → right-align text in a column of n characters")
