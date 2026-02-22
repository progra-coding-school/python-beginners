# Program Code: DT-HOT-01
# Title: Reverse Engineer — Decode the Types
# Cognitive Skill: Higher Order Thinking (Working backwards)
# Topic: Data Types in Python

score = 0

# Round 1
print("--- Round 1 ---")
print("Output: <class 'float'>")
print("Code: print(type(result))")
guess = input("What could 'result' be? Give one example value: ")
print("Possible answers: 3.14, 0.5, 10.0, 7/2, etc.")
print("Any value with a decimal OR the result of / is float.")
score += 1
input("Press Enter for Round 2...")

# Round 2
print("--- Round 2 ---")
print("Output: HelloHelloHello")
print("Code: print(word * count)")
word_guess = input("What type is 'word'? ")
count_guess = input("What type is 'count'? ")
print("Answer: word = str (e.g. 'Hello'), count = int (e.g. 3)")
if word_guess.lower() == "str" and count_guess.lower() == "int":
    print("Correct!")
    score += 1
else:
    print("str * int repeats the string. 'Hello' * 3 = 'HelloHelloHello'")
input("Press Enter for Round 3...")

# Round 3
print("--- Round 3 ---")
print("Output: 8892")
print("Code: print(a + b)")
guess = input("What types are a and b? (e.g. 'both int', 'both str') ")
print("Answer: both str. '88' + '92' = '8892' (string join, not addition)")
if "str" in guess.lower():
    print("Correct!")
    score += 1
else:
    print("If a and b were int, result would be 180. But 8892 = string join.")
input("Press Enter for Round 4...")

# Round 4 — challenge
print("--- Round 4 (Challenge) ---")
print("Output: 7")
print("Code: z = int(float(user_input))")
print("What was user_input?")
guess = input("Give a possible value for user_input: ")
print("Possible: '7.9', '7.1', '7.0', '7.5' — any string of a decimal between 7 and 8")
print("float('7.9') = 7.9, then int(7.9) = 7")
score += 1

print(f"\nScore: {score} / 4")
