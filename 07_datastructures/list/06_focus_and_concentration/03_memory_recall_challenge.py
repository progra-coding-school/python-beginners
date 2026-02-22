# Program Code: LIST-FC-03
# Title: Memory Recall Challenge — Remember the List!
# Cognitive Skill: Focus and Concentration (Memory + recall under pressure)
# Topic: Lists in Python
#
# ════════════════════════════════════════════════════════
#  HOW THIS WORKS
# ════════════════════════════════════════════════════════
#
#  1. A list of items flashes on screen for a few seconds.
#  2. The screen clears.
#  3. You must recall as many items as you can.
#  4. Your score = items you remembered correctly.
#
#  This trains your brain to HOLD a list in memory —
#  just like a computer holds a list in RAM!
#
# ════════════════════════════════════════════════════════

import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def show_and_hide(items, seconds):
    print("\n  🧠 MEMORISE THIS LIST:\n")
    print("  " + "-" * 35)
    for idx, item in enumerate(items):
        print(f"  {idx + 1}. {item}")
    print("  " + "-" * 35)
    print(f"\n  You have {seconds} seconds...\n")
    time.sleep(seconds)
    clear()

def check_recall(original, recalled):
    score = 0
    missed = []
    for item in original:
        if item.lower() in [r.lower() for r in recalled]:
            score += 1
        else:
            missed.append(item)
    return score, missed

# ── Round configuration ──────────────────────────────────
rounds = [
    {
        "title": "Round 1 — Fruits 🍎",
        "items": ["Mango", "Apple", "Banana", "Grapes", "Orange"],
        "seconds": 5,
    },
    {
        "title": "Round 2 — Python Keywords 🐍",
        "items": ["for", "while", "if", "elif", "else", "in", "print"],
        "seconds": 7,
    },
    {
        "title": "Round 3 — Indian Cities 🏙️",
        "items": ["Chennai", "Delhi", "Mumbai", "Kolkata", "Jaipur", "Kochi", "Pune", "Hyderabad"],
        "seconds": 8,
    },
]

# ── Game loop ────────────────────────────────────────────
print("=" * 55)
print("  🧠 MEMORY RECALL CHALLENGE — LIST EDITION")
print("=" * 55)
print()
print("  A list will flash on screen. Read it carefully.")
print("  Then type each item you remember, one per line.")
print("  Type DONE when you have finished recalling.")
print()
input("  Press Enter to start the first round...")

total_score = 0
total_possible = 0

for round_data in rounds:
    clear()
    print(f"\n  {round_data['title']}")
    print()
    show_and_hide(round_data["items"], round_data["seconds"])

    print(f"  {round_data['title']}")
    print("  What items do you remember? (type DONE when finished)\n")

    recalled = []
    while True:
        entry = input("  > ").strip()
        if entry.lower() == "done":
            break
        if entry:
            recalled.append(entry)

    score, missed = check_recall(round_data["items"], recalled)
    total_score += score
    total_possible += len(round_data["items"])

    print()
    print(f"  ✅ You remembered: {score} / {len(round_data['items'])}")
    if missed:
        print(f"  ❌ You missed: {missed}")
    print()
    input("  Press Enter for the next round...")
    clear()

# ── Final results ────────────────────────────────────────
print("=" * 55)
print("  CHALLENGE COMPLETE!")
print(f"  Total Score: {total_score} / {total_possible}")
percentage = round((total_score / total_possible) * 100)
print(f"  Accuracy   : {percentage}%")
print()

if percentage == 100:
    print("  🏆 Perfect recall! Your memory is exceptional!")
elif percentage >= 70:
    print("  🌟 Strong performance! Great concentration!")
elif percentage >= 50:
    print("  👍 Good effort! Keep training your memory!")
else:
    print("  💪 Keep practising — memory improves with effort!")

print("=" * 55)

# ════════════════════════════════════════════════════════
#  THINK ABOUT IT
# ════════════════════════════════════════════════════════
#
#  1. How does this game use PARALLEL lists? (items + recall)
#
#  2. Why does the game use .lower() when comparing answers?
#     What problem does this solve?
#
#  3. What list method could you use to find items that
#     are in the original list but NOT in recalled?
#     (Hint: there's a way using loops and "not in")
#
#  4. How would you add a TIMER to the recall phase
#     to make the challenge harder?
# ════════════════════════════════════════════════════════
