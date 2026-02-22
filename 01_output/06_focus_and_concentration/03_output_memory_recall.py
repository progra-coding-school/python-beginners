# Program Code: OUT-FC-03
# Title: Output Memory Recall
# Cognitive Skill: Focus and Concentration (Memory Recall)
# Topic: Output in Python

# How well do you remember output rules?
# Answer from memory — no notes!

score = 0

print("=== Output Memory Recall ===")
print("No looking back. Answer from memory!")
print()

# --- Part 1: Syntax ---
print("--- Part 1: Syntax ---")
print()

print("Q1: What Python function is used to display output on screen?")
ans = input("> ").strip().lower()
if "print" in ans:
    print("Correct! print() is the output function.")
    score += 1
else:
    print("Answer: print()")
print()

print("Q2: What are the 3 types of quotes you can use for strings?")
ans = input("> ").strip().lower()
if ("single" in ans or "'" in ans) and ("double" in ans or '"' in ans) and ("triple" in ans or '"""' in ans or "'''" in ans):
    print("Correct! Single ' , double \" , triple ''' or \"\"\"")
    score += 1
else:
    print("Answer: Single ('), double (\"), triple (''' or \"\"\")")
print()

print("Q3: What does the 'sep' parameter in print() do?")
ans = input("> ").strip().lower()
if any(w in ans for w in ["separator", "separate", "between", "items"]):
    print("Correct! sep changes the separator between multiple items (default is space).")
    score += 1
else:
    print("Answer: sep changes what goes BETWEEN items. Default is a space.")
print()

print("Q4: What does the 'end' parameter in print() do?")
ans = input("> ").strip().lower()
if any(w in ans for w in ["end", "after", "newline", "next line"]):
    print("Correct! end changes what comes AFTER the output (default is newline).")
    score += 1
else:
    print("Answer: end changes what comes after the print. Default is \\n (new line).")
print()

# --- Part 2: Concepts ---
print("--- Part 2: Concepts ---")
print()

print("Q5: What does print('5' + '5') display?")
ans = input("> ").strip()
if ans == "55":
    print("Correct! String + string = joined text, not arithmetic.")
    score += 1
else:
    print("Answer: 55 (string concatenation, not addition)")
print()

print("Q6: What does print(5 + 5) display?")
ans = input("> ").strip()
if ans == "10":
    print("Correct! Number + number = arithmetic.")
    score += 1
else:
    print("Answer: 10 (integer arithmetic)")
print()

print("Q7: What does print() return? (the return value, not the output)")
ans = input("> ").strip().lower()
if "none" in ans:
    print("Correct! print() always returns None.")
    score += 1
else:
    print("Answer: None — print() shows output but returns nothing.")
print()

print("Q8: What symbol is used in f-strings to embed a variable?")
ans = input("> ").strip()
if "{" in ans and "}" in ans:
    print("Correct! Curly braces {} hold variables in f-strings.")
    score += 1
else:
    print("Answer: { } curly braces — e.g., f'Hello, {name}!'")
print()

# --- Summary ---
print("═" * 40)
print(f"Memory Recall Score: {score} / 8")
print()
print("Quick Reference:")
print("  print()          → display output")
print("  ' or \"          → string quotes")
print("  ''' or \"\"\"      → multiline strings")
print("  sep=','          → change item separator")
print("  end=''           → change line ending")
print("  f'text {var}'    → embed variable in string")
print("  print() returns  → None")
print("  '5' + '5'        → '55'  (text join)")
print("  5 + 5            → 10   (arithmetic)")
print("═" * 40)
