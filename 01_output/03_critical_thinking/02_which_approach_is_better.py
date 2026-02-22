# Program Code: OUT-CT-02
# Title: Which Approach Is Better?
# Cognitive Skill: Critical Thinking (Approach Evaluation)
# Topic: Output in Python

# Same output — three different ways. Analyze which is clearest.

name  = "Aarav"
age   = 13
score = 87.5

print("=== Scenario 1: Displaying student info ===")

# Approach A: Concatenation with +
print("Approach A: " + "Name: " + name + ", Age: " + str(age) + ", Score: " + str(score))

# Approach B: Comma-separated
print("Approach B:", "Name:", name, "| Age:", age, "| Score:", score)

# Approach C: f-string
print(f"Approach C: Name: {name}, Age: {age}, Score: {score}")

print("Best: C — f-string is readable, no type conversion needed, cleanest.")
print()

# === Scenario 2: Formatted table ===
print("=== Scenario 2: Displaying a table row ===")

subject = "Maths"
marks   = 85

# Approach A: Manual spaces
print("  Maths                  85     A")    # messy, hard to maintain

# Approach B: f-string with alignment
print(f"  {subject:<15} {marks:>5}     {('A' if marks >= 80 else 'B'):>5}")

print("Best: B — columns align automatically regardless of content length.")
print()

# === Scenario 3: Multiline output ===
print("=== Scenario 3: Printing a poem ===")

poem = "Roses are red,\nViolets are blue,\nPython is awesome,\nAnd so are you!"

# Approach A: Multiple print()
print("Approach A:")
print("Roses are red,")
print("Violets are blue,")
print("Python is awesome,")
print("And so are you!")

# Approach B: Single print with \n
print("Approach B:")
print("Roses are red,\nViolets are blue,\nPython is awesome,\nAnd so are you!")

# Approach C: Triple quotes
print("Approach C:")
print("""Roses are red,
Violets are blue,
Python is awesome,
And so are you!""")

print("All 3 produce the same output.")
print("A is clearest for beginners.")
print("C is cleanest for long text.")
print()

# === Decision Guide ===
print("=== When to use which? ===")
print("Comma (,)  → quick mixing of values, adds space automatically")
print("Plus (+)   → joining strings, needs str() for numbers")
print("f-string   → BEST for combining variables with text")
print("Triple \"\"\" → multiline text blocks")
