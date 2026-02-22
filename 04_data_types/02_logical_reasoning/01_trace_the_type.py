# Program Code: DT-LR-01
# Title: Trace the Type
# Cognitive Skill: Logical Reasoning (Tracing type changes)
# Topic: Data Types in Python

score = 0

# Round 1
print("--- Round 1 ---")
print("x = 10")
print("x = float(x)")
print("x = str(x)")
guess = input("What type is x now? (int / float / str / bool) ")
print("Answer: str")
if guess.lower() == "str":
    print("Correct!")
    score += 1
else:
    print("Trace: int → float → str. Final type is str.")

# Round 2
print("\n--- Round 2 ---")
print("a = '99'")
print("b = int(a)")
print("c = b + 1")
guess = input("What type is c? (int / float / str / bool) ")
print("Answer: int")
if guess.lower() == "int":
    print("Correct!")
    score += 1
else:
    print("str → int → int+1 = int")

# Round 3
print("\n--- Round 3 ---")
print("p = 10")
print("q = 4")
print("r = p / q")
guess = input("What type is r? (int / float / str / bool) ")
print("Answer: float")
if guess.lower() == "float":
    print("Correct! Division always gives float.")
    score += 1
else:
    print("10 / 4 = 2.5. Division always produces a float in Python.")

# Round 4
print("\n--- Round 4 ---")
print("marks = 80")
print("result = marks >= 35")
guess = input("What type is result? (int / float / str / bool) ")
print("Answer: bool")
if guess.lower() == "bool":
    print("Correct! Comparisons always return True or False (bool).")
    score += 1
else:
    print("80 >= 35 is True. Any comparison gives a bool.")

# Round 5 — tricky!
print("\n--- Round 5 (Tricky!) ---")
print("val = int(9.9)")
guess = input("What is val? ")
print("Answer: 9")
if guess == "9":
    print("Correct! int() drops the decimal — it does NOT round.")
    score += 1
else:
    print("int(9.9) = 9, NOT 10. int() truncates (chops off) the decimal.")

print(f"\nScore: {score} / 5")
