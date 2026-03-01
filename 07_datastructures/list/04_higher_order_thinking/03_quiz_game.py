# Quiz Game – Powered by Lists
# Two parallel lists: questions[i] pairs with answers[i]
questions = [
    "What is the index of the first item in a list?",
    "Which method adds an item to the END of a list?",
    "Which method removes the LAST item from a list?",
    "What keyword checks if an item EXISTS in a list?",
    "Which method sorts a list in ascending order?",
]

answers = [
    "0",
    "append",
    "pop",
    "in",
    "sort",
]

score = 0
total = len(questions)

print("You will be asked", total, "questions.")
print()

for i in range(total):
    print("Q" + str(i + 1) + " of " + str(total) + ": " + questions[i])
    player_answer = input("Your answer: ").strip().lower()
    if player_answer == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Answer:", answers[i])
    print()

print("Score:", score, "/", total)
if score == total:
    print("Perfect score! Python List Master!")
elif score >= 3:
    print("Great effort! Almost there!")
else:
    print("Keep practising — you will get it!")
