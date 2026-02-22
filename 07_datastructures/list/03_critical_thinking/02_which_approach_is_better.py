# Program Code: LIST-CT-02
# Title: Which Approach is Better? — Evaluate and Judge!
# Cognitive Skill: Critical Thinking (Approach evaluation)
# Topic: Lists in Python
#
# Problem Statement:
#   In programming, there is often MORE THAN ONE way to solve a problem.
#   But not all ways are equally good. A critical thinker asks:
#   "Is there a cleaner, simpler, safer way to do this?"
#   In this activity, you will compare two approaches side by side
#   and decide which one is better — and why.
#
# Solution:
#   Work through 3 problems. Each shows two approaches (Approach A and B).
#   You decide which is better. Then see the reasoning and key lesson.
#
# Reflection:
#   1. Is the longer code always the wrong approach? Can you think of a case where it is better?
#   2. What makes code "clean"? List 3 things a clean piece of code must have.
#   3. Why does using the RIGHT method matter even if BOTH approaches give the same answer?
#   4. Which of these three problems will you remember the next time you write list code?

import time

# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def print_line(char="─", length=60):
    print(char * length)

def slow_print(text, delay=0.04):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def show_header():
    print_line("═")
    slow_print("  LIST-CT-02 | Which Approach is Better?")
    slow_print("  Evaluate and Judge!")
    print_line("═")
    print()
    slow_print("  Two programmers, Aarav and Diya, often solve the SAME problem")
    slow_print("  in different ways. Your job is to judge who has the better approach")
    slow_print("  — and explain WHY.")
    print()
    slow_print("  Think like a code reviewer! 🔍")
    print()

def show_code_block(label, lines):
    print_line()
    print(f"  {label}:")
    print_line()
    for line in lines:
        print(f"    {line}")
    print_line()
    print()

def ask_vote():
    while True:
        choice = input("  Your answer (A or B): ").strip().upper()
        if choice in ("A", "B"):
            return choice
        print("  Please type A or B.")

def show_verdict(correct_choice, correct_label, reasons, key_lesson):
    print()
    slow_print(f"  VERDICT: Approach {correct_choice} — {correct_label} — is better.")
    print()
    slow_print("  REASONS:")
    for r in reasons:
        slow_print(f"    → {r}")
    print()
    print_line()
    slow_print("  KEY LESSON:")
    slow_print(f"    {key_lesson}")
    print_line()
    print()

def show_score(correct, total):
    print_line("═")
    print(f"  Your Score: {correct} / {total}")
    pct = (correct / total) * 100 if total > 0 else 0
    if pct == 100:
        print("  🏆 You are a List Master!")
    elif pct >= 60:
        print("  ✅ Great work! Keep practising.")
    else:
        print("  💪 Keep going — tracing takes practice!")
    print_line("═")

# ─────────────────────────────────────────────
#  PROBLEMS
# ─────────────────────────────────────────────

