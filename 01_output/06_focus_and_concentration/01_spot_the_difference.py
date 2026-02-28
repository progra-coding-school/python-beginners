# Program Code: OUT-FC-01
# Title: Spot the Difference — Output
# Cognitive Skill: Focus and Concentration (Attention to Detail)
# Topic: Output in Python

# Each pair looks almost identical — but produces DIFFERENT output.
# Look at every character!

score = 0

print("=== Spot the Difference — Output ===")
print()

# --- Round 1 ---
print("Round 1:")
print('  Code A: print("5" + "3")')
print('  Code B: print(5 + 3)')
answer = input("What does each print? ")
print('Answer: A prints "53" (string join). B prints 8 (arithmetic).')
score += 1
print()

# --- Round 2 ---
print("Round 2:")
print('  Code A: print("Hello", "World")')
print('  Code B: print("Hello" + "World")')
answer = input("What is different? ")
print("Answer: A prints 'Hello World' (comma adds space).")
print("         B prints 'HelloWorld' (+ joins with NO space).")
score += 1
print()

# --- Round 3 ---
print("Round 3:")
print('  Code A: print("*" * 5)')
print('  Code B: print("*5")')
answer = input("What does each print? ")
print('Answer: A prints "*****" (repetition). B prints "*5" (just text).')
score += 1
print()

# --- Round 4 ---
print("Round 4:")
print('  Code A: print(10 / 4)')
print('  Code B: print(10 // 4)')
answer = input("What does each print? ")
print("Answer: A prints", 10/4, "(float division). B prints", 10//4, "(floor division).")
score += 1
print()

# --- Round 5 ---
print("Round 5:")
print('  Code A: print("Line1\\nLine2")')
print('  Code B: print("Line1" + "\\n" + "Line2")')
answer = input("Any difference in output? (yes/no) ")
print("Answer: No! Both produce 2 lines: Line1 / Line2. \\n means newline in both.")
score += 1
print()

print("Score:", score, "/ 5")
print("Remember: quotes type, + vs comma, * for repetition, / vs // — all matter!")
