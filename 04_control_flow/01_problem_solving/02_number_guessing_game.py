# Program Code: CF-PS-02
# Title: Number Guessing Game
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Control Flow in Python

# Big question: Build a game where the user guesses a secret number.
# Break it down: pick number, allow attempts, give hints, declare result.

import random

# Step 1: Set up
secret = random.randint(1, 20)
max_attempts = 5
attempts = 0

print("I'm thinking of a number between 1 and 20.")
print(f"You have {max_attempts} attempts.")

# Step 2: Game loop — repeat until guess is right or attempts run out
while attempts < max_attempts:
    attempts += 1
    guess = int(input(f"Attempt {attempts}: Enter your guess: "))

    # Step 3: Give hint
    if guess == secret:
        print(f"Correct! You guessed it in {attempts} attempt(s)!")
        break
    elif guess < secret:
        print("Too low! Try higher.")
    else:
        print("Too high! Try lower.")

    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"{remaining} attempt(s) left.")

# Step 4: End result
else:
    print(f"Game over! The number was {secret}.")

# Think:
# 1. What does the 'else' on a while loop mean? When does it run?
# 2. How would you add a scoring system (more points for fewer attempts)?
