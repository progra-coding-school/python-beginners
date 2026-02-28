# Program Code: SE-UN-04
# Title: Set Math — Venn Diagrams in Code
# Cognitive Skill: Understanding
# Topic: Sets in Python

# Everything you learned about Venn diagrams in Maths class
# works directly with Python sets!

print("=== Class Activity Signup ===")

art_club     = {"Aarav", "Diya", "Riya", "Ananya"}
science_club = {"Diya", "Karthik", "Riya", "Vivek"}
sports_club  = {"Aarav", "Karthik", "Vivek", "Riya"}

print("Art Club    :", art_club)
print("Science Club:", science_club)
print("Sports Club :", sports_club)
print()

# --- Who is in at least ONE club? (Union) ---
all_members = art_club | science_club | sports_club
print("In at least one club   :", all_members)

# --- Who is in ALL three clubs? (Intersection) ---
in_all_three = art_club & science_club & sports_club
print("In all three clubs     :", in_all_three)

# --- Who is ONLY in Art club? ---
only_art = art_club - science_club - sports_club
print("Only in Art Club       :", only_art)

# --- Who is in Art OR Science but NOT Sports? ---
art_or_science_not_sports = (art_club | science_club) - sports_club
print("Art/Science, not Sports:", art_or_science_not_sports)

# --- Are any two clubs completely separate? ---
print()
print("=== Are any clubs disjoint? ===")
print("Art & Science disjoint?:", art_club.isdisjoint(science_club))    # False — Diya, Riya
print("Art & Sports disjoint? :", art_club.isdisjoint(sports_club))     # False — Aarav, Riya

print()

# --- Real-world: Tags on videos ---
print("=== Tag System Example ===")
video1_tags = {"python", "beginner", "coding", "tutorial"}
video2_tags = {"coding", "advanced", "python", "projects"}

common_tags = video1_tags & video2_tags
print("Common tags     :", common_tags)

all_tags    = video1_tags | video2_tags
print("All unique tags  :", all_tags)

exclusive_v1 = video1_tags - video2_tags
print("Only in video 1  :", exclusive_v1)

print()
print("=== Set Math Summary ===")
print("  A | B  →  All items in A or B (union)")
print("  A & B  →  Only items in BOTH (intersection)")
print("  A - B  →  In A but NOT in B (difference)")
print("  A ^ B  →  In A or B but NOT both (symmetric difference)")

# Think:
# 1. How would you find students who joined the Science club AFTER quitting the Art club?
# 2. Name a real app that uses tag intersection (hint: think about Netflix or YouTube).
