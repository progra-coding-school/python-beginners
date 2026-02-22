# Program Code: LIST-LR-02
# Title: Predict the Output — What Will Python Print?
# Cognitive Skill: Logical Reasoning (Predicting output)
# Topic: Lists in Python
#
# Problem Statement:
#   A real programmer can READ code and know what it will print —
#   before even touching the keyboard to run it.
#   In this activity, you will look at code snippets involving lists
#   and predict exactly what Python will print.
#
# Solution:
#   Work through 5 challenges. For each, study the code carefully,
#   type your predicted output, then see the actual result with an
#   explanation of WHY Python prints that.
#
# Reflection:
#   1. Which challenge was trickiest — indexing, slicing, sorting, or loops?
#   2. What is the difference between index 0 and index -1?
#   3. If you sliced a list of 5 items with [1:4], how many items do you get?
#   4. Why does Python number list items starting from 0 and not 1?

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
    slow_print("  LIST-LR-02 | Predict the Output")
    slow_print("  What Will Python Print?")
    print_line("═")
    print()
    slow_print("  Read the code snippet carefully.")
    slow_print("  Then type what you think Python will print.")
    slow_print("  No running the code — use your brain! 🧠")
    print()

def show_code(lines):
    """Display a code block neatly."""
    print_line()
    print("  CODE:")
    print_line()
    for line in lines:
        print(f"    {line}")
    print_line()
    print()

def ask_prediction():
    return input("  Your prediction: ").strip()

def check_answer(user_answer, correct_answer, explanation, score):
    """Check prediction, print result, return updated score."""
    # Normalise both sides: strip whitespace, lowercase
    user_norm = user_answer.replace(" ", "").lower()
    correct_norm = str(correct_answer).replace(" ", "").lower()

    if user_norm == correct_norm:
        slow_print("  ✅ Correct! Well predicted!")
        score += 1
    else:
        slow_print(f"  ❌ Not quite.")
        slow_print(f"     Python actually prints: {correct_answer}")
    print()
    slow_print("  EXPLANATION:")
    for line in explanation:
        slow_print(f"    {line}")
    print()
    time.sleep(0.5)
    return score

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
#  CHALLENGES
# ─────────────────────────────────────────────

def challenge_1(score):
    """Indexing — accessing an element by index."""
    print_line("═")
    slow_print("  CHALLENGE 1 — Who Is at Position 2?")
    print_line("═")
    print()

    code = [
        'students = ["Aarav", "Diya", "Kabir"]',
        'print(students[2])',
    ]
    show_code(code)
    slow_print("  Aarav made a list of students in his class.")
    slow_print('  What will print(students[2]) display?')
    print()

    user = ask_prediction()
    input("\n  Press ENTER to see the answer...\n")

    # Run it
    students = ["Aarav", "Diya", "Kabir"]
    actual = students[2]
    explanation = [
        "List index starts at 0.",
        "  Index 0 → 'Aarav'",
        "  Index 1 → 'Diya'",
        "  Index 2 → 'Kabir'   ← this is what gets printed",
    ]
    return check_answer(user, actual, explanation, score)

def challenge_2(score):
    """Slicing — what part of the list comes out."""
    print_line("═")
    slow_print("  CHALLENGE 2 — Slicing Diya's Marks")
    print_line("═")
    print()

    code = [
        'marks = [88, 74, 91, 65, 80]',
        'print(marks[1:4])',
    ]
    show_code(code)
    slow_print("  Diya recorded her marks for 5 subjects.")
    slow_print("  What does marks[1:4] print?")
    slow_print("  (Hint: slicing goes from start index UP TO, but NOT including, end index)")
    print()

    user = ask_prediction()
    input("\n  Press ENTER to see the answer...\n")

    marks = [88, 74, 91, 65, 80]
    actual = marks[1:4]
    explanation = [
        "marks[1:4] means: take items from index 1 up to (NOT including) index 4.",
        "  Index 0 → 88",
        "  Index 1 → 74  ✓ start here",
        "  Index 2 → 91  ✓",
        "  Index 3 → 65  ✓",
        "  Index 4 → 80  ✗ stop before this",
        f"  Result: {actual}",
    ]
    return check_answer(user, str(actual), explanation, score)

