# Program Code: OUT-LR-03
# Title: Order Matters
# Cognitive Skill: Logical Reasoning (Sequential Reasoning)
# Topic: Output in Python

# Python runs print() statements TOP to BOTTOM, in order.
# The sequence of your prints is the sequence of your output.

score = 0

print("=== Order Matters ===")
print("Predict the EXACT output, in order.")
print()

# --- Q1: Simple order ---
print("Q1: What is the output of these 3 lines in order?")
print("""
  print("Maths")
  print("Science")
  print("English")
""")
answer = input("Write the 3 lines of output (comma separated): ")
print("Answer: Maths, Science, English")
if all(s in answer for s in ["Maths", "Science", "English"]):
    score += 1
    print("Correct!")
print()

# --- Q2: end="" changes order on screen ---
print("Q2: What is the full output?")
print("""
  print("A", end="")
  print("B", end="")
  print("C")
""")
answer = input("Output: ")
print("Answer: ABC  (all on one line — end='' removes the newline)")
if answer.strip() == "ABC":
    score += 1
    print("Correct!")
print()

# --- Q3: Blank lines affect spacing ---
print("Q3: How many lines does this produce (including blank lines)?")
print("""
  print("Start")
  print()
  print("Middle")
  print()
  print("End")
""")
answer = input("Number of lines: ")
print("Answer: 5  (Start, blank, Middle, blank, End)")
if answer.strip() == "5":
    score += 1
    print("Correct!")
print()

# --- Q4: Multiple end="" in sequence ---
print("Q4: What is the FULL output (one line or many)?")
print("""
  print("Morning", end=" | ")
  print("Afternoon", end=" | ")
  print("Evening")
""")
answer = input("Output: ")
print("Answer: Morning | Afternoon | Evening  (all on one line — end= changes the newline)")
if "Morning" in answer and "Evening" in answer:
    score += 1
    print("Correct!")
print()

# --- Q5: sep changes the separator ---
print("Q5: What are the 2 lines of output?")
print("""
  print("10", "20", "30", sep=" + ")
  print("10", "20", "30", sep=" → ")
""")
answer = input("Output (2 lines): ")
print("Answer: Line 1: 10 + 20 + 30   Line 2: 10 → 20 → 30")
if "+" in answer and "→" in answer:
    score += 1
    print("Correct!")
print()

print("Score:", score, "/ 5")
print("Key insight: Python reads TOP to BOTTOM. Order of print() = order of output.")
