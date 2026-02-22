# Program Code: LP-FC-01
# Title: Spot the Difference — Loops
# Cognitive Skill: Focus and Concentration (Attention to Detail)
# Topic: Loops in Python

# Each pair looks almost identical — but produces DIFFERENT output.
# Look very carefully at each character!

score = 0

print("=== Spot the Difference — Loops ===")
print()

# --- Round 1 ---
print("Round 1:")
print("  Code A: for i in range(5):")
print("  Code B: for i in range(1, 5):")
answer = input("What is different? ")
print(f"Answer: A gives 0,1,2,3,4 (5 values). B gives 1,2,3,4 (4 values).")
print(f"         range(5) starts at 0. range(1,5) starts at 1.")
score += 1
print()

# --- Round 2 ---
print("Round 2:")
print("  Code A: while count < 5:")
print("  Code B: while count <= 5:")
answer = input("What is different? ")
print("Answer: A stops BEFORE 5 (runs when count=0,1,2,3,4).")
print("         B includes 5 (runs when count=0,1,2,3,4,5).")
print("         One extra iteration — the <= makes a big difference!")
score += 1
print()

# --- Round 3 ---
print("Round 3:")
print("  Code A: for i in range(10, 0, -1): print(i)")
print("  Code B: for i in range(10, 0, -2): print(i)")
answer = input("What is different? ")
import io, sys
buf = io.StringIO()
sys.stdout = buf
for i in range(10, 0, -1): print(i, end=" ")
a_out = buf.getvalue()
buf = io.StringIO()
for i in range(10, 0, -2): print(i, end=" ")
b_out = buf.getvalue()
sys.stdout = sys.__stdout__
print(f"Answer: A counts down by 1: {a_out.strip()}")
print(f"         B counts down by 2: {b_out.strip()}")
score += 1
print()

# --- Round 4 ---
print("Round 4:")
print("  Code A:")
print("    for i in range(5):")
print("        if i == 3: break")
print("        print(i)")
print()
print("  Code B:")
print("    for i in range(5):")
print("        if i == 3: continue")
print("        print(i)")
answer = input("What does each print? ")
print("Answer: A prints 0 1 2 (stops at 3).")
print("         B prints 0 1 2 4 (skips 3, continues to 4).")
score += 1
print()

# --- Round 5 ---
print("Round 5:")
print("  Code A: total = 0")
print("           for n in [1,2,3,4]: total += n")
print()
print("  Code B: total = 1")
print("           for n in [1,2,3,4]: total += n")
answer = input("What is different? ")
total_a = 0
for n in [1,2,3,4]: total_a += n
total_b = 1
for n in [1,2,3,4]: total_b += n
print(f"Answer: A gives {total_a} (correct sum). B gives {total_b} (starts 1 too high).")
print("         Accumulator start value matters!")
score += 1
print()

# --- Round 6 ---
print("Round 6:")
print("  Code A: for i in range(3):")
print("               for j in range(3):")
print("                   print(i + j)")
print()
print("  Code B: for i in range(3):")
print("               for j in range(3):")
print("                   print(i * j)")
answer = input("At i=2, j=2: what does each print? ")
print(f"Answer: A prints {2+2} (2+2). B prints {2*2} (2×2).")
print("         Small operator difference — huge effect on pattern!")
score += 1
print()

print(f"Score: {score} / 6")
