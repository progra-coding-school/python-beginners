# Program Code: OP-FC-03
# Title: Operator Memory Recall
# Cognitive Skill: Focus and Concentration (Memory Recall)
# Topic: Operators in Python

# How well do you remember what each operator does?
# No looking back — recall from memory!

score = 0

print("=== Operator Memory Recall ===")
print("Answer from memory — no peeking at notes!")
print()

# --- Round 1: Symbol → Meaning ---
print("--- Part 1: What does this operator do? ---")
print()

print("Q1: What does ** do?")
ans = input("> ").lower()
if any(word in ans for word in ["power", "exponent", "raised"]):
    print("Correct! ** is the exponentiation (power) operator.")
    score += 1
else:
    print("Answer: ** raises a number to a power. e.g., 2**3 = 8")
print()

print("Q2: What does // do?")
ans = input("> ").lower()
if any(word in ans for word in ["floor", "whole", "integer", "int", "decimal"]):
    print("Correct! // is floor division — gives only the whole number part.")
    score += 1
else:
    print("Answer: // divides and removes the decimal. e.g., 7//2 = 3")
print()

print("Q3: What does % do?")
ans = input("> ").lower()
if any(word in ans for word in ["remainder", "modulo", "left", "rest"]):
    print("Correct! % gives the remainder after division.")
    score += 1
else:
    print("Answer: % gives remainder. e.g., 10%3 = 1")
print()

# --- Round 2: Meaning → Symbol ---
print("--- Part 2: Which symbol matches the meaning? ---")
print()

print("Q4: Which operator checks if two values are EQUAL?")
ans = input("> ").strip()
if ans == "==":
    print("Correct! == is the equality comparison operator.")
    score += 1
else:
    print("Answer: == (two equals signs)")
print()

print("Q5: Which operator means NOT EQUAL?")
ans = input("> ").strip()
if ans == "!=":
    print("Correct! != means 'not equal to'.")
    score += 1
else:
    print("Answer: !=")
print()

# --- Round 3: Logic recall ---
print("--- Part 3: Logic Rules ---")
print()

print("Q6: True AND False = ?")
ans = input("> ").strip()
if ans.lower() == "false":
    print("Correct! AND requires BOTH to be True.")
    score += 1
else:
    print("Answer: False (both must be True for AND to give True)")
print()

print("Q7: False OR True = ?")
ans = input("> ").strip()
if ans.lower() == "true":
    print("Correct! OR only needs ONE to be True.")
    score += 1
else:
    print("Answer: True (just one True is enough for OR)")
print()

print("Q8: not False = ?")
ans = input("> ").strip()
if ans.lower() == "true":
    print("Correct! not flips the boolean.")
    score += 1
else:
    print("Answer: True (not flips False to True)")
print()

# Final summary
print("═" * 40)
print(f"Memory Recall Score: {score} / 8")
print()
print("Quick Reference:")
print("  ** → power      // → floor div   % → remainder")
print("  == → equal      != → not equal")
print("  and → both True  or → one True   not → flip it")
print("═" * 40)
