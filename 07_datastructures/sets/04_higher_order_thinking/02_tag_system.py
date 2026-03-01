# Design a Tag System
# Each article/video has a set of tags. Users search for content by tags.
# Set operations power the search: issubset for ALL-match, intersection for ANY-match.

# --- Content library ---
# Each title maps to a set of tags — searching by tag is a set operation
content = {
    "Intro to Python"      : {"python", "beginner", "coding", "tutorial"},
    "Cricket Tactics 101"  : {"cricket", "sports", "strategy", "beginner"},
    "Advanced Python OOP"  : {"python", "advanced", "coding", "oop"},
    "Healthy Eating"       : {"health", "food", "lifestyle"},
    "Python for Data"      : {"python", "data", "coding", "advanced"},
    "Chess Opening Moves"  : {"chess", "strategy", "beginner", "sports"},
}

print("Tag-Based Content Search:")
print()

# --- Function: find content by a single tag ---
# Loop and check if the tag is in each title's tag set
def search_by_tag(tag):
    results = [title for title, tags in content.items() if tag in tags]
    return results

# --- Function: find content matching ALL given tags ---
# issubset → every tag the user asked for must be in the title's tags
def search_all_tags(user_tags):
    user_set = set(user_tags)
    return [title for title, tags in content.items() if user_set.issubset(tags)]

# --- Function: find content matching ANY given tag ---
# intersection → at least one of the user's tags overlaps with the title's tags
def search_any_tag(user_tags):
    user_set = set(user_tags)
    return [title for title, tags in content.items() if user_set & tags]

# --- Function: recommend content based on two users' shared interests ---
# Find their common tags first, then search for content matching any of those
def recommend_common(tags_a, tags_b):
    common_interests = set(tags_a) & set(tags_b)
    return search_any_tag(common_interests), common_interests

# --- Demo ---
print("Search for tag 'python':")
for title in search_by_tag("python"):
    print("  →", title)

print()

print("Search for content tagged BOTH 'python' AND 'beginner':")
for title in search_all_tags(["python", "beginner"]):
    print("  →", title)

print()

print("Search for content tagged 'strategy' OR 'chess':")
for title in search_any_tag(["strategy", "chess"]):
    print("  →", title)

print()

print("Recommend for Aarav ('python','coding') and Diya ('beginner','coding'):")
aarav_tags = {"python", "coding"}
diya_tags  = {"beginner", "coding"}
recommendations, common = recommend_common(aarav_tags, diya_tags)
print("  Shared interests:", common)
for title in recommendations:
    print("  →", title)

print()

# --- All unique tags in the library ---
# |= is the update-in-place union — collect all tags from every title
all_tags = set()
for tags in content.values():
    all_tags |= tags
print("All unique tags in library:", sorted(all_tags))

# Think:
# 1. How would you add a "difficulty" tag filter on top of topic tags?
# 2. How does YouTube or Netflix use a similar tag/category system?
