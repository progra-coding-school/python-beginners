# Program Code: SE-ST-03
# Title: Choose the Right Structure
# Cognitive Skill: Structured Thinking
# Topic: Sets in Python

# For each scenario, decide: list, set, or dict?
# Then see the correct choice and explanation.

print("=== Scenario Decision Guide ===")
print()

# --- Scenario 1: Cricket team scores ---
print("Scenario 1: Store scores for 11 players in batting order")
print("Need: order, duplicates allowed (two players can score the same)")
batting_scores = [45, 12, 62, 0, 33, 18, 7, 55, 3, 20, 10]
print("Best choice: LIST  →", batting_scores[:4], "... (ordered, allows 0 twice)")
print()

# --- Scenario 2: Student IDs for fast lookup ---
print("Scenario 2: Store 10,000 student IDs and check if one is valid")
print("Need: fast membership check, no duplicates")
valid_ids = {1001, 1002, 1003, 1004, 1005}   # set — instant lookup
print("Best choice: SET   → 1001 in valid_ids:", 1001 in valid_ids)
print()

# --- Scenario 3: Student profile ---
print("Scenario 3: Store name, age, grade, city for one student")
print("Need: label each field meaningfully")
student = {"name": "Aarav", "age": 13, "grade": 7, "city": "Chennai"}
print("Best choice: DICT  →", student)
print()

# --- Scenario 4: Tags on a blog post ---
print("Scenario 4: Tags like 'python', 'tutorial', 'beginner' on a post")
print("Need: unique tags only, fast membership, set operations")
tags = {"python", "tutorial", "beginner", "coding"}
print("Best choice: SET   →", tags)
print()

# --- Scenario 5: Weekly schedule ---
print("Scenario 5: Track which subjects are on which day")
print("Need: day → subject mapping, lookup by day")
schedule = {
    "Monday"   : "Maths",
    "Tuesday"  : "Science",
    "Wednesday": "English",
}
print("Best choice: DICT  →", schedule)
print()

# --- Scenario 6: Unique words in a paragraph ---
print("Scenario 6: Find all unique words in an essay")
essay  = "the quick brown fox jumps over the lazy dog the fox"
unique_words = set(essay.split())
print("Best choice: SET   →", sorted(unique_words))
print()

# --- Quick reference ---
print("=== Quick Reference ===")
print("  Ordered + duplicates allowed → LIST")
print("  Unique + fast lookup + math  → SET")
print("  Key-value pairs              → DICT")

# Think:
# 1. You're building a leaderboard showing top 10 scores. List or set? Why?
# 2. You need to store which students have completed each homework. What structure would you use?
