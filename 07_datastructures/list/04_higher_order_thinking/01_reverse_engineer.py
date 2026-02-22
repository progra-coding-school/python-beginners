# Program Code: LIST-HOT-01
# Title: Reverse Engineer — Figure Out the Code from the Output!
# Cognitive Skill: Higher Order Thinking (Reverse engineering)
# Topic: Lists in Python
#
# Problem Statement:
#   A great programmer does not just write code — they can READ the output
#   of code and work BACKWARDS to figure out what produced it.
#   This skill is called REVERSE ENGINEERING.
#   You will see a STARTING list and a FINAL list (or output).
#   Your job: figure out WHICH list operation(s) caused this change!
#
# Solution:
#   Work through 4 challenges. For each one:
#     - Study the STARTING list and the FINAL list carefully.
#     - Type your best guess for the code that produced the change.
#     - See the real answer revealed with a step-by-step explanation.
#     - A score is tracked across all 4 challenges.
#
# Reflection:
#   1. How is reverse engineering a list like being a detective on a mystery case?
#   2. Which challenge was hardest to reverse engineer — and why?
#   3. If you saw only the FINAL list and not the start, could you still figure
#      out what happened? What extra information would you need?
#   4. How could this skill of "reading outputs and figuring out the code"
#      help you fix bugs in your own programs?

import time

# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def print_line(char="─", length=55):
    print(char * length)

def slow_print(text, delay=0.03):
    """Print text character by character for a typewriter effect."""
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def pause(msg="  Press ENTER to reveal the answer..."):
    input(f"\n{msg}\n")

def show_header():
    print("=" * 55)
    slow_print("  LIST-HOT-01 | Reverse Engineer the List!")
    slow_print("  Figure Out the Code from the Output!")
    print("=" * 55)
    print()
    slow_print("  Welcome, Detective Programmer! 🔍")
    slow_print("  You will see a STARTING list and a FINAL list.")
    slow_print("  Your mission: figure out what CODE caused the change!")
    print()
    slow_print("  This is what real programmers do when they debug —")
    slow_print("  they READ the output and THINK BACKWARDS.")
    print()

def show_score_summary(score, total):
    print("=" * 55)
    print(f"  YOUR FINAL SCORE: {score} / {total}")
    pct = (score / total) * 100
    if pct == 100:
        slow_print("  🏆 Perfect! You are a true reverse engineering master!")
    elif pct >= 75:
        slow_print("  ✅ Excellent work! You think like a real programmer!")
    elif pct >= 50:
        slow_print("  💡 Good effort! Study the explanations and try again.")
    else:
        slow_print("  Keep going! Reverse engineering takes practice. You've got this!")
    print("=" * 55)

def ask_guess(challenge_num):
    print()
    print(f"  CHALLENGE {challenge_num} — What code produced this change?")
    print()
    print("  Example answers you could type:")
    print('    team.append("Meera")')
    print('    scores.remove(30)')
    print('    fruits.sort()')
    print()
    guess = input("  Your guess (type the list operation): ").strip()
    return guess

def check_keywords(guess, keywords):
    """
    Check if the user's guess contains the key method name(s).
    We do a loose check — if the right method word appears, it counts.
    Returns True if at least one keyword matches.
    """
    guess_lower = guess.lower().replace(" ", "")
    for kw in keywords:
        if kw.lower() in guess_lower:
            return True
    return False

def reveal_answer(correct, user_guess, accepted_keywords, explanation_lines, code_demo):
    """Print the reveal section for a challenge."""
    print()
    print_line("─")
    slow_print("  REVEALING THE ANSWER...")
    print_line("─")
    print()

    if check_keywords(user_guess, accepted_keywords):
        slow_print("  ✅ You got it! Great reverse engineering!")
        result = 1
    else:
        slow_print("  ❌ Not quite — but let's learn from it!")
        slow_print(f"  The correct code was: {correct}")
        result = 0

    print()
    slow_print("  HOW IT WORKS — Step by Step:")
    for line in explanation_lines:
        time.sleep(0.2)
        print(f"    {line}")

    print()
    slow_print("  PROOF — Let's run the code right now:")
    time.sleep(0.3)
    code_demo()
    print()
    time.sleep(0.5)
    return result

