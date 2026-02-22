# Program Code: CF-LR-02
# Title: Predict the Condition
# Cognitive Skill: Logical Reasoning (Predicting branch execution)
# Topic: Control Flow in Python

score = 0

# Round 1
print("--- Round 1 ---")
print("marks = 72")
print("if marks >= 75:")
print("    print('Merit')")
print("elif marks >= 35:")
print("    print('Pass')")
print("else:")
print("    print('Fail')")
guess = input("What prints? ")
print("Answer: Pass")
if guess.strip().lower() == "pass":
    print("Correct! 72 < 75, so first branch skipped. 72 >= 35, so 'Pass'.")
    score += 1
else:
    print("72 fails the first condition (>=75). It passes the second (>=35).")

# Round 2
print("\n--- Round 2 ---")
print("x = 5")
print("y = 10")
print("if x > 3 and y < 8:")
print("    print('A')")
print("elif x > 3 or y < 8:")
print("    print('B')")
print("else:")
print("    print('C')")
guess = input("What prints? ")
print("Answer: B")
if guess.strip().upper() == "B":
    print("Correct! x>3 is True BUT y<8 is False. AND fails. OR: x>3 is True → B.")
    score += 1
else:
    print("x>3 (True) AND y<8 (False) = False. x>3 (True) OR y<8 (False) = True → B.")

# Round 3
print("\n--- Round 3 ---")
print("for i in range(4):")
print("    if i == 2:")
print("        print('Found!')")
guess = input("How many times does 'Found!' print? ")
print("Answer: 1")
if guess.strip() == "1":
    print("Correct! range(4) = 0,1,2,3. Only i==2 triggers the print.")
    score += 1
else:
    print("Loop runs 4 times (0-3). Only when i=2 does the condition match.")

# Round 4
print("\n--- Round 4 ---")
print("is_raining = False")
print("has_umbrella = True")
print("if not is_raining or has_umbrella:")
print("    print('Go out!')")
print("else:")
print("    print('Stay home!')")
guess = input("What prints? ")
print("Answer: Go out!")
if "go out" in guess.lower():
    print("Correct! not False = True. True or anything = True.")
    score += 1
else:
    print("not is_raining = not False = True. True or True = True → 'Go out!'")

print(f"\nScore: {score} / 4")
