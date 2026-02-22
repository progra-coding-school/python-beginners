# Program Code: LIST-FC-01
# Title: Spot the Difference — Which List Changed?
# Cognitive Skill: Focus & Concentration (Attention to detail)
# Topic: Lists in Python
#
# Problem Statement:
#   A list looks almost the same — but something is different.
#   Can you spot exactly what changed between List A and List B?
#   Programmers who debug code need this exact skill: noticing tiny
#   differences between two versions of the same data.
#
# Solution:
#   Work through 5 rounds. Each round shows you two lists — List A
#   and List B. One has been slightly changed from the other. You must
#   spot the difference, type your answer, then see the explanation.
#
# Reflection:
#   1. Which type of change was hardest to spot — capitalisation,
#      value change, added item, or swapped order? Why?
#   2. In real programming, tiny differences like 50 vs 500 can crash
#      a program. What habit can you build to avoid this?
#   3. How is spotting list differences like proofreading an essay?
#   4. If two lists look identical but your program gives a wrong
#      answer, what would you check first?

import time

# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def print_line(char="─", length=55):
    print(char * length)

def slow_print(text, delay=0.04):
    """Print text character by character for a typewriter effect."""
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def show_header():
    print("=" * 55)
    slow_print("  LIST-FC-01 | Spot the Difference")
    slow_print("  Which List Changed?")
    print("=" * 55)
    print()
    slow_print("  Welcome, young detective!")
    slow_print("  Two lists will appear on your screen.")
    slow_print("  One has been slightly changed from the other.")
    slow_print("  Your job: spot EXACTLY what is different.")
    slow_print("  Sharp eyes win! 👀")
    print()

def show_lists(list_a, list_b):
    """Display List A and List B side by side, clearly labelled."""
    print_line()
    print(f"  List A:  {list_a}")
    print(f"  List B:  {list_b}")
    print_line()
    print()

def ask_difference():
    print("  What is the difference between List A and List B?")
    return input("  Your answer: ").strip()

def pause_reveal():
    input("\n  Press ENTER to reveal the difference...\n")

def show_achievement(score, total):
    print("=" * 55)
    pct = (score / total) * 100 if total > 0 else 0
    print(f"  Your Score: {score} / {total}")
    print()
    if pct == 100:
        slow_print("  🏆 Sharp eyes! You are a List Detective!")
    elif pct >= 60:
        slow_print("  ✅ Good focus! Keep training your attention.")
    else:
        slow_print("  💪 Keep practising — focus takes training!")
    print("=" * 55)

def ask_got_it():
    """Ask the student if their own answer was correct."""
    ans = input("  Did you spot it correctly? (y / n): ").strip().lower()
    return ans == "y"

# ─────────────────────────────────────────────
#  ROUNDS
# ─────────────────────────────────────────────

def round_1():
    """Capitalisation changed — banana vs Banana."""
    print("=" * 55)
    slow_print("  ROUND 1 — Aarav's Fruit Basket")
    print("=" * 55)
    print()
    slow_print("  Aarav typed his fruit list twice. One has a typo.")
    slow_print("  Look very carefully at every letter!")
    print()

    list_a = ["apple", "banana", "mango"]
    list_b = ["apple", "Banana", "mango"]

    show_lists(list_a, list_b)
    ask_difference()
    pause_reveal()

    slow_print('  DIFFERENCE: In List B, "banana" became "Banana"')
    slow_print('  The letter B is UPPERCASE in List B.')
    slow_print('  In Python, "banana" != "Banana" — capitalisation matters!')
    print()
    slow_print("  WHY IT MATTERS: If you search for 'banana' in List B,")
    slow_print("  Python will say it is NOT there — because 'Banana' != 'banana'.")
    print()

    return 1 if ask_got_it() else 0

def round_2():
    """Last number changed — 50 vs 500."""
    print("=" * 55)
    slow_print("  ROUND 2 — Diya's Cricket Score Sheet")
    print("=" * 55)
    print()
    slow_print("  Diya recorded cricket scores for 5 players.")
    slow_print("  One score was entered incorrectly. Can you find it?")
    print()

    list_a = [10, 20, 30, 40, 50]
    list_b = [10, 20, 30, 40, 500]

    show_lists(list_a, list_b)
    ask_difference()
    pause_reveal()

    slow_print("  DIFFERENCE: The last number changed from 50 to 500.")
    slow_print("  One extra zero was added — a common typing mistake!")
    print()
    slow_print("  WHY IT MATTERS: A score of 500 in cricket is impossible")
    slow_print("  for one player! Always check if numbers look reasonable.")
    print()

    return 1 if ask_got_it() else 0

