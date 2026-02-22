# Program Code: CF-HOT-01
# Title: Reverse Engineer — Decode the Control Flow
# Cognitive Skill: Higher Order Thinking (Working backwards)
# Topic: Control Flow in Python

score = 0

# Round 1
print("--- Round 1 ---")
print("Output:")
print("  1")
print("  2")
print("  4")
print("  5")
print("(3 is missing)")
guess = input("What control flow statement caused 3 to be skipped? ")
print("Answer: continue  (when i == 3: continue)")
if "continue" in guess.lower():
    print("Correct!")
    score += 1
else:
    print("'continue' skips the rest of the loop body for that iteration.")
input("Press Enter...")

# Round 2
print("\n--- Round 2 ---")
print("Output:")
print("  Hello")
print("  Hello")
print("  Hello")
guess = input("Write ONE possible for loop that produces this output: ")
print("Possible: for i in range(3): print('Hello')")
print("Also valid: for i in ['a','b','c']: print('Hello')")
score += 1
input("Press Enter...")

# Round 3
print("\n--- Round 3 ---")
print("Output: 15")
print("Code hint: uses a for loop over a list and an accumulator variable.")
guess = input("Reconstruct the code that produces 15 from a list: ")
print("Possible: total = 0")
print("          for n in [1, 2, 3, 4, 5]: total += n")
print("          print(total)     →  1+2+3+4+5 = 15")
score += 1
input("Press Enter...")

# Round 4 — challenge
print("\n--- Round 4 (Challenge) ---")
print("Output:")
print("  0")
print("  2")
print("  4")
print("  6")
print("  8")
guess = input("Write a loop (for or while) that produces this: ")
print("Possible A: for i in range(0, 10, 2): print(i)")
print("Possible B: for i in range(10):")
print("                if i % 2 == 0: print(i)")
score += 1

print(f"\nScore: {score} / 4")
