# Program Code: SE-HOT-02
# Title: Design a Tag System
# Cognitive Skill: Higher Order Thinking
# Topic: Sets in Python

# Design challenge:
# Build a simple tag-based search system.
# Each article/video has a set of tags.
# Users can search for content that matches their interests.

# --- Content library ---
content = {
    "Intro to Python"      : {"python", "beginner", "coding", "tutorial"},
    "Cricket Tactics 101"  : {"cricket", "sports", "strategy", "beginner"},
    "Advanced Python OOP"  : {"python", "advanced", "coding", "oop"},
    "Healthy Eating"       : {"health", "food", "lifestyle"},
    "Python for Data"      : {"python", "data", "coding", "advanced"},
    "Chess Opening Moves"  : {"chess", "strategy", "beginner", "sports"},
}

print("=== Tag-Based Content Search ===")
print()

# --- Function: find content by a single tag ---
def search_by_tag(tag):
    results = [title for title, tags in content.items() if tag in tags]
    return results

# --- Function: find content matching ALL given tags ---
def search_all_tags(user_tags):
    user_set = set(user_tags)
    return [title for title, tags in content.items() if user_set.issubset(tags)]

# --- Function: find content matching ANY given tag ---
def search_any_tag(user_tags):
    user_set = set(user_tags)
    return [title for title, tags in content.items() if user_set & tags]

# --- Function: recommend content based on two users' interests ---
def recommend_common(tags_a, tags_b):
    common_interests = set(tags_a) & set(tags_b)
    return search_any_tag(common_interests), common_interests

# --- Demo ---
print("Search for tag 'python':")
for title in search_by_tag("python"):
    print(f"  → {title}")

print()

print("Search for content tagged BOTH 'python' AND 'beginner':")
for title in search_all_tags(["python", "beginner"]):
    print(f"  → {title}")

print()

print("Search for content tagged 'strategy' OR 'chess':")
for title in search_any_tag(["strategy", "chess"]):
    print(f"  → {title}")

print()

print("Recommend for Aarav ('python','coding') and Diya ('beginner','coding'):")
aarav_tags = {"python", "coding"}
diya_tags  = {"beginner", "coding"}
recommendations, common = recommend_common(aarav_tags, diya_tags)
print(f"  Shared interests: {common}")
for title in recommendations:
    print(f"  → {title}")

print()

# --- All unique tags in the library ---
all_tags = set()
for tags in content.values():
    all_tags |= tags
print("All unique tags in library:", sorted(all_tags))

# Think:
# 1. How would you add a "difficulty" tag filter on top of topic tags?
# 2. How does YouTube or Netflix use a similar tag/category system?