# ─────────────────────────────────────────────
#  CHALLENGE 1 — append
# ─────────────────────────────────────────────

def challenge_1():
    print("=" * 55)
    print("  CHALLENGE 1 — The New Team Member")
    print("=" * 55)
    print()
    slow_print("  Aarav's cricket team had 3 players.")
    slow_print("  Then something happened and now there are 4 players.")
    print()

    print("  STARTING LIST:")
    print('    team = ["Aarav", "Diya", "Kabir"]')
    print()
    print("  FINAL LIST:")
    print('    team = ["Aarav", "Diya", "Kabir", "Meera"]')
    print()
    slow_print("  Something was added to the END of the list.")
    slow_print("  🔍 What single line of code did this?")

    user_guess = ask_guess(1)
    pause()

    explanation = [
        '"Meera" appeared at the END of the list.',
        "When we add to the END of a list, we use .append().",
        'team.append("Meera") adds "Meera" after "Kabir".',
        "append() always adds at the LAST position.",
    ]

    def demo():
        team = ["Aarav", "Diya", "Kabir"]
        print(f"    Before: {team}")
        team.append("Meera")
        print(f"    After:  {team}  ✅")

    return reveal_answer(
        correct='team.append("Meera")',
        user_guess=user_guess,
        accepted_keywords=["append"],
        explanation_lines=explanation,
        code_demo=demo
    )

# ─────────────────────────────────────────────
#  CHALLENGE 2 — remove / pop
# ─────────────────────────────────────────────

def challenge_2():
    print("=" * 55)
    print("  CHALLENGE 2 — The Missing Score")
    print("=" * 55)
    print()
    slow_print("  Diya had a list of 5 cricket scores.")
    slow_print("  One score disappeared. Can you figure out how?")
    print()

    print("  STARTING LIST:")
    print("    scores = [10, 20, 30, 40, 50]")
    print()
    print("  FINAL LIST:")
    print("    scores = [10, 20, 40, 50]")
    print()
    slow_print("  The number 30 is gone. It was the MIDDLE of the list.")
    slow_print("  🔍 What single line of code removed it?")
    slow_print("  💡 HINT: There are TWO possible correct answers here!")

    user_guess = ask_guess(2)
    pause()

    explanation = [
        "30 was removed from the list. It was at index 2.",
        "TWO methods can do this:",
        "  Option A: scores.remove(30)  → removes by VALUE",
        "  Option B: scores.pop(2)      → removes by INDEX",
        "Both produce the exact same final list!",
        "remove() is used when you know the VALUE you want gone.",
        "pop()    is used when you know the INDEX (position).",
    ]

    def demo():
        print("    Option A — using remove():")
        scores_a = [10, 20, 30, 40, 50]
        print(f"      Before: {scores_a}")
        scores_a.remove(30)
        print(f"      After:  {scores_a}  ✅")
        print()
        print("    Option B — using pop(2):")
        scores_b = [10, 20, 30, 40, 50]
        print(f"      Before: {scores_b}")
        scores_b.pop(2)
        print(f"      After:  {scores_b}  ✅")

    return reveal_answer(
        correct="scores.remove(30)  OR  scores.pop(2)",
        user_guess=user_guess,
        accepted_keywords=["remove", "pop"],
        explanation_lines=explanation,
        code_demo=demo
    )

# ─────────────────────────────────────────────
#  CHALLENGE 3 — sort (ascending)
# ─────────────────────────────────────────────

def challenge_3():
    print("=" * 55)
    print("  CHALLENGE 3 — The Tidy Fruit Basket")
    print("=" * 55)
    print()
    slow_print("  Kabir's fruit list was in random order.")
    slow_print("  Someone neatened it up. Can you spot how?")
    print()

    print("  STARTING LIST:")
    print('    fruits = ["mango", "apple", "banana"]')
    print()
    print("  FINAL LIST:")
    print('    fruits = ["apple", "banana", "mango"]')
    print()
    slow_print("  The items are now in ALPHABETICAL order (A to Z).")
    slow_print("  Nothing was added or removed — just rearranged.")
    slow_print("  🔍 What single line of code did this?")

    user_guess = ask_guess(3)
    pause()

    explanation = [
        "The list went from random order to alphabetical (A to Z).",
        'apple < banana < mango  — this is alphabetical ascending order.',
        "fruits.sort() arranges strings from A to Z automatically.",
        "sort() works on numbers too — it sorts from smallest to largest.",
        "No items were added or removed — the same 3 items, just reordered.",
    ]

    def demo():
        fruits = ["mango", "apple", "banana"]
        print(f"    Before: {fruits}")
        fruits.sort()
        print(f"    After:  {fruits}  ✅")

    return reveal_answer(
        correct="fruits.sort()",
        user_guess=user_guess,
        accepted_keywords=["sort"],
        explanation_lines=explanation,
        code_demo=demo
    )

