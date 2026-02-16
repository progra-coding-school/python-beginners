# Program Code: CS-FC-01
# Title: Eagle Eye - Spot the Difference!
# Cognitive Skill: Focus & Concentration (Visual attention to detail)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Programmers need EAGLE EYES! A tiny mistake - one wrong
# letter, one wrong number - can break an entire program.
# Can you spot TINY differences between two code blocks?
# Look VERY carefully. The difference is small!
# ============================================================

# ------------------------------------------------------------
# INSTRUCTIONS:
# 1. Two code blocks will be shown side by side
# 2. They look ALMOST identical - but ONE thing is different
# 3. Find the difference and type what changed
# 4. Be PRECISE - every character matters in programming!
# ------------------------------------------------------------

score = 0

print("=== Eagle Eye: Spot the Difference! ===")
print("Two code blocks. ONE tiny difference. Find it!")
print()

# ----- ROUND 1: Different number -----
print("--- Round 1 ---")
print()
print("  Code A:                    Code B:")
print("  name = 'Aarav'             name = 'Aarav'")
print("  age = 12                   age = 12")
print("  marks = 95                 marks = 85")
print()
answer = input("What is different? : ")
print("ANSWER: marks is 95 in Code A but 85 in Code B!")
print("A single digit changes the entire result!")
score = score + 1
print()

# ----- ROUND 2: Different variable name -----
print("--- Round 2 ---")
print()
print("  Code A:                    Code B:")
print("  price = 100                price = 100")
print("  quantity = 5               quantity = 5")
print("  total = price * quantity   total = prize * quantity")
print()
answer = input("What is different? : ")
print("ANSWER: Code A uses 'price' but Code B uses 'prize'!")
print("One wrong letter = a NameError crash!")
score = score + 1
print()

# ----- ROUND 3: Different operator -----
print("--- Round 3 ---")
print()
print("  Code A:                    Code B:")
print("  a = 10                     a = 10")
print("  b = 3                      b = 3")
print("  result = a + b             result = a - b")
print()
answer = input("What is different? : ")
print("ANSWER: Code A uses + (addition) but Code B uses - (subtraction)!")
print("Result changes from 13 to 7!")
score = score + 1
print()

# ----- ROUND 4: Extra space / quote style -----
print("--- Round 4 ---")
print()
print('  Code A:                    Code B:')
print('  city = "Chennai"           city = "Chennai "')
print('  print(city)                print(city)')
print()
answer = input("What is different? (Look very carefully!): ")
print('ANSWER: Code B has an extra SPACE inside the quotes: "Chennai "')
print("That invisible space can cause bugs in comparisons!")
score = score + 1
print()

# ----- ROUND 5: Wrong variable used -----
print("--- Round 5 ---")
print()
print("  Code A:                    Code B:")
print("  length = 10                length = 10")
print("  width = 5                  width = 5")
print("  area = length * width      area = length * length")
print()
answer = input("What is different? : ")
print("ANSWER: Code A correctly uses 'width' but Code B uses 'length' twice!")
print("Code B calculates a SQUARE area instead of a RECTANGLE area!")
score = score + 1
print()

# ----- ROUND 6: Different string value -----
print("--- Round 6 ---")
print()
print("  Code A:                    Code B:")
print('  greeting = "Vanakkam"      greeting = "Vanakam"')
print("  print(greeting)            print(greeting)")
print()
answer = input("What is different? (Count the letters!): ")
print('ANSWER: "Vanakkam" (double k) vs "Vanakam" (single k)!')
print("Spelling matters even inside strings!")
score = score + 1
print()

# ----- ROUND 7: Assignment vs comparison -----
print("--- Round 7 (Challenge!) ---")
print()
print("  Code A:                    Code B:")
print("  score = 100                score = 100")
print("  bonus = 10                 bonus = 10")
print("  score = score + bonus      score + bonus")
print("  print(score)               print(score)")
print()
answer = input("What is different? : ")
print("ANSWER: Code A has 'score = score + bonus' (STORES the result)")
print("Code B has just 'score + bonus' (calculates but does NOT store!)")
print("Code A prints 110, Code B still prints 100!")
score = score + 1
print()

# Final Score
print("=" * 40)
print(f"EAGLE EYE SCORE: {score} / 7")
if score == 7:
    print("Perfect vision! You caught every detail!")
elif score >= 5:
    print("Sharp eyes! Keep practicing!")
else:
    print("Keep training those eyes!")
print("=" * 40)

# ============================================================
# REFLECTION PROMPTS:
# 1. Which difference was hardest to spot? Why?
# 2. In real programming, bugs are often tiny mistakes
#    like these. How can you train yourself to notice them?
#    (Hint: Read code slowly, line by line, character by character)
# 3. Why do you think programmers use different colors for
#    different parts of code? (Syntax highlighting helps
#    your eyes catch mistakes faster!)
# ============================================================
