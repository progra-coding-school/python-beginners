# Program Code: CF-FC-02
# Title: Count the Iterations
# Cognitive Skill: Focus and Concentration (Mental loop tracing)
# Topic: Control Flow in Python

score = 0

print("=== Count the Iterations ===")
print("How many times does the print statement run? Think carefully!\n")

# Challenge 1
print("--- Challenge 1 ---")
print("for i in range(1, 11, 2):")
print("    print(i)")
guess = input("How many times? ")
print("Answer: 5  (values: 1, 3, 5, 7, 9)")
if guess.strip() == "5":
    print("Correct!")
    score += 1
else:
    print("range(1,11,2): 1,3,5,7,9 → 5 values.")

# Challenge 2
print("\n--- Challenge 2 ---")
print("count = 20")
print("while count > 10:")
print("    print(count)")
print("    count -= 3")
guess = input("How many times? ")
print("Answer: 4  (20, 17, 14, 11 — next is 8 which fails count > 10)")
if guess.strip() == "4":
    print("Correct!")
    score += 1
else:
    print("20→17→14→11→8(stop). So 20,17,14,11 print = 4 times.")

# Challenge 3 — nested loops
print("\n--- Challenge 3 ---")
print("for i in range(5):")
print("    for j in range(3):")
print("        print(i, j)")
guess = input("How many total prints? ")
print("Answer: 15  (5 outer × 3 inner = 15)")
if guess.strip() == "15":
    print("Correct! Nested loops multiply.")
    score += 1
else:
    print("Outer runs 5 times. For each outer, inner runs 3 times. 5 × 3 = 15.")

# Challenge 4 — with break inside nested loops
print("\n--- Challenge 4 (Tricky!) ---")
print("for i in range(5):")
print("    for j in range(5):")
print("        if j == 2:")
print("            break")
print("        print(i, j)")
guess = input("How many total prints? ")
print("Answer: 10  (for each i, j runs 0 and 1 then breaks → 2 prints × 5 = 10)")
if guess.strip() == "10":
    print("Correct!")
    score += 1
else:
    print("Inner loop breaks at j=2, so only j=0 and j=1 print each time. 2 × 5 = 10.")

print(f"\nScore: {score} / 4")
