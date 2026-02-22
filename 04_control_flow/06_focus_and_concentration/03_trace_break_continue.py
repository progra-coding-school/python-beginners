# Program Code: CF-FC-03
# Title: Trace Break and Continue
# Cognitive Skill: Focus and Concentration (Precise tracing)
# Topic: Control Flow in Python

# Study these 4 programs carefully, then answer from memory.
print("=== STUDY PHASE ===")
print("Read each program and remember its output!\n")

print("Program 1:")
print("  for i in range(1, 8):")
print("      if i % 3 == 0:")
print("          continue")
print("      print(i)")
print("  Output: 1 2 4 5 7  (skips multiples of 3: 3 and 6)\n")

print("Program 2:")
print("  for i in range(1, 8):")
print("      if i % 3 == 0:")
print("          break")
print("      print(i)")
print("  Output: 1 2  (stops when it hits 3)\n")

print("Program 3:")
print("  i = 0")
print("  while i < 5:")
print("      i += 1")
print("      if i == 3:")
print("          continue")
print("      print(i)")
print("  Output: 1 2 4 5  (skips 3)\n")

print("Program 4:")
print("  found = False")
print("  for i in [4, 7, 2, 9, 1]:")
print("      if i > 8:")
print("          found = True")
print("          break")
print("  print(found)")
print("  Output: True  (9 > 8, so found=True and loop breaks)\n")

input("Cover the above. Press Enter when ready for the test...")

score = 0
print("\n=== TEST PHASE ===\n")

guess = input("Program 1 — What is the last number printed? ")
if guess.strip() == "7":
    print("Correct!")
    score += 1
else:
    print("Answer: 7. (skips 3 and 6, last is 7)")

guess = input("Program 2 — How many numbers are printed? ")
if guess.strip() == "2":
    print("Correct!")
    score += 1
else:
    print("Answer: 2. (1 and 2 before break at i=3)")

guess = input("Program 3 — Which number is NOT printed? ")
if guess.strip() == "3":
    print("Correct!")
    score += 1
else:
    print("Answer: 3. (continue skips it)")

guess = input("Program 4 — What does print(found) output? ")
if guess.strip().lower() == "true":
    print("Correct!")
    score += 1
else:
    print("Answer: True. (9 > 8 sets found=True before break)")

print(f"\nScore: {score} / 4")
