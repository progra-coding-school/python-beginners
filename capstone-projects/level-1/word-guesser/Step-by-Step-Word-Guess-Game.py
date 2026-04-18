word = "india"
clues = ["A country", "In Asia", "Famous for cricket"]

print("🎮 Guess the Word Letter by Letter")

# Show clues
print("\nClues:")
for clue in clues:
    print("-", clue)

# Create empty progress
progress = ["_", "_", "_", "_", "_"]

index = 0

while index < len(word):
    attempts = 6
    correct_letter = word[index]

    print("\nGuess letter", index + 1)

    while attempts > 0:
        print("Word:", progress)

        guess = input("Enter a letter: ").lower()

        if guess == correct_letter:
            print("✅ Correct!")
            progress[index] = guess
            break
        else:
            attempts = attempts - 1
            print("❌ Wrong. Attempts left:", attempts)

    if attempts == 0:
        print("Game Over! The word was:", word)
        break

    index = index + 1

# Final check
if "_" not in progress:
    print("\n🎉 You guessed the word:", word)