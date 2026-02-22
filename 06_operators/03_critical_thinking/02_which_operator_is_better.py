# Program Code: OP-CT-02
# Title: Which Operator Approach Is Better?
# Cognitive Skill: Critical Thinking (Approach Evaluation)
# Topic: Operators in Python

# Same problem, two different operator choices.
# Analyze which is better and WHY.

# --- Scenario 1: Sharing chocolates ---
print("=== Scenario 1: Sharing 25 chocolates among 4 friends ===")
chocolates = 25
friends = 4

# Approach A: Regular division
approach_a = chocolates / friends
print("Approach A (/):", approach_a)    # 6.25

# Approach B: Floor division + modulo
each_gets = chocolates // friends
leftover = chocolates % friends
print(f"Approach B (// and %): {each_gets} each, {leftover} leftover")

print("Better approach: B — you can't give 0.25 of a chocolate!")
print()

# --- Scenario 2: Checking if a number is even ---
print("=== Scenario 2: Is 47 even or odd? ===")
number = 47

# Approach A: Using modulo
approach_a = number % 2 == 0
print("Approach A (% 2 == 0):", approach_a)   # False — correct!

# Approach B: Using division and comparison
approach_b = int(number / 2) * 2 == number
print("Approach B (int(n/2)*2 == n):", approach_b)  # False — works but awkward

print("Better approach: A — shorter, clearer, industry standard")
print()

# --- Scenario 3: Finding last digit ---
print("=== Scenario 3: Last digit of 4827 ===")
n = 4827

# Approach A: Convert to string and index
approach_a = int(str(n)[-1])
print("Approach A (string trick):", approach_a)   # 7

# Approach B: Modulo
approach_b = n % 10
print("Approach B (% 10):", approach_b)    # 7

print("Better approach: B for numbers — faster and avoids type conversion")
print()

# --- Scenario 4: Calculating percentage ---
print("=== Scenario 4: Marks percentage ===")
marks = 378
total = 500

# Approach A: Direct formula
percentage_a = marks / total * 100
print("Approach A (marks/total*100):", percentage_a)

# Approach B: Multiply first then divide
percentage_b = marks * 100 / total
print("Approach B (marks*100/total):", percentage_b)

print("Both give same result here, but Approach B avoids tiny float errors")
print("in some programming languages. In Python, both are fine.")
print()

# Think:
# 1. When would you choose // over /? Give 2 real examples.
# 2. When is % more useful than if-else to check something?
