# Program Code: SE-PS-02
# Title: Common and Unique Interests
# Cognitive Skill: Problem Solving
# Topic: Sets in Python

# Problem:
# Two students fill in their hobby lists.
# Find: what they have in common, what is unique to each,
# and suggest a club they could both join.

# --- Data ---
aarav_hobbies  = {"cricket", "coding", "reading", "chess", "music"}
diya_hobbies   = {"music", "dancing", "reading", "painting", "coding"}

print("Aarav's hobbies:", aarav_hobbies)
print("Diya's hobbies :", diya_hobbies)
print()

# --- Step 1: Common hobbies ---
common = aarav_hobbies & diya_hobbies
print("=== What they share ===")
if common:
    print("Common hobbies:", common)
    print("They can bond over:", sorted(common))
else:
    print("No common hobbies — they can still learn from each other!")

print()

# --- Step 2: Unique to each ---
only_aarav = aarav_hobbies - diya_hobbies
only_diya  = diya_hobbies  - aarav_hobbies

print("=== Unique hobbies ===")
print("Only Aarav :", only_aarav)
print("Only Diya  :", only_diya)

print()

# --- Step 3: All hobbies combined ---
all_hobbies = aarav_hobbies | diya_hobbies
print("=== All unique hobbies together ===")
print("All hobbies:", sorted(all_hobbies))
print(f"({len(aarav_hobbies)} + {len(diya_hobbies)} hobbies → {len(all_hobbies)} unique)")

print()

# --- Step 4: Club suggestion ---
print("=== Club Suggestion ===")
clubs = {
    "Music Club"    : {"music", "singing", "instruments"},
    "Tech Club"     : {"coding", "robotics", "chess"},
    "Sports Club"   : {"cricket", "football", "swimming"},
    "Arts Club"     : {"painting", "dancing", "drawing"},
    "Reading Club"  : {"reading", "writing", "storytelling"},
}

print("Clubs both Aarav and Diya would enjoy:")
for club, activities in clubs.items():
    if common & activities:     # any common hobby matches this club's activities
        print(f"  → {club}")

# Think:
# 1. What if a third friend Karthik also has hobbies? How would you find hobbies all THREE share?
# 2. How would a friendship app use this idea to suggest connections?
