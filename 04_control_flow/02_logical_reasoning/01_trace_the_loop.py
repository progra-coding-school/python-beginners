# Program Code: CF-LR-01
# Title: Trace the Loop
# Cognitive Skill: Logical Reasoning (Tracing loop execution)
# Topic: Control Flow in Python

score = 0

# Round 1
print("--- Round 1 ---")
print("for i in range(3):")
print("    print(i * 2)")
guess = input("What are the 3 outputs? (e.g. 0 2 4) ")
print("Answer: 0 2 4")
if "0" in guess and "2" in guess and "4" in guess:
    print("Correct!")
    score += 1
else:
    print("range(3) = 0,1,2. i*2 gives 0, 2, 4.")

# Round 2
print("\n--- Round 2 ---")
print("total = 0")
print("for n in [5, 10, 15]:")
print("    total = total + n")
print("print(total)")
guess = input("What does print(total) output? ")
print("Answer: 30")
if guess.strip() == "30":
    print("Correct!")
    score += 1
else:
    print("5 + 10 + 15 = 30. The loop accumulates the sum.")

# Round 3
print("\n--- Round 3 ---")
print("count = 10")
print("while count > 7:")
print("    print(count)")
print("    count -= 1")
guess = input("What 3 values are printed? (e.g. 10 9 8) ")
print("Answer: 10 9 8")
if "10" in guess and "9" in guess and "8" in guess:
    print("Correct!")
    score += 1
else:
    print("Starts at 10. Stops when count <= 7. Prints 10, 9, 8.")

# Round 4
print("\n--- Round 4 ---")
print("for i in range(1, 6):")
print("    if i == 3:")
print("        break")
print("    print(i)")
guess = input("What values are printed? ")
print("Answer: 1 2")
if "1" in guess and "2" in guess and "3" not in guess:
    print("Correct! Break stops the loop when i == 3.")
    score += 1
else:
    print("break exits when i=3. Only 1 and 2 are printed.")

# Round 5 — tricky!
print("\n--- Round 5 (Tricky!) ---")
print("for i in range(5):")
print("    if i % 2 == 0:")
print("        continue")
print("    print(i)")
guess = input("What values are printed? ")
print("Answer: 1 3")
if "1" in guess and "3" in guess and "0" not in guess and "2" not in guess:
    print("Correct! continue skips even numbers (0, 2, 4).")
    score += 1
else:
    print("Even numbers (0,2,4) are skipped. Only odd: 1 and 3.")

print(f"\nScore: {score} / 5")
