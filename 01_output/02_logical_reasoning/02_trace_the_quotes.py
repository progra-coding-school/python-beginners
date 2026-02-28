# Program Code: OUT-LR-02
# Title: Trace the Quotes
# Cognitive Skill: Logical Reasoning (Pattern Finding)
# Topic: Output in Python

# Look at each print() carefully.
# Identify which quote style is used and what the output will be.

score = 0

print("=== Trace the Quotes ===")
print("Identify: single / double / triple  AND  predict output.")
print()

# --- Q1 ---
print("Q1: print('Namaste, World!')")
q = input("Quote style (single/double/triple): ").strip().lower()
a = input("Output: ").strip()
print("Answer: single quotes.  Output: Namaste, World!")
if "single" in q and a == "Namaste, World!": score += 1
print()

# --- Q2 ---
print('Q2: print("It\'s a great day!")')
q = input("Quote style (single/double/triple): ").strip().lower()
a = input("Output: ").strip()
print("Answer: double quotes.  Output: It's a great day!")
if "double" in q and "It's" in a: score += 1
print()

# --- Q3 ---
print("Q3: print('''Hello\\nWorld''')")
q = input("Quote style: ").strip().lower()
a = input("How many lines in output (1 or 2)? ").strip()
print("Answer: triple single quotes.  Output is on 2 lines: Hello / World")
if "triple" in q and "2" in a: score += 1
print()

# --- Q4 ---
print("Q4: print('She said', '\"Hello!\"')")
a = input("Output: ").strip()
print('Answer: She said "Hello!"')
if '"Hello!"' in a or '"Hello!"' in a: score += 1
print()

# --- Q5 ---
print("Q5: Which is the correct way to print: I can't stop!")
print("  A: print('I can't stop!')")
print("  B: print(\"I can't stop!\")")
print("  C: print('''I can't stop!''')")
a = input("Correct options (A/B/C — can be multiple): ").strip().upper()
print("Answer: B and C.  A causes SyntaxError — apostrophe breaks single quotes.")
if "B" in a and "C" in a: score += 1
print()

print("Score:", score, "/ 5")
print()
print("Quick guide:")
print("  Single '  → use when text has double quotes inside")
print("  Double \"  → use when text has apostrophes inside")
print("  Triple ''' or \"\"\" → multiline OR when you need both ' and \"")
