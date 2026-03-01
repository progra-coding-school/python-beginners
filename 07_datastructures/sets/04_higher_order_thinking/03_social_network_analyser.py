# Mini Social Network Analyser
# Model a simple social network: each person has a set of friends.
# Use set operations to answer relationship questions — the same logic real social apps use.

# --- Friend graph ---
# Each person maps to a SET of their friends — set operations answer relationship questions
friends = {
    "Aarav"  : {"Diya", "Karthik", "Riya"},
    "Diya"   : {"Aarav", "Ananya", "Karthik"},
    "Karthik": {"Aarav", "Diya", "Vivek"},
    "Riya"   : {"Aarav", "Ananya"},
    "Ananya" : {"Diya", "Riya", "Vivek"},
    "Vivek"  : {"Karthik", "Ananya"},
}

print("Mini Social Network:")
for person, flist in friends.items():
    print("  " + person.ljust(10) + ":", sorted(flist))
print()

# --- Q1: Mutual friends between two people ---
# Intersection finds who appears in BOTH friend lists
def mutual_friends(a, b):
    return friends[a] & friends[b]

print("Mutual friends (Aarav & Diya)  :", mutual_friends("Aarav", "Diya"))
print("Mutual friends (Riya & Karthik):", mutual_friends("Riya", "Karthik"))
print()

# --- Q2: Friend suggestions (friends of friends, not already a friend) ---
# Collect all friends-of-friends; remove anyone already known (including self)
def friend_suggestions(person):
    my_friends     = friends[person]
    already_know   = my_friends | {person}   # friends + self — these should NOT be suggested
    suggestions    = set()
    for friend in my_friends:
        suggestions |= friends[friend]       # gather all their friends' friends
    return suggestions - already_know        # remove people already known

print("Friend suggestions for Aarav  :", friend_suggestions("Aarav"))
print("Friend suggestions for Vivek  :", friend_suggestions("Vivek"))
print()

# --- Q3: Most connected person ---
# max() with a key function to compare friend-set sizes
def most_connected():
    return max(friends, key=lambda p: len(friends[p]))

top = most_connected()
print("Most connected:", top, "with", len(friends[top]), "friends")
print()

# --- Q4: Who knows everyone in a group? ---
# issubset checks if the entire group is inside someone's friend set
def knows_all(group):
    group_set = set(group)
    return [
        person
        for person in friends
        if person not in group_set and group_set.issubset(friends[person])
    ]

group = ["Diya", "Karthik"]
print("Who knows both", group, ":", knows_all(group))
print()

# --- Q5: Are two people connected (direct or through one person)? ---
# Check direct first; then loop through mutual friends for second-hop connections
def connected_within_two(a, b):
    if b in friends[a]:
        return "Direct friends"
    for friend in friends[a]:
        if b in friends[friend]:
            return "Connected through " + friend
    return "Not connected within 2 steps"

print("Aarav & Vivek  :", connected_within_two("Aarav", "Vivek"))
print("Aarav & Ananya :", connected_within_two("Aarav", "Ananya"))

# Think:
# 1. How would you find the person who is a friend of EVERYONE in the network?
# 2. How does Instagram's "Suggested for you" feature likely work at a high level?
