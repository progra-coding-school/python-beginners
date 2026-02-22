# Program Code: STR-FC-03
# Title: Memory Recall Challenge — Remember the Strings!
# Cognitive Skill: Focus and Concentration (Memory recall)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# A set of strings will be shown for a short time.
# Then they will disappear!
# You must RECALL what you saw — from memory.
# This trains working memory and concentration.
# ============================================================

import time

print("=" * 55)
print("  MEMORY RECALL CHALLENGE — STRINGS EDITION!")
print("=" * 55)

print("""
RULES:
  1. A list of strings will appear for 5 seconds
  2. They will disappear
  3. You must type them back from memory!
  4. Spelling and case both matter.
""")

score = 0

# -------------------------------------------------------
# ROUND 1: Short strings (easy)
# -------------------------------------------------------
print("=" * 40)
print("ROUND 1 — 3 strings, 5 seconds")
print("-" * 40)
print("Ready? Press ENTER to see the strings...")
input()

strings_r1 = ["Chennai", "Cricket", "Python"]
print()
for s in strings_r1:
    print(f"  >>> {s}")
print()
print("MEMORISE THEM! (5 seconds...)")
time.sleep(5)

# Clear with blank lines (simulate hiding)
print("\n" * 5)
print("=" * 40)
print("  NOW — TYPE WHAT YOU SAW!")
print("=" * 40)

for i, correct in enumerate(strings_r1, 1):
    answer = input(f"  String {i}: ")
    if answer.strip() == correct:
        print(f"    ✅ Correct!")
        score += 1
    else:
        print(f"    ❌ It was: '{correct}'")

# -------------------------------------------------------
# ROUND 2: Longer strings (medium)
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 2 — 4 strings, 6 seconds")
print("-" * 40)
print("Ready? Press ENTER to see the strings...")
input()

strings_r2 = ["Aarav Sharma", "Science Fair", "Grade 6", "Morning Batch"]
print()
for s in strings_r2:
    print(f"  >>> {s}")
print()
print("MEMORISE THEM! (6 seconds...)")
time.sleep(6)

print("\n" * 5)
print("=" * 40)
print("  NOW — TYPE WHAT YOU SAW!")
print("=" * 40)

for i, correct in enumerate(strings_r2, 1):
    answer = input(f"  String {i}: ")
    if answer.strip() == correct:
        print(f"    ✅ Correct!")
        score += 1
    else:
        print(f"    ❌ It was: '{correct}'")

# -------------------------------------------------------
# ROUND 3: Codes and numbers in strings (hard)
# -------------------------------------------------------
print("\n" + "=" * 40)
print("ROUND 3 — 3 strings with codes, 7 seconds")
print("-" * 40)
print("Ready? Press ENTER to see the strings...")
input()

strings_r3 = ["STU-AAR-2026", "Progra Thinkers Lab", "Chennai-TN-600001"]
print()
for s in strings_r3:
    print(f"  >>> {s}")
print()
print("MEMORISE THEM! (7 seconds...)")
time.sleep(7)

print("\n" * 5)
print("=" * 40)
print("  NOW — TYPE WHAT YOU SAW!")
print("=" * 40)

for i, correct in enumerate(strings_r3, 1):
    answer = input(f"  String {i}: ")
    if answer.strip() == correct:
        print(f"    ✅ Correct!")
        score += 1
    else:
        print(f"    ❌ It was: '{correct}'")

# -------------------------------------------------------
# FINAL SCORE
# -------------------------------------------------------
total = len(strings_r1) + len(strings_r2) + len(strings_r3)
print("\n" + "=" * 55)
print(f"  MEMORY RECALL SCORE : {score} / {total}")

if score == total:
    print("  🏆 Perfect Memory! You remembered everything!")
elif score >= 7:
    print("  ✅ Excellent recall — sharp memory!")
elif score >= 4:
    print("  👍 Good effort! Keep training your memory.")
else:
    print("  🧠 Memory is a muscle — keep exercising it!")

print("=" * 55)

print("""
MEMORY TIPS:
  → Group strings into categories mentally
  → Repeat them in your head silently
  → Look for patterns (e.g., STU-AAR-2026 = student code)
  → Visualise them in your mind
""")

# ============================================================
# REFLECTION:
# 1. Which round was hardest? Why?
# 2. What strategy helped you remember the strings?
# 3. How is this skill useful in real programming?
# ============================================================
