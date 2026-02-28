# Program Code: DC-PS-03
# Title: Word Frequency Counter
# Cognitive Skill: Problem Solving
# Topic: Dictionaries in Python

# Problem:
# Given a sentence, count how many times each word appears.
# This is how search engines, spell-checkers, and autocomplete work!

# --- Step 1: The sentence ---
sentence = "the cat sat on the mat and the cat sat again"

print("=== Word Frequency Counter ===")
print(f"Sentence: \"{sentence}\"")
print()

# --- Step 2: Split into words and count ---
words      = sentence.split()   # ["the", "cat", "sat", ...]
frequency  = {}                 # empty dict to fill

for word in words:
    if word in frequency:
        frequency[word] += 1    # seen before — add 1
    else:
        frequency[word] = 1     # first time — start at 1

print("Word counts:")
for word, count in frequency.items():
    bar = "█" * count           # visual bar
    print(f"  {word:10} {count}  {bar}")

print()

# --- Step 3: Most and least common word ---
most_common  = max(frequency, key=frequency.get)
least_common = min(frequency, key=frequency.get)

print(f"Most common word  : '{most_common}' ({frequency[most_common]} times)")
print(f"Least common word : '{least_common}' ({frequency[least_common]} time/s)")
print(f"Unique words      : {len(frequency)}")
print(f"Total words       : {len(words)}")

print()

# --- Step 4: Find all words that appear more than once ---
print("Words repeated more than once:")
repeated = {word: count for word, count in frequency.items() if count > 1}
if repeated:
    for word, count in repeated.items():
        print(f"  '{word}' appears {count} times")
else:
    print("  No repeated words.")

# Think:
# 1. What would you change so it ignores UPPERCASE vs lowercase (e.g., "The" == "the")?
# 2. How is this similar to an attendance register?