def round_3():
    """Item added at the end — Meera added to team."""
    print("=" * 55)
    slow_print("  ROUND 3 — Kabir's Class Register")
    print("=" * 55)
    print()
    slow_print("  Kabir has a list of his friends. One list has an")
    slow_print("  extra name that should not be there. Spot it!")
    print()

    list_a = ["Aarav", "Diya", "Kabir"]
    list_b = ["Aarav", "Diya", "Kabir", "Meera"]

    show_lists(list_a, list_b)
    ask_difference()
    pause_reveal()

    slow_print('  DIFFERENCE: List B has one EXTRA item — "Meera"')
    slow_print("  She was added at the end. List A has 3 items.")
    slow_print("  List B has 4 items.")
    print()
    slow_print("  HOW TO CHECK: Use len() — len(List A)=3, len(List B)=4.")
    slow_print("  If lengths differ, something was added or removed!")
    print()

    return 1 if ask_got_it() else 0

def round_4():
    """Two items swapped — green and blue switched positions."""
    print("=" * 55)
    slow_print("  ROUND 4 — Riya's Colour Palette")
    print("=" * 55)
    print()
    slow_print("  Riya sorted her paint colours. But in one list,")
    slow_print("  two colours have swapped positions. Which ones?")
    print()

    list_a = ["red", "green", "blue"]
    list_b = ["red", "blue", "green"]

    show_lists(list_a, list_b)
    ask_difference()
    pause_reveal()

    slow_print('  DIFFERENCE: "green" and "blue" swapped positions.')
    slow_print('  List A: index 1 = "green", index 2 = "blue"')
    slow_print('  List B: index 1 = "blue",  index 2 = "green"')
    print()
    slow_print("  WHY IT MATTERS: Order matters in lists!")
    slow_print("  If your code depends on position (index), a swap")
    slow_print("  will give the wrong result silently.")
    print()

    return 1 if ask_got_it() else 0

def round_5():
    """Last two numbers swapped — 4,5 vs 5,4."""
    print("=" * 55)
    slow_print("  ROUND 5 — Aarav's Number Sequence  [BOSS ROUND]")
    print("=" * 55)
    print()
    slow_print("  Aarav wrote a sequence of numbers twice.")
    slow_print("  The lists look VERY similar. Stay sharp!")
    slow_print("  (This one is tricky — look at every position!)")
    print()

    list_a = [1, 2, 3, 4, 5]
    list_b = [1, 2, 3, 5, 4]

    show_lists(list_a, list_b)
    ask_difference()
    pause_reveal()

    slow_print("  DIFFERENCE: The LAST TWO numbers swapped positions.")
    slow_print("  List A: ...3, 4, 5   (correct order)")
    slow_print("  List B: ...3, 5, 4   (4 and 5 are flipped!)")
    print()
    slow_print("  PRO TIP: Always compare lists item by item,")
    slow_print("  from left to right — like reading a sentence.")
    slow_print("  Do not just glance — check each index!")
    print()

    return 1 if ask_got_it() else 0

# ─────────────────────────────────────────────
#  REFLECTION
# ─────────────────────────────────────────────

def show_reflection():
    print("=" * 55)
    slow_print("  REFLECTION — Think About It")
    print("=" * 55)
    print()
    slow_print("  1. Which type of change was hardest to spot —")
    slow_print("     capitalisation, value change, added item, or")
    slow_print("     swapped order? Why?")
    print()
    slow_print("  2. In real programming, a typo like 50 vs 500 can")
    slow_print("     crash a program or give wrong results.")
    slow_print("     What habit can you build to catch such errors?")
    print()
    slow_print("  3. How is spotting list differences like")
    slow_print("     proofreading an essay before submitting it?")
    print()
    slow_print("  4. If two lists look identical but your program gives")
    slow_print("     a wrong answer, what would you check first?")
    print()
    print("=" * 55)

# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

def main():
    show_header()
    input("  Press ENTER to start Round 1...\n")

    score = 0
    total = 5

    score += round_1()
    input("  Press ENTER for Round 2...\n")

    score += round_2()
    input("  Press ENTER for Round 3...\n")

    score += round_3()
    input("  Press ENTER for Round 4...\n")

    score += round_4()
    input("  Press ENTER for Round 5 (Boss Round)...\n")

    score += round_5()

    show_achievement(score, total)
    show_reflection()

main()
