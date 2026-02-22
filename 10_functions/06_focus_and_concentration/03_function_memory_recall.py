# Program Code: FN-FC-03
# Title: Function Memory Recall
# Cognitive Skill: Focus and Concentration (Memory Recall)
# Topic: Functions in Python

# How well do you remember functions?
# No notes — recall from memory!

score = 0

print("=== Function Memory Recall ===")
print("Answer from memory. No looking back!")
print()

# --- Part 1: Syntax recall ---
print("--- Part 1: Keywords and Syntax ---")
print()

print("Q1: What keyword is used to CREATE a function?")
ans = input("> ").strip().lower()
if ans == "def":
    print("Correct! 'def' defines a function.")
    score += 1
else:
    print("Answer: def")
print()

print("Q2: What keyword sends a value back from a function?")
ans = input("> ").strip().lower()
if ans == "return":
    print("Correct! 'return' sends the result back to the caller.")
    score += 1
else:
    print("Answer: return")
print()

print("Q3: What do you call a variable inside the function definition parentheses?")
ans = input("> ").strip().lower()
if "parameter" in ans:
    print("Correct! Those are called parameters (or formal parameters).")
    score += 1
else:
    print("Answer: parameter")
print()

print("Q4: What do you call the value you pass when CALLING the function?")
ans = input("> ").strip().lower()
if "argument" in ans:
    print("Correct! The values you pass in a call are called arguments.")
    score += 1
else:
    print("Answer: argument")
print()

# --- Part 2: Concept recall ---
print("--- Part 2: Concepts ---")
print()

print("Q5: If a function has no return statement, what does it return?")
ans = input("> ").strip().lower()
if "none" in ans:
    print("Correct! Python automatically returns None.")
    score += 1
else:
    print("Answer: None")
print()

print("Q6: Are variables inside a function accessible OUTSIDE it?")
ans = input("> ").strip().lower()
if ans in ["no", "false", "not accessible", "no, local"]:
    print("Correct! Function variables are LOCAL — they exist only inside.")
    score += 1
else:
    print("Answer: No — they are local to the function.")
print()

print("Q7: What is the Golden Rule for functions? (hint: one...)")
ans = input("> ").strip().lower()
if "one" in ans and ("job" in ans or "task" in ans or "thing" in ans):
    print("Correct! Each function should do ONE job.")
    score += 1
else:
    print("Answer: Each function should do ONE job.")
print()

print("Q8: What is the benefit of using functions instead of repeating code?")
ans = input("> ").strip().lower()
if any(word in ans for word in ["reuse", "reusable", "once", "fix"]):
    print("Correct! Write once, reuse anywhere. Fix in one place.")
    score += 1
else:
    print("Answer: Reuse — write once, call many times. Fix in one place.")
print()

# Final summary
print("═" * 40)
print(f"Memory Recall Score: {score} / 8")
print()
print("Quick Reference:")
print("  def       → create a function")
print("  return    → send value back")
print("  parameter → placeholder in definition")
print("  argument  → actual value in the call")
print("  local     → variable lives inside function only")
print("  None      → returned if no return statement")
print("  One Job   → each function does ONE thing")
print("═" * 40)
