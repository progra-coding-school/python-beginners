# Program Code: SE-HOT-03
# Title: Mini Social Network Analyser
# Cognitive Skill: Higher Order Thinking
# Topic: Sets in Python

# Design challenge:
# Model a simple social network where each person has a set of friends.
# Use set operations to answer relationship questions.

# --- Friend graph ---
friends = {
    "Aarav"  : {"Diya", "Karthik", "Riya"},
    "Diya"   : {"Aarav", "Ananya", "Karthik"},
    "Karthik": {"Aarav", "Diya", "Vivek"},
    "Riya"   : {"Aarav", "Ananya"},
    "Ananya" : {"Diya", "Riya", "Vivek"},
    "Vivek"  : {"Karthik", "Ananya"},
}

print("=== Mini Social Network ===")
for person, flist in friends.items():
    print(f"  {person:<10}: {sorted(flist)}")
print()

# --- Q1: Mutual friends between two people ---
def mutual_friends(a, b):
    return friends[a] & friends[b]

print("Mutual friends (Aarav & Diya)  :", mutual_friends("Aarav", "Diya"))
print("Mutual friends (Riya & Karthik):", mutual_friends("Riya", "Karthik"))
print()

# --- Q2: Friend suggestions (friends of friends, not already a friend) ---
def friend_suggestions(person):
    my_friends     = friends[person]
    already_know   = my_friends | {person}   # friends + self
    suggestions    = set()
    for friend in my_friends:
        suggestions |= friends[friend]       # collect all their friends
    return suggestions - already_know        # remove people already known

print("Friend suggestions for Aarav  :", friend_suggestions("Aarav"))
print("Friend suggestions for Vivek  :", friend_suggestions("Vivek"))
print()

# --- Q3: Most connected person ---
def most_connected():
    return max(friends, key=lambda p: len(friends[p]))

top = most_connected()
print(f"Most connected: {top} with {len(friends[top])} friends")
print()

# --- Q4: Who knows everyone in a group? ---
def knows_all(group):
    group_set = set(group)
    return [
        person
        for person in friends
        if person not in group_set and group_set.issubset(friends[person])
    ]

group = ["Diya", "Karthik"]
print(f"Who knows both {group}:", knows_all(group))
print()

# --- Q5: Are two people connected (direct or through one person)? ---
def connected_within_two(a, b):
    if b in friends[a]:
        return "Direct friends"
    for friend in friends[a]:
        if b in friends[friend]:
            return f"Connected through {friend}"
    return "Not connected within 2 steps"

print("Aarav & Vivek  :", connected_within_two("Aarav", "Vivek"))
print("Aarav & Ananya :", connected_within_two("Aarav", "Ananya"))

# Think:
# 1. How would you find the person who is a friend of EVERYONE in the network?
# 2. How does Instagram's "Suggested for you" feature likely work at a high level?
