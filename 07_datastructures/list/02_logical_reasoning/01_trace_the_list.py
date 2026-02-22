# Program Code: LIST-LR-01
# Title: Trace the List — What's in the Box After Each Step?
# Cognitive Skill: Logical Reasoning (Tracing values)
# Topic: Lists in Python
#
# Problem Statement:
#   A list changes every time we run an operation on it.
#   Can you trace each step and predict what the final list looks like?
#   A good programmer does NOT need to run code to know the answer —
#   they trace it in their head, step by step.
#
# Solution:
#   Work through 5 rounds. Each round shows you a starting list and a
#   series of operations. You predict the final list, then see the answer
#   revealed step by step.
#
# Reflection:
#   1. Which operation was hardest to trace — append, insert, pop, or sort? Why?
#   2. When you got an answer wrong, what step did you miss?
#   3. How is tracing a list like following a recipe in a kitchen?
#   4. Why is it important for a programmer to predict output WITHOUT running the code?

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
    print_line("═")
    slow_print("  LIST-LR-01 | Trace the List")
    slow_print("  What's in the Box After Each Step?")
    print_line("═")
    print()
    slow_print("  Welcome, young programmer!")
    slow_print("  In this activity, you will watch a list change step")
    slow_print("  by step — and predict what it looks like at the end.")
    slow_print("  No running code. Just your brain! 🧠")
    print()

def show_score(correct, total):
    print_line()
    print(f"  Your Score: {correct} / {total}")
    pct = (correct / total) * 100 if total > 0 else 0
    if pct == 100:
        print("  🏆 You are a List Master!")
    elif pct >= 60:
        print("  ✅ Great work! Keep practising.")
    else:
        print("  💪 Keep going — tracing takes practice!")
    print_line()

def ask_answer(prompt="  Your answer (type the list, e.g. [1, 2, 3]): "):
    return input(prompt).strip()

def pause():
    input("\n  Press ENTER to reveal the answer...\n")

def trace_step(step_num, operation, result):
    """Print one step of the trace."""
    time.sleep(0.3)
    print(f"    Step {step_num}: {operation}")
    print(f"            → List is now: {result}")

# ─────────────────────────────────────────────
#  ROUNDS
# ─────────────────────────────────────────────

def round_1():
    """Simple append and remove."""
    print_line()
    print("  ROUND 1 — Aarav's Snack Box")
    print_line()
    print()
    print("  Starting list:")
    print('    snacks = ["chips", "mango", "biscuit"]')
    print()
    print("  Operations:")
    print('    snacks.append("chocolate")')
    print('    snacks.remove("mango")')
    print()
    answer = ask_answer()
    pause()

    # Trace
    snacks = ["chips", "mango", "biscuit"]
    slow_print("  Tracing step by step:")
    print(f'    Start      : {snacks}')
    snacks.append("chocolate")
    trace_step(1, 'snacks.append("chocolate")', snacks)
    snacks.remove("mango")
    trace_step(2, 'snacks.remove("mango")', snacks)
    print()
    correct_answer = str(snacks)
    print(f"  FINAL LIST: {snacks}")
    print()
    return check_answer(answer, snacks)

def round_2():
    """insert at index + pop."""
    print_line()
    print("  ROUND 2 — Diya's Cricket Team Order")
    print_line()
    print()
    print("  Starting list:")
    print('    team = ["Aarav", "Kabir", "Diya"]')
    print()
    print("  Operations:")
    print('    team.insert(1, "Riya")')
    print('    team.pop()')
    print()
    answer = ask_answer()
    pause()

    team = ["Aarav", "Kabir", "Diya"]
    slow_print("  Tracing step by step:")
    print(f'    Start      : {team}')
    team.insert(1, "Riya")
    trace_step(1, 'team.insert(1, "Riya")   → inserts "Riya" at index 1', team)
    team.pop()
    trace_step(2, "team.pop()               → removes the LAST item", team)
    print()
    print(f"  FINAL LIST: {team}")
    print()
    return check_answer(answer, team)

