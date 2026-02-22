# Program Code: DT-FC-02
# Title: Type Math Challenge
# Cognitive Skill: Focus and Concentration (Mental precision)
# Topic: Data Types in Python

score = 0

print("=== Type Math Challenge ===")
print("Calculate the result AND the type without running code!\n")

# Challenge 1
print("--- Challenge 1 ---")
print("x = 5")
print("y = 2")
print("z = x / y")
val_guess = input("Value of z: ")
type_guess = input("Type of z (int/float): ")
print("Answer: 2.5, float")
if val_guess == "2.5" and type_guess.lower() == "float":
    print("Correct!")
    score += 2
elif val_guess == "2.5" or type_guess.lower() == "float":
    print("Half right.")
    score += 1

# Challenge 2
print("\n--- Challenge 2 ---")
print("a = '3'")
print("b = '7'")
print("c = a + b")
val_guess = input("Value of c: ")
type_guess = input("Type of c (int/float/str): ")
print("Answer: 37, str")
if val_guess == "37" and type_guess.lower() == "str":
    print("Correct!")
    score += 2
elif val_guess == "37" or type_guess.lower() == "str":
    print("Half right.")
    score += 1

# Challenge 3
print("\n--- Challenge 3 ---")
print("p = 10")
print("q = 3")
print("r = p % q")
val_guess = input("Value of r: ")
type_guess = input("Type of r (int/float): ")
print("Answer: 1, int")
if val_guess == "1" and type_guess.lower() == "int":
    print("Correct!")
    score += 2
elif val_guess == "1" or type_guess.lower() == "int":
    print("Half right.")
    score += 1

# Challenge 4 — tricky
print("\n--- Challenge 4 (Tricky!) ---")
print("x = int(float('9.9'))")
val_guess = input("Value of x: ")
type_guess = input("Type of x (int/float/str): ")
print("Answer: 9, int")
if val_guess == "9" and type_guess.lower() == "int":
    print("Correct! float('9.9')=9.9, then int(9.9)=9")
    score += 2
elif val_guess == "9" or type_guess.lower() == "int":
    print("Half right.")
    score += 1

print(f"\nScore: {score} / 8")
