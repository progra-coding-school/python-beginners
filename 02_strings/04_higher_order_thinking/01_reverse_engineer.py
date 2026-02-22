# Program Code: STR-HOT-01
# Title: Reverse Engineer — Work Backwards from the Output!
# Cognitive Skill: Higher Order Thinking (Reverse engineering)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# You are given the FINAL OUTPUT of a string program.
# Your job is to figure out WHAT CODE produced it.
# This trains your mind to think from result → code!
# ============================================================

print("=" * 55)
print("  REVERSE ENGINEER — WHAT CODE MADE THIS OUTPUT?")
print("=" * 55)

print("""
Rules:
  You see the OUTPUT.
  You must WRITE or DESCRIBE the code that produced it.
  Then press ENTER to see the actual code used!
""")

score = 0
total = 4

# -------------------------------------------------------
# CHALLENGE 1
# -------------------------------------------------------
print("=" * 40)
print("CHALLENGE 1:")
print("-" * 40)
print("OUTPUT was:")
print()

# The actual output:
output_text = "AARAV"
print(f'  "{output_text}"')
print()
print("The original variable was: name = 'aarav sharma'")
print()
input("What code produced this? Press ENTER to see: ")

name   = "aarav sharma"
result = name.split()[0].upper()
print(f"""
  CODE: name.split()[0].upper()
  Step 1: name.split()    → ['aarav', 'sharma']
  Step 2: [0]             → 'aarav'
  Step 3: .upper()        → '{result}'
""")
guess = input("Did you figure it out? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# CHALLENGE 2
# -------------------------------------------------------
print("\n" + "=" * 40)
print("CHALLENGE 2:")
print("-" * 40)
print("OUTPUT was:")
print()
text = "I love Python and Python is great!"
result2 = text.replace("Python", "Cricket")
print(f'  "{result2}"')
print()
print('The original sentence was: "I love Python and Python is great!"')
print()
input("What code produced this? Press ENTER to see: ")
print(f"""
  CODE: text.replace("Python", "Cricket")
  replace() swaps EVERY occurrence of "Python" with "Cricket"
  Both "Python"s were replaced!
""")
guess = input("Did you figure it out? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# CHALLENGE 3
# -------------------------------------------------------
print("\n" + "=" * 40)
print("CHALLENGE 3:")
print("-" * 40)
print("OUTPUT was:")
print()
original = "NOHTYP"
result3  = original[::-1]
print(f'  "{result3}"')
print()
print(f'The original string was: "{original}"')
print()
input("What code produced this? Press ENTER to see: ")
print(f"""
  CODE: original[::-1]
  [::-1] reverses the string completely!
  "{original}" reversed → "{result3}"
""")
guess = input("Did you figure it out? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# CHALLENGE 4
# -------------------------------------------------------
print("\n" + "=" * 40)
print("CHALLENGE 4 (HARD!):")
print("-" * 40)
print("OUTPUT was:")
print()
raw    = "  hello world  "
result4 = raw.strip().title().replace("World", "India")
print(f'  "{result4}"')
print()
print(f'The original string was: "{raw}"')
print()
input("What code produced this? Press ENTER to see: ")
print(f"""
  CODE: raw.strip().title().replace("World", "India")
  Step 1: .strip()                  → 'hello world'
  Step 2: .title()                  → 'Hello World'
  Step 3: .replace("World","India") → '{result4}'

  This is called METHOD CHAINING — applying multiple
  methods one after another!
""")
guess = input("Did you figure it out? (y/n): ")
if guess.lower() == "y":
    score += 1

# -------------------------------------------------------
# FINAL SCORE
# -------------------------------------------------------
print("\n" + "=" * 55)
print(f"  REVERSE ENGINEER SCORE : {score} / {total}")
if score == total:
    print("  🏆 Master Reverse Engineer — Brilliant!")
elif score >= 2:
    print("  ✅ Good reverse thinking! Keep practising method chains.")
else:
    print("  💡 Reverse engineering is hard — keep experimenting!")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. What is method chaining? Can you create your own chain?
# 2. How did you figure out Challenge 4?
# 3. Write an output for a friend and challenge them!
# ============================================================
