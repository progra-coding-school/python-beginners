# Program Code: 07-application-03
# Title: Quiz Game

# A quiz game using lists to store questions, options, and answers.

questions = [
    "What is the capital of India?",
    "How many legs does a spider have?",
    "Which planet is known as the Red Planet?",
    "What is the largest animal on Earth?",
    "How many days are there in a leap year?"
]

options = [
    ["a) Mumbai", "b) New Delhi", "c) Chennai", "d) Kolkata"],
    ["a) 6", "b) 8", "c) 10", "d) 4"],
    ["a) Venus", "b) Jupiter", "c) Mars", "d) Saturn"],
    ["a) Elephant", "b) Giraffe", "c) Blue Whale", "d) Shark"],
    ["a) 364", "b) 365", "c) 366", "d) 367"]
]

answers = ["b", "b", "c", "c", "c"]

score = 0

print("=== Quiz Game ===")
print("Answer by typing a, b, c, or d\n")

for i in range(len(questions)):
    print("Q" + str(i + 1) + ":", questions[i])
    for option in options[i]:
        print("  ", option)

    player_answer = input("Your answer: ").lower()

    if player_answer == answers[i]:
        print("Correct!\n")
        score = score + 1
    else:
        print("Wrong! The answer was:", answers[i], "\n")

print("=== Results ===")
print("Score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent! Full marks!")
elif score >= 3:
    print("Well done!")
else:
    print("Keep learning and try again!")
