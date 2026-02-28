# Program Code: SE-ST-02
# Title: Naming Matters
# Cognitive Skill: Structured Thinking
# Topic: Sets in Python

# Good names make set code readable without comments.
# Compare the same logic with poor vs good naming.

# ─── VERSION A: Poor naming ─────────────────────────────────────
print("=== Version A: Poor naming (confusing) ===")

s1 = {"a", "b", "c", "d"}
s2 = {"c", "d", "e", "f"}
s3 = s1 & s2
s4 = s1 - s2

print("s3:", s3)
print("s4:", s4)
# What does this code do? Hard to say without studying it.

print()

# ─── VERSION B: Good naming ─────────────────────────────────────
print("=== Version B: Good naming (self-explanatory) ===")

morning_batch  = {"Aarav", "Diya", "Karthik", "Riya"}
evening_batch  = {"Karthik", "Riya", "Ananya", "Vivek"}

both_batches   = morning_batch & evening_batch   # enrolled in both
morning_only   = morning_batch - evening_batch   # only morning students

print("Attend both batches :", both_batches)
print("Morning only        :", morning_only)
# Immediately clear what the code does!

print()

# ─── Naming conventions for sets ────────────────────────────────
print("=== Naming Guidelines for Sets ===")
guidelines = {
    "Use plural nouns"         : "students, colours, tags — not s or data",
    "Name describes contents"  : "submitted_ids, visited_urls",
    "Avoid single letters"     : "use 'allowed_users' not 'a'",
    "Use _set suffix if needed": "if ambiguous, add _set: ids_set",
    "Operation results named"  : "common_members, only_in_a, all_users",
}
for rule, example in guidelines.items():
    print(f"  {rule:<30} → {example}")

print()

# ─── Practice: rename these ─────────────────────────────────────
print("=== Practice: Better names ===")

# Poor:
x = {"red", "blue"}
y = {"blue", "green"}
z = x | y
# Better:
primary_colours   = {"red", "blue"}
cool_colours      = {"blue", "green"}
all_colours       = primary_colours | cool_colours
print("all_colours:", all_colours)

# Poor:
a = {"Aarav", "Diya"}
b = {"Diya", "Karthik"}
c = a & b
# Better:
class_a_students  = {"Aarav", "Diya"}
class_b_students  = {"Diya", "Karthik"}
shared_students   = class_a_students & class_b_students
print("shared_students:", shared_students)

# Think:
# 1. Look at a set program you wrote — are your variable names self-explanatory?
# 2. Why is naming especially important when sets use symbols like &, |, -, ^?