def round_3():
    """sort + append."""
    print_line()
    print("  ROUND 3 — Kabir's Maths Marks")
    print_line()
    print()
    print("  Starting list:")
    print("    marks = [78, 45, 92, 60]")
    print()
    print("  Operations:")
    print("    marks.sort()")
    print("    marks.append(55)")
    print()
    answer = ask_answer()
    pause()

    marks = [78, 45, 92, 60]
    slow_print("  Tracing step by step:")
    print(f'    Start      : {marks}')
    marks.sort()
    trace_step(1, "marks.sort()      → sorts in ascending order", marks)
    marks.append(55)
    trace_step(2, "marks.append(55)  → adds 55 at the end", marks)
    print()
    print(f"  FINAL LIST: {marks}")
    print()
    return check_answer(answer, marks)

def round_4():
    """Multiple ops in sequence."""
    print_line()
    print("  ROUND 4 — Riya's Shopping List")
    print_line()
    print()
    print("  Starting list:")
    print('    cart = ["rice", "dal", "oil"]')
    print()
    print("  Operations:")
    print('    cart.append("sugar")')
    print('    cart.insert(0, "salt")')
    print('    cart.remove("oil")')
    print('    cart.append("ghee")')
    print()
    answer = ask_answer()
    pause()

    cart = ["rice", "dal", "oil"]
    slow_print("  Tracing step by step:")
    print(f'    Start      : {cart}')
    cart.append("sugar")
    trace_step(1, 'cart.append("sugar")', cart)
    cart.insert(0, "salt")
    trace_step(2, 'cart.insert(0, "salt") → inserts at the front', cart)
    cart.remove("oil")
    trace_step(3, 'cart.remove("oil")', cart)
    cart.append("ghee")
    trace_step(4, 'cart.append("ghee")', cart)
    print()
    print(f"  FINAL LIST: {cart}")
    print()
    return check_answer(answer, cart)

def round_5():
    """Harder ops: extend, reverse, pop with index."""
    print_line()
    print("  ROUND 5 — Aarav's Cricket Scores  [BOSS ROUND]")
    print_line()
    print()
    print("  Starting list:")
    print("    scores = [34, 12, 56]")
    print()
    print("  Operations:")
    print("    scores.extend([20, 45])")
    print("    scores.reverse()")
    print("    scores.pop(2)")
    print()
    answer = ask_answer()
    pause()

    scores = [34, 12, 56]
    slow_print("  Tracing step by step:")
    print(f'    Start      : {scores}')
    scores.extend([20, 45])
    trace_step(1, "scores.extend([20, 45]) → adds 20 and 45 at the end", scores)
    scores.reverse()
    trace_step(2, "scores.reverse()        → flips the whole list", scores)
    scores.pop(2)
    trace_step(3, "scores.pop(2)           → removes item at INDEX 2", scores)
    print()
    print(f"  FINAL LIST: {scores}")
    print()
    return check_answer(answer, scores)

# ─────────────────────────────────────────────
#  ANSWER CHECKER
# ─────────────────────────────────────────────

def check_answer(user_input, actual_list):
    """
    Compare the user's typed answer to the actual list.
    We try a flexible match: compare string representations
    with spaces stripped, or try eval if it looks like a list.
    """
    correct = False
    # Try to parse user input as a Python list
    try:
        parsed = eval(user_input)
        if parsed == actual_list:
            correct = True
    except Exception:
        pass

    # Also do a loose string comparison (strip whitespace)
    if not correct:
        user_clean = user_input.replace(" ", "").lower()
        actual_clean = str(actual_list).replace(" ", "").lower()
        if user_clean == actual_clean:
            correct = True

    if correct:
        slow_print("  ✅ Correct! Excellent tracing!")
    else:
        slow_print(f"  ❌ Not quite. The correct answer is: {actual_list}")
        slow_print("     Study the step-by-step trace above to see where it changed.")
    print()
    time.sleep(0.5)
    return 1 if correct else 0

# ─────────────────────────────────────────────
#  REFLECTION
# ─────────────────────────────────────────────

def show_reflection():
    print_line("═")
    slow_print("  REFLECTION — Think About It")
    print_line("═")
    print()
    slow_print("  1. Which operation was hardest to trace — append, insert,")
    slow_print("     pop, or sort? Why?")
    print()
    slow_print("  2. When you got an answer wrong, at which step did you go wrong?")
    print()
    slow_print("  3. How is tracing a list like following a recipe step by step?")
    print()
    slow_print("  4. Why should a programmer be able to predict output WITHOUT")
    slow_print("     running the code?")
    print()
    print_line("═")

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

    show_score(score, total)
    show_reflection()

main()
