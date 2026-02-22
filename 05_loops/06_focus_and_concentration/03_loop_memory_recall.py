# Program Code: LP-FC-03
# Title: Loop Memory Recall
# Cognitive Skill: Focus and Concentration (Memory Recall)
# Topic: Loops in Python

# How well do you remember loops?
# Answer from memory — no notes!

score = 0

print("=== Loop Memory Recall ===")
print("No notes. Answer from memory!")
print()

# --- Part 1: Keywords ---
print("--- Part 1: Keywords ---")
print()

print("Q1: What keyword starts a for loop?")
ans = input("> ").strip().lower()
if ans == "for":
    print("Correct!")
    score += 1
else:
    print("Answer: for")
print()

print("Q2: What keyword starts a loop that runs 'until a condition is False'?")
ans = input("> ").strip().lower()
if ans == "while":
    print("Correct!")
    score += 1
else:
    print("Answer: while")
print()

print("Q3: What keyword exits a loop immediately?")
ans = input("> ").strip().lower()
if ans == "break":
    print("Correct!")
    score += 1
else:
    print("Answer: break")
print()

print("Q4: What keyword skips the rest of the current iteration?")
ans = input("> ").strip().lower()
if ans == "continue":
    print("Correct!")
    score += 1
else:
    print("Answer: continue")
print()

# --- Part 2: Concepts ---
print("--- Part 2: Concepts ---")
print()

print("Q5: What does range(1, 10) produce? (first and last values)")
ans = input("> ").strip()
if "1" in ans and "9" in ans:
    print("Correct! 1 to 9 (stop value 10 is excluded)")
    score += 1
else:
    print("Answer: 1 to 9 — range is start-inclusive, stop-exclusive")
print()

print("Q6: Which loop is better when you don't know how many times to repeat?")
ans = input("> ").strip().lower()
if "while" in ans:
    print("Correct! while loop — runs until the condition becomes False")
    score += 1
else:
    print("Answer: while loop")
print()

print("Q7: What is an 'accumulator' in a loop?")
ans = input("> ").strip().lower()
if any(w in ans for w in ["total", "sum", "collect", "add", "build"]):
    print("Correct! A variable that collects/builds up a value across iterations.")
    score += 1
else:
    print("Answer: A variable (like total=0) that collects values as the loop runs.")
print()

print("Q8: If the outer loop runs 4 times and the inner loop runs 3 times,")
print("    how many total iterations does the inner loop body execute?")
ans = input("> ").strip()
if ans == "12":
    print("Correct! 4 × 3 = 12")
    score += 1
else:
    print("Answer: 12 (outer × inner = total)")
print()

# --- Summary ---
print("═" * 40)
print(f"Memory Recall Score: {score} / 8")
print()
print("Quick Reference:")
print("  for     → known count / sequence")
print("  while   → condition-based / unknown count")
print("  break   → exit the loop now")
print("  continue → skip this iteration")
print("  range(s,e,step) → generates a sequence of numbers")
print("  accumulator → starts at 0, builds total inside loop")
print("  nested loops → outer × inner = total inner iterations")
print("═" * 40)
