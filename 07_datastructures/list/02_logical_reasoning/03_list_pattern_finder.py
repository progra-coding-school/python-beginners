# Program Code: LIST-LR-03
# Title: Find the Pattern — What Comes Next?
# Cognitive Skill: Logical Reasoning (Pattern finding)
# Topic: Lists in Python
#
# Problem Statement:
#   Lists often store items that follow a pattern — numbers that grow by 2,
#   days of the week in order, powers of a number, and more.
#   Can you spot the rule and predict what comes next?
#
# Solution:
#   Work through 5 challenges. Each shows you a list with the last item
#   replaced by a '?'. Spot the pattern, type what comes next, then
#   see the explanation with the rule clearly stated.
#
# Reflection:
#   1. Which pattern was hardest to spot — arithmetic, geometric, or string-based?
#   2. How would you store a pattern like this in a list using a loop instead of typing each item?
#   3. Can you think of a pattern from everyday life that could be stored in a Python list?
#   4. What happens if a pattern BREAKS in the middle? How would you find the mistake?

import time

# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def print_line(char="─", length=55):
    print(char * length)

def slow_print(text, delay=0.04):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def show_header():
    print_line("═")
    slow_print("  LIST-LR-03 | Find the Pattern")
    slow_print("  What Comes Next?")
    print_line("═")
    print()
    slow_print("  A list is not always random — sometimes it follows a RULE.")
    slow_print("  Your job: look at the list, find the rule, and predict")
    slow_print("  what the NEXT item should be.")
    print()
    slow_print("  Look carefully. Some patterns are sneaky! 🔍")
    print()

def show_list_with_question(items, label="my_list"):
    """Display the list with the last slot shown as ?"""
    display = items[:-1] + ["?"]
    print_line()
    print(f"    {label} = {display}")
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

def check_answer(user_input, correct_answer, rule_msg, full_list, score):
    """Compare user answer to correct, print rule, return updated score."""
    user_clean = user_input.strip().lower()
    correct_clean = str(correct_answer).lower()

    if user_clean == correct_clean:
        slow_print("  ✅ Correct! You spotted the pattern!")
        score += 1
    else:
        slow_print(f"  ❌ Not quite. The next item is: {correct_answer}")

    print()
    slow_print("  THE RULE:")
    slow_print(f"    {rule_msg}")
    print()
    slow_print(f"  Full list: {full_list}")
    print()
    time.sleep(0.5)
    return score

# ─────────────────────────────────────────────
#  CHALLENGES
# ─────────────────────────────────────────────

def challenge_1(score):
    """Even numbers — increase by 2."""
    print_line("═")
    slow_print("  CHALLENGE 1 — Aarav's Even Numbers")
    print_line("═")
    print()
    slow_print("  Aarav is making a list of even numbers for maths class.")
    slow_print("  Look at his list carefully:")
    print()

    partial = [2, 4, 6, 8, 10]
    show_list_with_question(partial, "evens")

    slow_print("  What is the PATTERN?")
    slow_print("  What number should replace the '?'?")
    print()
    user = input("  Your answer: ").strip()
    input("\n  Press ENTER to reveal...\n")

    correct = 10
    rule = "Each number increases by 2. (Add 2 each time — these are even numbers!)"
    full = [2, 4, 6, 8, 10]
    return check_answer(user, correct, rule, full, score)

def challenge_2(score):
    """Days of the week pattern."""
    print_line("═")
    slow_print("  CHALLENGE 2 — Diya's Weekly Planner")
    print_line("═")
    print()
    slow_print("  Diya is writing the days of the week in a list for her planner.")
    slow_print("  But she stopped early. What comes next?")
    print()

    partial = ["Mon", "Tue", "Wed", "Thu", "?"]
    show_list_with_question(partial, "days")

    slow_print('  What should replace "?"?')
    print()
    user = input("  Your answer: ").strip()
    input("\n  Press ENTER to reveal...\n")

    correct = "Fri"
    rule = "Days of the week in order: Mon → Tue → Wed → Thu → Fri → Sat → Sun"
    full = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    return check_answer(user, correct, rule, full, score)

