# Program Code: LP-UN-03
# Title: for vs while — When to Use Which?
# Cognitive Skill: Understanding
# Topic: Loops in Python

# for  → use when you know the COUNT or have a SEQUENCE to loop through
# while → use when you loop UNTIL a CONDITION changes

print("=== Use for when count/sequence is known ===")

# Good use of for:
for i in range(1, 6):
    print(f"  Question {i}")

subjects = ["Maths", "Science", "English"]
for subject in subjects:
    print(f"  Subject: {subject}")

print()

print("=== Use while when condition-based ===")

# Good use of while:
battery = 100
while battery > 20:
    battery -= 15
    print(f"  Battery: {battery}%")
print("  Low battery warning!")

print()

# --- Same task: for vs while ---
print("=== Same task — two ways ===")

print("Using for:")
for i in range(1, 6):
    print(f"  {i} × 3 = {i * 3}")

print("Using while:")
i = 1
while i <= 5:
    print(f"  {i} × 3 = {i * 3}")
    i += 1

print()

# --- When while is BETTER than for ---
print("=== While is better: unknown count ===")
print("Guess the secret number (between 1 and 10):")
secret = 7
guesses = 0
while True:
    guess = int(input("Your guess: "))
    guesses += 1
    if guess == secret:
        print(f"Correct! You got it in {guesses} guess(es).")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
# We don't know HOW MANY guesses — while is perfect here.

print()

# --- Decision guide ---
print("=== When to use which? ===")
print("for   → 'for each student in the list'")
print("for   → 'repeat exactly 10 times'")
print("for   → 'for every character in a word'")
print("while → 'keep asking until correct answer'")
print("while → 'keep running until battery dies'")
print("while → 'keep looping until user types quit'")

# Think:
# 1. Would you use for or while to simulate rolling a dice until you get a 6?
# 2. Could you always replace a for loop with a while loop? How?
