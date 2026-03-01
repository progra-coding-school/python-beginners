# Program Code: LIST-FC-03
# Title: Memory Recall Challenge — Remember the List!
# Cognitive Skill: Focus and Concentration (Memory + recall under pressure)
# Topic: Lists in Python

# How it works:
#   1. A list flashes on screen for a few seconds
#   2. Screen clears
#   3. You recall as many items as you can
#   4. Score = items remembered correctly

import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def show_and_hide(items, seconds):
    print()
    print("  MEMORISE THIS LIST:")
    print("  " + "-" * 30)
    for idx, item in enumerate(items):
        print("  " + str(idx + 1) + ". " + item)
    print("  " + "-" * 30)
    print("  You have", seconds, "seconds...")
    print()
    time.sleep(seconds)
    clear()

def check_recall(original, recalled):
    score  = 0
    missed = []
    for item in original:
        if item.lower() in [r.lower() for r in recalled]:
            score += 1
        else:
            missed.append(item)
    return score, missed

rounds = [
    {
        "title":   "Round 1 — Fruits",
        "items":   ["Mango", "Apple", "Banana", "Grapes", "Orange"],
        "seconds": 5,
    },
    {
        "title":   "Round 2 — Python Keywords",
        "items":   ["for", "while", "if", "elif", "else", "in", "print"],
        "seconds": 7,
    },
    {
        "title":   "Round 3 — Indian Cities",
        "items":   ["Chennai", "Delhi", "Mumbai", "Kolkata", "Jaipur", "Kochi", "Pune", "Hyderabad"],
        "seconds": 8,
    },
]

print("=== Memory Recall Challenge ===")
print("A list will flash on screen. Read it carefully.")
print("Then type each item you remember, one per line.")
print("Type DONE when you have finished recalling.")
print()
input("Press Enter to start the first round...")

total_score    = 0
total_possible = 0

for rd in rounds:
    clear()
    print()
    print("  " + rd["title"])
    print()
    show_and_hide(rd["items"], rd["seconds"])

    print("  " + rd["title"])
    print("  What items do you remember? (type DONE when finished)")
    print()

    recalled = []
    while True:
        entry = input("  > ").strip()
        if entry.lower() == "done":
            break
        if entry:
            recalled.append(entry)

    score, missed = check_recall(rd["items"], recalled)
    total_score    += score
    total_possible += len(rd["items"])

    print()
    print("  You remembered:", score, "/", len(rd["items"]))
    if missed:
        print("  Missed:", missed)
    print()
    input("  Press Enter for the next round...")
    clear()

print("=== Challenge Complete ===")
print("Total Score:", total_score, "/", total_possible)
percentage = round((total_score / total_possible) * 100)
print("Accuracy   :", str(percentage) + "%")
print()
if percentage == 100:
    print("Perfect recall! Your memory is exceptional!")
elif percentage >= 70:
    print("Strong performance! Great concentration!")
elif percentage >= 50:
    print("Good effort! Keep training your memory!")
else:
    print("Keep practising — memory improves with effort!")
