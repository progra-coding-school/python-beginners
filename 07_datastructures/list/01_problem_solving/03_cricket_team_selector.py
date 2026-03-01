# Program Code: LIST-PS-03
# Title: Cricket Team Selector
# Cognitive Skill: Problem Solving (Sorting, slicing, list manipulation)
# Topic: Lists in Python

# 15 available players, pick the top 11 based on scores
player_names  = ["Aarav", "Diya", "Kabir", "Meera", "Rohan",
                 "Riya",  "Dev",  "Kiran", "Priya", "Arjun",
                 "Sam",   "Arun", "Nisha", "Raj",   "Tara"]

player_scores = [85, 70, 90, 75, 88,
                 60, 92, 78, 82, 65,
                 95, 55, 80, 72, 68]

print("=== Cricket Team Selector ===")
print()

# Pair names with scores, sort highest first
paired = list(zip(player_scores, player_names))
paired.sort(reverse=True)

all_scores = [s for s, n in paired]
all_names  = [n for s, n in paired]

# Top 11 = Playing XI, rest = bench
playing_11 = all_names[:11]
bench      = all_names[11:]

print("PLAYING XI:")
for i in range(len(playing_11)):
    name = playing_11[i]
    score = all_scores[i]
    print("  " + str(i + 1).rjust(2) + ". " + name.ljust(10) + "  score: " + str(score))

print()
print("BENCH (reserve players):")
for i in range(len(bench)):
    name = bench[i]
    score = all_scores[11 + i]
    print("  " + str(i + 1) + ". " + name.ljust(10) + "  score: " + str(score))

print()
print("Team size:", len(playing_11))
print("Bench size:", len(bench))
