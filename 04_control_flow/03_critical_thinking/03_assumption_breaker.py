# Program Code: CF-CT-03
# Title: Assumption Breaker — Control Flow
# Cognitive Skill: Critical Thinking (Challenging assumptions)
# Topic: Control Flow in Python

print("=== Assumption Breaker ===\n")

# Assumption 1: "else only works with if"
print("--- Assumption 1 ---")
print("Assume: else can only follow an if statement")
print("Actually: for and while loops can also have an else!")
print()
for i in range(3):
    print("Loop:", i)
else:
    print("Loop finished normally (else ran!)")
print()
print("The else on a loop runs ONLY if the loop was NOT exited by break.")
input("Press Enter to continue...")

# Assumption 2: "break exits the whole program"
print("\n--- Assumption 2 ---")
print("Assume: break exits the entire program")
print("Actually: break only exits the INNERMOST loop.")
for i in range(3):
    if i == 1:
        break
print("Code here still runs after break!")
input("Press Enter to continue...")

# Assumption 3: "if-elif checks ALL conditions"
print("\n--- Assumption 3 ---")
print("Assume: all elif conditions are checked even if an earlier one matches")
marks = 88
if marks >= 80:
    print("A — this ran")
elif marks >= 70:
    print("B — this ran too?")  # This will NOT run!
print("Actually: once one condition is True, Python skips ALL remaining elif/else.")
input("Press Enter to continue...")

# Assumption 4: "range(5) gives 1, 2, 3, 4, 5"
print("\n--- Assumption 4 ---")
print("Assume: range(5) gives 1 2 3 4 5")
print("Actually:")
for i in range(5):
    print(i, end=" ")
print()
print("range(5) gives 0,1,2,3,4 — it starts at 0 by default!")

# Think:
# 1. The 'else' on a for loop — when exactly does it NOT run?
# 2. You have a nested loop (loop inside a loop). What does break do inside the inner loop?
