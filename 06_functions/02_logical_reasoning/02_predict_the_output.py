# Program Code: FN-LR-02
# Title: Predict the Output
# Cognitive Skill: Logical Reasoning (Pattern Finding)
# Topic: Functions in Python

# Study each set of functions.
# Predict what gets printed when the code runs.

score = 0

# Setup — read these functions carefully first!
def square(n):
    return n * n

def cube(n):
    return n * n * n

def is_even(n):
    return n % 2 == 0

def describe(n):
    if is_even(n):
        label = "even"
    else:
        label = "odd"
    return f"{n} is {label}"

print("Study the 4 functions above, then answer:")
print()

# --- Q1 ---
print("Q1: print(square(4))")
answer = input("Your answer: ")
actual = square(4)
print(f"Output: {actual}")
if answer.strip() == str(actual):
    score += 1
    print("Correct!")
print()

# --- Q2 ---
print("Q2: print(cube(3))")
answer = input("Your answer: ")
actual = cube(3)
print(f"Output: {actual}")
if answer.strip() == str(actual):
    score += 1
    print("Correct!")
print()

# --- Q3 ---
print("Q3: print(square(3) + cube(2))")
answer = input("Your answer: ")
actual = square(3) + cube(2)
print(f"Output: {actual}  (square(3)=9, cube(2)=8, 9+8=17)")
if answer.strip() == str(actual):
    score += 1
    print("Correct!")
print()

# --- Q4 ---
print("Q4: print(is_even(7))")
answer = input("Your answer (True/False): ")
actual = is_even(7)
print(f"Output: {actual}")
if answer.strip().lower() == str(actual).lower():
    score += 1
    print("Correct!")
print()

# --- Q5 ---
print("Q5: print(describe(10))")
answer = input("Your answer: ")
actual = describe(10)
print(f"Output: {actual}")
if answer.strip() == actual:
    score += 1
    print("Correct!")
print()

# --- Q6 ---
print("Q6: What does this print?")
print("""
  result = square(is_even(4))
  print(result)
""")
print("Hint: is_even(4) returns True. True is treated as 1 in Python.")
answer = input("Your answer: ")
actual = square(is_even(4))  # square(True) = square(1) = 1
print(f"Output: {actual}  (is_even(4)=True=1, square(1)=1)")
if answer.strip() == str(actual):
    score += 1
    print("Correct!")
print()

print(f"Score: {score} / 6")