def problem_1(score):
    """remove() vs pop() for removing by value."""
    print_line("═")
    slow_print("  PROBLEM 1 — Removing a Specific Player from the Team")
    print_line("═")
    print()
    slow_print("  Kabir wants to remove 'Diya' from the cricket team list.")
    slow_print("  He sees two ways to do it. Which is better?")
    print()

    code_a = [
        '# Approach A — Aarav\'s way',
        'team = ["Aarav", "Diya", "Kabir", "Riya"]',
        '',
        '# Find the index first, then pop',
        'index = team.index("Diya")',
        'team.pop(index)',
        'print(team)',
    ]

    code_b = [
        '# Approach B — Diya\'s way',
        'team = ["Aarav", "Diya", "Kabir", "Riya"]',
        '',
        '# Remove directly by value',
        'team.remove("Diya")',
        'print(team)',
    ]

    show_code_block("Approach A (Aarav)", code_a)
    show_code_block("Approach B (Diya)", code_b)

    slow_print("  Both approaches remove 'Diya' from the list.")
    slow_print("  Which approach is better when you know the VALUE, not the index?")
    print()

    choice = ask_vote()
    input("\n  Press ENTER to see the verdict...\n")

    correct = "B"
    if choice == correct:
        slow_print("  ✅ Correct! Approach B is better.")
        score += 1
    else:
        slow_print(f"  ❌ Actually, Approach {correct} is better.")

    show_verdict(
        correct,
        "remove() directly",
        [
            "remove('Diya') does the job in ONE line — simple and readable.",
            "Approach A uses two steps: finding the index AND THEN popping.",
            "pop() is designed for when you know the INDEX.",
            "remove() is designed for when you know the VALUE.",
            "Always use the right tool for the right job.",
        ],
        "Use remove(value) when you know WHAT to delete. "
        "Use pop(index) when you know WHERE to delete."
    )

    # Run both live
    slow_print("  Live demo — Approach B:")
    team = ["Aarav", "Diya", "Kabir", "Riya"]
    team.remove("Diya")
    print(f"    Result: {team}")
    print()
    time.sleep(0.5)
    return score

def problem_2(score):
    """append() in a loop vs extend()."""
    print_line("═")
    slow_print("  PROBLEM 2 — Adding Multiple Items to the Shopping Cart")
    print_line("═")
    print()
    slow_print("  Riya wants to add three new items to her shopping cart at once.")
    slow_print("  She found two ways. Which is better?")
    print()

    code_a = [
        '# Approach A — Aarav\'s way',
        'cart = ["rice", "dal"]',
        'new_items = ["oil", "sugar", "ghee"]',
        '',
        '# Add each item one by one with a loop',
        'for item in new_items:',
        '    cart.append(item)',
        'print(cart)',
    ]

    code_b = [
        '# Approach B — Diya\'s way',
        'cart = ["rice", "dal"]',
        'new_items = ["oil", "sugar", "ghee"]',
        '',
        '# Add all items in one step',
        'cart.extend(new_items)',
        'print(cart)',
    ]

    show_code_block("Approach A (Aarav)", code_a)
    show_code_block("Approach B (Diya)", code_b)

    slow_print("  Both give the same final cart. Which is the BETTER approach?")
    print()

    choice = ask_vote()
    input("\n  Press ENTER to see the verdict...\n")

    correct = "B"
    if choice == correct:
        slow_print("  ✅ Correct! Approach B is better.")
        score += 1
    else:
        slow_print(f"  ❌ Actually, Approach {correct} is better.")

    show_verdict(
        correct,
        "extend() in one step",
        [
            "extend() is designed exactly for adding multiple items at once.",
            "Approach A works but writes 3 lines where 1 line is enough.",
            "extend() is faster, shorter, and easier to read.",
            "Approach A is only needed when the items to add come from different places.",
            "A good programmer avoids unnecessary loops.",
        ],
        "Use extend(another_list) to merge two lists in one step. "
        "Use append() only when adding ONE item at a time."
    )

    # Live demo
    slow_print("  Live demo — Approach B:")
    cart = ["rice", "dal"]
    new_items = ["oil", "sugar", "ghee"]
    cart.extend(new_items)
    print(f"    Result: {cart}")
    print()
    time.sleep(0.5)
    return score

