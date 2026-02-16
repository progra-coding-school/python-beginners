# Program Code: 07-application-02
# Title: Spelling Bee Game

# The program picks a word and shows it for a moment.
# The player has to type the correct spelling from memory.

import time
import os

words = ["elephant", "butterfly", "dinosaur", "chocolate", "beautiful",
         "crocodile", "umbrella", "strawberry", "adventure", "wonderful"]

score = 0
total_rounds = 5

print("=== Spelling Bee Game ===")
print("A word will flash on screen. Remember it and type it correctly!\n")

for round_number in range(total_rounds):
    word = words[round_number]

    print("Round", round_number + 1, "- Look at the word carefully...")
    print(">>>", word, "<<<")
    time.sleep(3)

    # Clear screen effect (print empty lines)
    print("\n" * 20)

    answer = input("Type the word: ")

    if answer.lower() == word:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct spelling was:", word)
    print()

print("=== Game Over ===")
print("Your score:", score, "/", total_rounds)

if score == total_rounds:
    print("Perfect! You are a Spelling Champion!")
elif score >= 3:
    print("Great job! Keep practicing!")
else:
    print("Good try! Practice more and try again!")
