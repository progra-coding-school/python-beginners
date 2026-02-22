# Program Code: LP-KN-03
# Title: The while Loop
# Cognitive Skill: Knowledge
# Topic: Loops in Python

# A while loop repeats AS LONG AS the condition is True.
# Use it when you don't know how many times to repeat.

# --- Basic while loop ---
count = 1
while count <= 5:
    print("Count:", count)
    count += 1    # IMPORTANT: update the variable or loop runs forever!

print()

# --- Countdown ---
rocket = 5
while rocket > 0:
    print(f"T-minus {rocket}...")
    rocket -= 1
print("Blast off!")

print()

# --- User-controlled loop ---
# Keep asking until the user types 'quit'
print("Type something (or 'quit' to stop):")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    print("You typed:", user_input)

print()

# --- Loop with a condition ---
password = "progra123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered = input("Enter password: ")
    attempts += 1
    if entered == password:
        print("Access granted!")
        break
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"Wrong password. {remaining} attempt(s) left.")
else:
    print("Too many wrong attempts. Locked out!")

# Think:
# 1. What happens if you forget to write count += 1 inside the loop?
# 2. When would you choose while True over while count <= 10?
