# Program Code: LIST-HOT-03
# Title: Quiz Game — Build a Game Powered by Lists!
# Cognitive Skill: Higher Order Thinking (Design and build a complete system)
# Topic: Lists in Python
#
# ════════════════════════════════════════════════════════
#  DESIGN THINKING SECTION — How Do We Build This Game?
# ════════════════════════════════════════════════════════
#
#  Before writing a single line of code, a good programmer DESIGNS.
#
#  What do we need for a quiz game?
#  → A list of questions
#  → A list of answers
#  → A way to ask each question
#  → A way to check the player's answer
#  → A way to track the score
#
#  Data Plan:
#  → questions  = ["Q1", "Q2", ...]   (list of question strings)
#  → answers    = ["A1", "A2", ...]   (list of correct answers)
#  → score      = 0                   (integer, increases per correct answer)
#
#  Why two separate lists instead of one?
#  → questions[0] pairs with answers[0], questions[1] with answers[1], etc.
#  → Both lists share the same index — this is called parallel lists.
#
# ════════════════════════════════════════════════════════
#  THE QUIZ GAME
# ════════════════════════════════════════════════════════

import time

print("=" * 55)
print("       🧠 PROGRA PYTHON QUIZ GAME 🧠")
print("=" * 55)
print()

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

print(f"  Welcome! You will be asked {total} questions.")
print("  Type your answer and press Enter.")
print("-" * 55)
print()

for i in range(total):
    print(f"  Question {i + 1} of {total}")
    print(f"  {questions[i]}")
    player_answer = input("  Your answer: ").strip().lower()

    if player_answer == answers[i].lower():
        print("  ✅ Correct!\n")
        score += 1
    else:
        print(f"  ❌ Not quite. The answer was: {answers[i]}\n")

    time.sleep(0.5)

print("=" * 55)
print("  QUIZ COMPLETE!")
print(f"  Your Score: {score} / {total}")

if score == total:
    print("  🏆 Perfect score! You're a Python List Master!")
elif score >= 3:
    print("  🌟 Great effort! Almost there!")
else:
    print("  💪 Keep practising — you'll get it!")

print("=" * 55)

# ════════════════════════════════════════════════════════
#  THINK ABOUT IT
# ════════════════════════════════════════════════════════
#
#  1. What would happen if len(questions) != len(answers)?
#
#  2. How would you add a new question to this game?
#     (Hint: which two lists do you need to update?)
#
#  3. What if you wanted the questions to appear in
#     RANDOM order every time? Which Python module could help?
#
#  4. How would you track wrong answers in a third list
#     so the player can review them at the end?
#
#  EXTENSION CHALLENGE:
#  → Add a "wrong_answers" list.
#  → After the quiz, print each question the player got wrong
#    along with the correct answer.
# ════════════════════════════════════════════════════════
