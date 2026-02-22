# Program Code: CF-LR-03
# Title: Loop Count Detective
# Cognitive Skill: Logical Reasoning (Counting iterations)
# Topic: Control Flow in Python

score = 0

print("Deduce how many times each loop runs, WITHOUT running the code.\n")

# Clue 1
print("--- Clue 1 ---")
print("for i in range(10):")
print("    print(i)")
guess = input("How many times does print run? ")
print("Answer: 10")
if guess.strip() == "10":
    print("Correct! range(10) = 0 to 9 → 10 iterations.")
    score += 1
else:
    print("range(10) produces 0,1,2,...,9 — that's 10 values.")

# Clue 2
print("\n--- Clue 2 ---")
print("for i in range(2, 8):")
print("    print(i)")
guess = input("How many times? ")
print("Answer: 6")
if guess.strip() == "6":
    print("Correct! range(2,8) = 2,3,4,5,6,7 → 6 values.")
    score += 1
else:
    print("range(2,8): starts at 2, stops before 8. Count: 2,3,4,5,6,7 = 6.")

# Clue 3
print("\n--- Clue 3 ---")
print("for i in range(1, 20, 4):")
print("    print(i)")
guess = input("How many times? ")
print("Answer: 5")
if guess.strip() == "5":
    print("Correct! 1, 5, 9, 13, 17 → 5 values.")
    score += 1
else:
    print("range(1,20,4): 1, 5, 9, 13, 17 — next would be 21 which is >= 20. Total: 5.")

# Clue 4 — with break
print("\n--- Clue 4 ---")
print("for i in range(10):")
print("    if i == 4:")
print("        break")
print("    print(i)")
guess = input("How many times does print run? ")
print("Answer: 4")
if guess.strip() == "4":
    print("Correct! Prints 0, 1, 2, 3 then breaks at i=4.")
    score += 1
else:
    print("Loop runs i=0,1,2,3 (print runs 4 times). Breaks before printing 4.")

# Clue 5 — with continue
print("\n--- Clue 5 ---")
print("for i in range(6):")
print("    if i == 3:")
print("        continue")
print("    print(i)")
guess = input("How many times does print run? ")
print("Answer: 5")
if guess.strip() == "5":
    print("Correct! Skips i=3. Prints 0,1,2,4,5 — 5 times.")
    score += 1
else:
    print("range(6)=0-5. continue skips 3. So 0,1,2,4,5 = 5 prints.")

print(f"\nScore: {score} / 5")