def challenge_3(score):
    """Powers of 3 — geometric sequence."""
    print_line("═")
    slow_print("  CHALLENGE 3 — Kabir's Cricket Tournament Rounds  [TRICKY]")
    print_line("═")
    print()
    slow_print("  In a cricket tournament, the number of teams playing in each")
    slow_print("  round keeps getting multiplied. Look at the pattern:")
    print()

    partial = [1, 3, 9, 27, "?"]
    show_list_with_question(partial, "teams")

    slow_print("  What number should replace '?'?")
    slow_print("  (Hint: look at how each number relates to the one before it)")
    print()
    user = input("  Your answer: ").strip()
    input("\n  Press ENTER to reveal...\n")

    correct = 81
    rule = "Each number is multiplied by 3: 1×3=3, 3×3=9, 9×3=27, 27×3=81 (Powers of 3)"
    full = [1, 3, 9, 27, 81]
    return check_answer(user, correct, rule, full, score)

def challenge_4(score):
    """String repetition pattern."""
    print_line("═")
    slow_print("  CHALLENGE 4 — Riya's Letter Art")
    print_line("═")
    print()
    slow_print("  Riya is making a string art pattern using the letter 'a'.")
    slow_print("  Each item in her list adds one more 'a'. What comes next?")
    print()

    partial = ["a", "aa", "aaa", "aaaa", "?"]
    show_list_with_question(partial, "pattern")

    slow_print('  What string should replace "?"?')
    print()
    user = input("  Your answer: ").strip()
    input("\n  Press ENTER to reveal...\n")

    correct = "aaaaa"
    rule = "Each item adds one more 'a': len 1, 2, 3, 4, 5... (repetition pattern)"
    full = ["a", "aa", "aaa", "aaaa", "aaaaa"]
    return check_answer(user, correct, rule, full, score)

def challenge_5(score):
    """Decreasing by 10 — countdown pattern."""
    print_line("═")
    slow_print("  CHALLENGE 5 — Aarav's Countdown Score  [BOSS CHALLENGE]")
    print_line("═")
    print()
    slow_print("  In Aarav's game, the score decreases by the same amount")
    slow_print("  after each level. Look at the scores recorded after each level:")
    print()

    partial = [100, 90, 80, 70, "?"]
    show_list_with_question(partial, "scores")

    slow_print("  What number should replace '?'?")
    slow_print("  BONUS QUESTION: What is the RULE for this pattern?")
    print()
    user = input("  Your answer (just the number): ").strip()
    bonus = input("  Bonus — describe the rule in your own words: ").strip()
    input("\n  Press ENTER to reveal...\n")

    correct = 60
    rule = "Each number decreases by 10. This is an arithmetic sequence with a common difference of -10."
    full = [100, 90, 80, 70, 60]

    print()
    if bonus.strip():
        slow_print(f"  Your rule: \"{bonus}\"")
        slow_print("  Great thinking! Here is the official rule:")
    return check_answer(user, correct, rule, full, score)

# ─────────────────────────────────────────────
#  REFLECTION
# ─────────────────────────────────────────────

def show_reflection():
    print_line("═")
    slow_print("  REFLECTION — Think About It")
    print_line("═")
    print()
    slow_print("  1. Which pattern was hardest to spot — arithmetic (add/subtract),")
    slow_print("     geometric (multiply), or string-based? Why?")
    print()
    slow_print("  2. How would you CREATE one of these patterns in a list")
    slow_print("     using a loop instead of typing each item manually?")
    print()
    slow_print("  3. Can you think of a pattern from everyday life that could")
    slow_print("     be stored as a Python list?")
    slow_print("     (e.g. school timetable, bus timings, cricket overs...)")
    print()
    slow_print("  4. What happens if a pattern BREAKS in the middle?")
    slow_print("     How would you find the mistake?")
    print()
    print_line("═")

# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

def main():
    show_header()
    input("  Press ENTER to start Challenge 1...\n")

    score = 0
    total = 5

    score = challenge_1(score)
    input("  Press ENTER for Challenge 2...\n")

    score = challenge_2(score)
    input("  Press ENTER for Challenge 3...\n")

    score = challenge_3(score)
    input("  Press ENTER for Challenge 4...\n")

    score = challenge_4(score)
    input("  Press ENTER for Challenge 5 (Boss Challenge)...\n")

    score = challenge_5(score)

    show_score(score, total)
    show_reflection()

main()
