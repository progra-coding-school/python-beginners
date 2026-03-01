# Reverse Engineer — Write the print()
# Given the OUTPUT — write the print() statement that produced it.
# Reverse engineering builds deep understanding: you must know WHY, not just HOW.

score = 0

print("Reverse Engineer")
print("Given the output — write the print() statement that produced it.")
print()

# --- Challenge 1 ---
print("Challenge 1 — Output:")
print("  Hello, Aarav!")
answer = input("What print() produced this? ")
print('Answer: print("Hello, Aarav!")')
if "Hello" in answer and "Aarav" in answer:
    score += 1
print()

# --- Challenge 2 ---
# * repeats a string — think about what produces exactly 10 stars
print("Challenge 2 — Output:")
print("  **********")
answer = input("What print() produced this? ")
print('Answer: print("*" * 10)')
if '"*"' in answer and "10" in answer:
    score += 1
print()

# --- Challenge 3 ---
# sep= changes the character that goes BETWEEN items
print("Challenge 3 — Output:")
print("  A-B-C-D")
answer = input("What print() produced this (using sep)? ")
print('Answer: print("A", "B", "C", "D", sep="-")')
if "sep" in answer and '"-"' in answer:
    score += 1
print()

# --- Challenge 4 ---
# Multiple items and numbers in one print() using comma
print("Challenge 4 — Output:")
print("  Name: Diya   Age: 12   Grade: 6")
answer = input("What print() produced this (one line)? ")
print('Answer: print("Name:", "Diya", "  Age:", 12, "  Grade:", 6)')
if "Name" in answer and "Age" in answer:
    score += 1
print()

# --- Challenge 5 ---
# \n inside a string creates a newline — one print() can produce multiple lines
print("Challenge 5 — Output (exactly 3 lines):")
print("  Line 1")
print("  Line 2")
print("  Line 3")
answer = input("Write ONE print() that produces all 3 lines: ")
print('Answer: print("Line 1\\nLine 2\\nLine 3")')
print('  OR:   print("""Line 1')
print('Line 2')
print('Line 3""")')
if "\\n" in answer or '"""' in answer or "'''" in answer:
    score += 1
print()

# --- Challenge 6 ---
# str() converts the arithmetic result so it can be joined with text using +
print("Challenge 6 — Output:")
print("  Total: Rs.450")
answer = input("What print() produced this (use price=150, qty=3)? ")
print('Answer: print("Total: Rs." + str(150 * 3))')
if "str(" in answer and "150" in answer:
    score += 1
print()

print("Score:", score, "/ 6")