def challenge_3(score):
    """After sort(), what is the first item?"""
    print_line("═")
    slow_print("  CHALLENGE 3 — Kabir's Cricket Scores After Sorting")
    print_line("═")
    print()

    code = [
        'scores = [67, 23, 89, 45]',
        'scores.sort()',
        'print(scores[0])',
    ]
    show_code(code)
    slow_print("  Kabir sorted his cricket scores. What will scores[0] be?")
    slow_print("  (Hint: sort() arranges numbers in ascending order — smallest first)")
    print()

    user = ask_prediction()
    input("\n  Press ENTER to see the answer...\n")

    scores = [67, 23, 89, 45]
    scores.sort()
    actual = scores[0]
    explanation = [
        "sort() arranges the list from smallest to largest.",
        f"  After sort → {scores}",
        "  Index 0 is always the FIRST item after sorting.",
        f"  So scores[0] = {actual}",
    ]
    return check_answer(user, str(actual), explanation, score)

def challenge_4(score):
    """After append and pop, what does len() return?"""
    print_line("═")
    slow_print("  CHALLENGE 4 — How Many Items Are Left?")
    print_line("═")
    print()

    code = [
        'team = ["Aarav", "Diya", "Kabir", "Riya"]',
        'team.append("Arjun")',
        'team.pop()',
        'team.pop()',
        'print(len(team))',
    ]
    show_code(code)
    slow_print("  The team list changes a few times. What will len(team) print?")
    slow_print("  (Hint: count the adds and removes carefully!)")
    print()

    user = ask_prediction()
    input("\n  Press ENTER to see the answer...\n")

    team = ["Aarav", "Diya", "Kabir", "Riya"]
    team.append("Arjun")
    team.pop()
    team.pop()
    actual = len(team)
    explanation = [
        "Let's count:",
        "  Start       → ['Aarav', 'Diya', 'Kabir', 'Riya']  (4 items)",
        "  append('Arjun') → adds 1 item  → 5 items",
        "  pop()       → removes last item → 4 items",
        "  pop()       → removes last item → 3 items",
        f"  len(team) = {actual}",
    ]
    return check_answer(user, str(actual), explanation, score)

def challenge_5(score):
    """Enumerate loop — predict the printed output."""
    print_line("═")
    slow_print("  CHALLENGE 5 — What Does the Loop Print?  [BOSS CHALLENGE]")
    print_line("═")
    print()

    code = [
        'fruits = ["mango", "banana", "apple"]',
        'for i, fruit in enumerate(fruits):',
        '    print(i, fruit)',
    ]
    show_code(code)
    slow_print("  This loop uses enumerate(). What will it print? (line by line)")
    slow_print('  Type your answer like this: "0 mango / 1 banana / 2 apple"')
    slow_print("  Use / between lines.")
    print()

    user = ask_prediction()
    input("\n  Press ENTER to see the answer...\n")

    fruits = ["mango", "banana", "apple"]
    output_lines = []
    for i, fruit in enumerate(fruits):
        output_lines.append(f"{i} {fruit}")
    actual_display = " / ".join(output_lines)

    explanation = [
        "enumerate() gives each item its INDEX number automatically.",
        "  i=0, fruit='mango'   → prints: 0 mango",
        "  i=1, fruit='banana'  → prints: 1 banana",
        "  i=2, fruit='apple'   → prints: 2 apple",
        "",
        "  Full output:",
    ]
    for line in output_lines:
        explanation.append(f"    {line}")

    return check_answer(user, actual_display, explanation, score)

# ─────────────────────────────────────────────
#  REFLECTION
# ─────────────────────────────────────────────

def show_reflection():
    print_line("═")
    slow_print("  REFLECTION — Think About It")
    print_line("═")
    print()
    slow_print("  1. Which challenge was trickiest — indexing, slicing,")
    slow_print("     sorting, or loops? Why?")
    print()
    slow_print("  2. What is the difference between index 0 and index -1?")
    print()
    slow_print("  3. If you sliced a list of 5 items with [1:4],")
    slow_print("     how many items do you get?")
    print()
    slow_print("  4. Why does Python number list items starting from 0")
    slow_print("     and not 1?")
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