def problem_3(score):
    """Multiple if-elif for search vs 'in' keyword."""
    print_line("═")
    slow_print("  PROBLEM 3 — Searching for a City  [BOSS PROBLEM]")
    print_line("═")
    print()
    slow_print("  Arjun wants to check if a city is in his travel list.")
    slow_print("  He wrote two versions. Which is better?")
    print()

    code_a = [
        '# Approach A — Arjun\'s first try',
        'cities = ["Chennai", "Mumbai", "Delhi", "Kolkata"]',
        'search = "Mumbai"',
        '',
        '# Checking one by one with if-elif',
        'if search == cities[0]:',
        '    print("Found!")',
        'elif search == cities[1]:',
        '    print("Found!")',
        'elif search == cities[2]:',
        '    print("Found!")',
        'elif search == cities[3]:',
        '    print("Found!")',
        'else:',
        '    print("Not found.")',
    ]

    code_b = [
        '# Approach B — Arjun\'s improved try',
        'cities = ["Chennai", "Mumbai", "Delhi", "Kolkata"]',
        'search = "Mumbai"',
        '',
        '# Using the "in" keyword',
        'if search in cities:',
        '    print("Found!")',
        'else:',
        '    print("Not found.")',
    ]

    show_code_block("Approach A (Manual if-elif)", code_a)
    show_code_block("Approach B (in keyword)", code_b)

    slow_print("  Both check for 'Mumbai'. But which is SMARTER?")
    slow_print("  Think about what happens if the list has 100 cities...")
    print()

    choice = ask_vote()
    input("\n  Press ENTER to see the verdict...\n")

    correct = "B"
    if choice == correct:
        slow_print("  ✅ Correct! Approach B is the clear winner.")
        score += 1
    else:
        slow_print(f"  ❌ Actually, Approach {correct} is far better.")

    show_verdict(
        correct,
        "the 'in' keyword",
        [
            "Approach A has 4 elif branches — one for every item in the list.",
            "If the list grows to 100 cities, you need 100 elif lines. Terrible!",
            "Approach B's 'in' keyword searches the WHOLE list automatically.",
            "'in' works no matter how big or small the list is — always 1 line.",
            "Approach B is clean, scalable, and readable.",
        ],
        "Python's 'in' keyword is built for searching. "
        "Never write if-elif for every item in a list."
    )

    # Live demo
    slow_print("  Live demo — Approach B:")
    cities = ["Chennai", "Mumbai", "Delhi", "Kolkata"]
    search = "Mumbai"
    if search in cities:
        print("    Found!")
    else:
        print("    Not found.")
    print()
    time.sleep(0.5)
    return score

# ─────────────────────────────────────────────
#  FINAL SUMMARY
# ─────────────────────────────────────────────

def show_summary():
    print_line("═")
    slow_print("  SUMMARY — The Better Approaches")
    print_line("═")
    print()
    summary = [
        ("1", "Remove by value",      "remove(value) — not pop(index)"),
        ("2", "Add multiple items",   "extend(list)  — not append in a loop"),
        ("3", "Search in list",       "'item in list'— not manual if-elif"),
    ]
    print(f"  {'#':<4} {'Problem':<25} {'Better Approach'}")
    print_line()
    for num, prob, approach in summary:
        print(f"  {num:<4} {prob:<25} {approach}")
    print_line()
    print()

# ─────────────────────────────────────────────
#  REFLECTION
# ─────────────────────────────────────────────

def show_reflection():
    print_line("═")
    slow_print("  REFLECTION — Think About It")
    print_line("═")
    print()
    slow_print("  1. Is the LONGER code always the wrong approach?")
    slow_print("     Can you think of a case where more lines are actually better?")
    print()
    slow_print("  2. What makes code 'clean'? List 3 things a clean piece of code must have.")
    print()
    slow_print("  3. Why does using the RIGHT method matter, even if BOTH approaches")
    slow_print("     give the same answer?")
    print()
    slow_print("  4. Which of these three problems will you remember the NEXT TIME")
    slow_print("     you write list code?")
    print()
    print_line("═")

# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

def main():
    show_header()
    input("  Press ENTER to start Problem 1...\n")

    score = 0
    total = 3

    score = problem_1(score)
    input("  Press ENTER for Problem 2...\n")

    score = problem_2(score)
    input("  Press ENTER for Problem 3 (Boss Problem)...\n")

    score = problem_3(score)

    show_summary()
    show_score(score, total)
    show_reflection()

main()
