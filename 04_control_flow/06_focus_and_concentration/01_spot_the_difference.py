# Program Code: CF-FC-01
# Title: Spot the Difference — Control Flow
# Cognitive Skill: Focus and Concentration (Attention to detail)
# Topic: Control Flow in Python

score = 0

# Round 1
print("--- Round 1 ---")
print("  Code A: if marks == 90:")
print("  Code B: if marks = 90:")
answer = input("What is different? ")
print("Answer: A uses == (comparison). B uses = (assignment — a syntax error)!")
score += 1

# Round 2
print("--- Round 2 ---")
print("  Code A: for i in range(5):")
print("  Code B: for i in range(1, 5):")
answer = input("What is different? ")
print("Answer: A gives 0,1,2,3,4 (5 values). B gives 1,2,3,4 (4 values).")
score += 1

# Round 3
print("--- Round 3 ---")
print("  Code A: if score >= 35:")
print("               print('Pass')")
print("           elif score >= 35:")
print("               print('Eligible')")
print("")
print("  Code B: if score >= 35:")
print("               print('Pass')")
print("           if score >= 35:")
print("               print('Eligible')")
answer = input("What is different? ")
print("Answer: A uses elif (only one runs). B uses two ifs (BOTH run if score >= 35)!")
score += 1

# Round 4
print("--- Round 4 ---")
print("  Code A: while count < 10:")
print("               count += 1")
print("  Code B: while count < 10:")
print("               count -= 1")
answer = input("What is different? ")
print("Answer: A increments (eventually stops). B decrements (infinite loop if count > 0)!")
score += 1

# Round 5
print("--- Round 5 ---")
print("  Code A: for i in range(10):")
print("               if i == 5: break")
print("               print(i)")
print("")
print("  Code B: for i in range(10):")
print("               if i == 5: continue")
print("               print(i)")
answer = input("What is different? ")
print("Answer: A stops at 5 (prints 0-4). B skips 5 (prints 0-4 and 6-9).")
score += 1

# Round 6
print("--- Round 6 ---")
print("  Code A: if x > 5 and y > 5:")
print("  Code B: if x > 5 or y > 5:")
answer = input("What is different? (Try x=3, y=8) ")
print("Answer: A: 3>5=False. False AND anything = False → skipped.")
print("         B: 3>5=False OR 8>5=True → True → runs!")
score += 1

print(f"\nScore: {score} / 6")
