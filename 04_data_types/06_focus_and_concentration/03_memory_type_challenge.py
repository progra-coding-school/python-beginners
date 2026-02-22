# Program Code: DT-FC-03
# Title: Memory Type Challenge
# Cognitive Skill: Focus and Concentration (Memory and recall)
# Topic: Data Types in Python

# Study these values, then answer from memory.
print("=== STUDY PHASE ===")
print("Remember these variables — you'll be tested!\n")

print("student = 'Meera'         (str)")
print("age     = 14              (int)")
print("gpa     = 9.3             (float)")
print("passed  = True            (bool)")
print("school  = 'RKV Chennai'   (str)")
print("rank    = 3               (int)")
print("weight  = 48.5            (float)")
print("active  = False           (bool)")

input("\nCover the above and press Enter when ready...")

score = 0

print("\n=== TEST PHASE ===\n")

guess = input("What was 'gpa'? ")
if guess == "9.3":
    print("Correct!")
    score += 1
else:
    print("Answer: 9.3")

guess = input("What type was 'passed'? ")
if guess.lower() == "bool":
    print("Correct!")
    score += 1
else:
    print("Answer: bool")

guess = input("What was 'rank'? ")
if guess == "3":
    print("Correct!")
    score += 1
else:
    print("Answer: 3")

guess = input("What was 'school'? ")
if "RKV" in guess or "Chennai" in guess:
    print("Correct!")
    score += 1
else:
    print("Answer: RKV Chennai")

guess = input("What type was 'weight'? ")
if guess.lower() == "float":
    print("Correct!")
    score += 1
else:
    print("Answer: float")

guess = input("What was 'active'? ")
if guess.lower() == "false":
    print("Correct!")
    score += 1
else:
    print("Answer: False")

print(f"\nScore: {score} / 6")
