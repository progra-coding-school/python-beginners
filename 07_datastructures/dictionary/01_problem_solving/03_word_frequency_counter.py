# Word Frequency Counter
# Given a sentence, count how many times each word appears.
# KEY IDEA: word is the KEY, count is the VALUE.
# Pattern: for each word, if already in dict → add 1; else → start at 1.
# This exact pattern powers search engines, spell-checkers, and autocomplete!

# Step 1: The sentence to analyse
sentence = "the cat sat on the mat and the cat sat again"

print("Word Frequency Counter")
print('Sentence: "' + sentence + '"')
print()

# Step 2: Split sentence into words and count each one
# .split() breaks on spaces → returns a list of words
words     = sentence.split()   # ["the", "cat", "sat", ...]
frequency = {}                 # empty dict to build up

for word in words:
    if word in frequency:
        frequency[word] += 1    # word seen before — increment the count
    else:
        frequency[word] = 1     # first time seeing this word — start at 1

print("Word counts:")
for word, count in frequency.items():
    bar = "+" * count           # visual bar: one + per occurrence
    print("  " + word.ljust(10) + str(count) + "  " + bar)

print()

# Step 3: Most and least common word
# max(dict, key=dict.get) → finds the key (word) with the highest value (count)
most_common  = max(frequency, key=frequency.get)
least_common = min(frequency, key=frequency.get)

print("Most common word  : '" + most_common + "' (" + str(frequency[most_common]) + " times)")
print("Least common word : '" + least_common + "' (" + str(frequency[least_common]) + " time/s)")
print("Unique words      :", len(frequency))
print("Total words       :", len(words))

print()

# Step 4: Find repeated words — words that appear more than once
# Dictionary comprehension: build a new dict keeping only entries where count > 1
print("Words repeated more than once:")
repeated = {word: count for word, count in frequency.items() if count > 1}
if repeated:
    for word, count in repeated.items():
        print("  '" + word + "' appears " + str(count) + " times")
else:
    print("  No repeated words.")
