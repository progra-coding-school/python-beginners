# Cricket Team Selector
# 15 available players — sort by score, pick top 11, rest go to bench.
# KEY IDEA: zip() merges two lists into pairs so they stay linked during sorting.
# zip(scores, names) → [(85, "Aarav"), (70, "Diya"), ...]
# After sorting the pairs, we slice — [:11] = Playing XI, [11:] = bench.

player_names  = ["Aarav", "Diya", "Kabir", "Meera", "Rohan",
                 "Riya",  "Dev",  "Kiran", "Priya", "Arjun",
                 "Sam",   "Arun", "Nisha", "Raj",   "Tara"]

player_scores = [85, 70, 90, 75, 88,
                 60, 92, 78, 82, 65,
                 95, 55, 80, 72, 68]

# zip() pairs each score with its player name — they sort as one unit
# Without zip(), sorting scores would lose track of which name goes with which score
paired = list(zip(player_scores, player_names))
paired.sort(reverse=True)                # highest score moves to the front

# Unpack the sorted pairs back into two separate lists
all_scores = [s for s, n in paired]
all_names  = [n for s, n in paired]

# Slicing: [:11] takes the first 11 (top scorers), [11:] takes the rest
playing_11 = all_names[:11]   # top 11 by score = Playing XI
bench      = all_names[11:]   # remaining 4 = reserve bench

print("PLAYING XI:")
for i in range(len(playing_11)):
    name  = playing_11[i]
    score = all_scores[i]
    print("  " + str(i + 1).rjust(2) + ". " + name.ljust(10) + "  score: " + str(score))

print()
print("BENCH (reserve players):")
for i in range(len(bench)):
    name  = bench[i]
    score = all_scores[11 + i]         # bench players start at index 11 in all_scores
    print("  " + str(i + 1) + ". " + name.ljust(10) + "  score: " + str(score))

print()
print("Team size:", len(playing_11))
print("Bench size:", len(bench))