# ─────────────────────────────────────────────
#  CHALLENGE 4 — sort(reverse=True)
# ─────────────────────────────────────────────

def challenge_4():
    print("=" * 55)
    print("  CHALLENGE 4 — The BOSS ROUND — Kabir's Rankings!")
    print("=" * 55)
    print()
    slow_print("  Kabir had a list of match scores in random order.")
    slow_print("  After ONE operation, the list became a TOP-SCORE RANKING —")
    slow_print("  the HIGHEST score first, and the LOWEST score last.")
    print()

    print("  STARTING LIST:")
    print("    rankings = [5, 3, 8, 1, 9]")
    print()
    print("  FINAL LIST:")
    print("    rankings = [9, 8, 5, 3, 1]")
    print()
    slow_print("  The list is sorted LARGEST to SMALLEST — that's descending order.")
    slow_print("  🔍 What single line of code did this?")
    slow_print("  💡 HINT: Think about sort() — but with a special option...")

    user_guess = ask_guess(4)
    pause()

    explanation = [
        "The list went from random to DESCENDING order (largest first).",
        "9 → 8 → 5 → 3 → 1   (each number is smaller than the one before)",
        "sort() by itself gives ASCENDING order (smallest first).",
        "To get DESCENDING order, we add: reverse=True",
        "rankings.sort(reverse=True) — this is the key!",
        'The "reverse=True" part is called a KEYWORD ARGUMENT.',
        "It tells sort() to flip the direction — big to small.",
    ]

    def demo():
        rankings = [5, 3, 8, 1, 9]
        print(f"    Before:  {rankings}")
        rankings.sort(reverse=True)
        print(f"    After:   {rankings}  ✅")
        print()
        print("    Compare with plain sort():")
        rankings2 = [5, 3, 8, 1, 9]
        rankings2.sort()
        print(f"    sort()             → {rankings2}  (ascending — small to big)")
        rankings3 = [5, 3, 8, 1, 9]
        rankings3.sort(reverse=True)
        print(f"    sort(reverse=True) → {rankings3}  (descending — big to small)")

    return reveal_answer(
        correct="rankings.sort(reverse=True)",
        user_guess=user_guess,
        accepted_keywords=["reverse=true", "reverse =true", "reverse= true", "reverse=True"],
        explanation_lines=explanation,
        code_demo=demo
    )

# ─────────────────────────────────────────────
#  REFLECTION
# ─────────────────────────────────────────────

def show_reflection():
    print("=" * 55)
    slow_print("  REFLECTION — Think About It")
    print("=" * 55)
    print()
    slow_print("  1. How is reverse engineering a list like being a")
    slow_print("     detective solving a mystery case?")
    print()
    slow_print("  2. Which challenge was the hardest to reverse engineer?")
    slow_print("     What made it tricky?")
    print()
    slow_print("  3. In Challenge 2, BOTH remove() and pop() gave the")
    slow_print("     same result. Can you think of a case where only")
    slow_print("     ONE of them would work?")
    print()
    slow_print("  4. How could the skill of 'reading output and figuring")
    slow_print("     out what code ran' help you debug your own programs?")
    print()
    print("=" * 55)

# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

def main():
    show_header()
    input("  Press ENTER to start Challenge 1...\n")

    score = 0
    total = 4

    score += challenge_1()
    input("\n  Press ENTER for Challenge 2...\n")

    score += challenge_2()
    input("\n  Press ENTER for Challenge 3...\n")

    score += challenge_3()
    input("\n  Press ENTER for Challenge 4 — BOSS ROUND...\n")

    score += challenge_4()

    show_score_summary(score, total)
    show_reflection()

main()
