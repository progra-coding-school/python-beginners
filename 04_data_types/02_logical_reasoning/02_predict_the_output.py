# Program Code: DT-LR-02
# Title: Predict the Output
# Cognitive Skill: Logical Reasoning (Predicting behaviour)
# Topic: Data Types in Python

score = 0

# Round 1
print("--- Round 1 ---")
print("print(type(3.0))")
guess = input("What will print? ")
answer = "<class 'float'>"
print("Answer:", answer)
if "float" in guess.lower():
    print("Correct!")
    score += 1
else:
    print("3.0 has a decimal point, so Python treats it as float.")

# Round 2
print("\n--- Round 2 ---")
print("a = '5'")
print("b = '3'")
print("print(a + b)")
guess = input("What will print? ")
print("Answer: 53")
if guess == "53":
    print("Correct! Strings join, they don't add.")
    score += 1
else:
    print("'5' + '3' = '53' (joining strings). It is NOT 8!")

# Round 3
print("\n--- Round 3 ---")
print("print(bool(0), bool(1), bool(-5))")
guess = input("What will print? ")
print("Answer: False True True")
if "false" in guess.lower() and "true" in guess.lower():
    print("Correct! 0 is False; any non-zero number is True.")
    score += 1
else:
    print("bool(0)=False, bool(1)=True, bool(-5)=True (non-zero = True)")

# Round 4
print("\n--- Round 4 ---")
print("x = 7 // 2")
print("print(x, type(x))")
guess = input("What will print? ")
print("Answer: 3 <class 'int'>")
if "3" in guess and "int" in guess.lower():
    print("Correct! Floor division gives int.")
    score += 1
else:
    print("7 // 2 = 3 (int). Regular / would give 3.5 (float).")

# Round 5
print("\n--- Round 5 ---")
print("name = 'Aarav'")
print("print(name * 2)")
guess = input("What will print? ")
print("Answer: AaravAarav")
if guess == "AaravAarav":
    print("Correct! String * int repeats the string.")
    score += 1
else:
    print("'Aarav' * 2 = 'AaravAarav'. Strings can be repeated with *.")

print(f"\nScore: {score} / 5")
