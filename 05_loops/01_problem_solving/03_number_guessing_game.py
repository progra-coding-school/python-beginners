# Program Code: LP-PS-03
# Title: Number Guessing Game
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Loops in Python

# Big question: Build a full number guessing game with hints, attempts, and replay.
# Break it into smaller problems — each one handled by a loop.

import random

def play_game():
    # Step 1: Set up the game
    secret = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    guessed = False

    print(f"\nI'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts. Good luck!")
    print()

    # Step 2: Main guess loop (while — unknown number of guesses)
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts

        try:
            guess = int(input(f"Attempt {attempts}/{max_attempts} — Your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1
            continue

        # Step 3: Give hints using comparison
        if guess == secret:
            guessed = True
            break
        elif guess < secret:
            if secret - guess <= 10:
                print(f"  Too low — but you're VERY CLOSE! ({remaining} left)")
            else:
                print(f"  Too low! ({remaining} attempt(s) left)")
        else:
            if guess - secret <= 10:
                print(f"  Too high — but you're VERY CLOSE! ({remaining} left)")
            else:
                print(f"  Too high! ({remaining} attempt(s) left)")

    # Step 4: End of game message
    print()
    if guessed:
        if attempts == 1:
            print(f"AMAZING! You got it on the FIRST try! The number was {secret}.")
        elif attempts <= 3:
            print(f"Excellent! You guessed it in {attempts} attempts!")
        else:
            print(f"Well done! You got it in {attempts} attempts.")
    else:
        print(f"Out of attempts! The secret number was {secret}.")

    return guessed, attempts

# Step 5: Replay loop (loop until player says no)
total_games = 0
total_wins = 0

while True:
    won, attempts = play_game()
    total_games += 1
    if won:
        total_wins += 1

    print()
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        break

# Step 6: Final stats
print()
print("=== Your Stats ===")
print(f"Games played: {total_games}")
print(f"Games won:    {total_wins}")
print(f"Win rate:     {total_wins/total_games*100:.0f}%")
print("Thanks for playing!")

# Think:
# 1. How would you add a HIGH SCORE that tracks the fewest attempts ever?
# 2. How would you make the game harder by narrowing the hint range?
