# Reverse Engineer the Set
# Study the OUTPUT. Write the code that produced it. Then compare with the reference solution.
# Reverse engineering forces you to think about WHAT a set operation does, not just HOW to type it.

# --- Challenge 1 ---
# Output: {2, 4, 6, 8, 10}
# Clue: even numbers from 1 to 10
# Set comprehension — same idea as list comprehension but builds a set instead
print("Challenge 1:")
print("Target: {2, 4, 6, 8, 10}")
evens = {n for n in range(1, 11) if n % 2 == 0}
print("Result:", evens)

print()

# --- Challenge 2 ---
# Output: {'a', 'e', 'i', 'o', 'u'}
# Clue: unique vowels in the alphabet
# set() on a string gives one element per unique character
print("Challenge 2:")
print("Target: {'a', 'e', 'i', 'o', 'u'}")
vowels = set("aeiou")
print("Result:", vowels)

print()

# --- Challenge 3 ---
# Output:
#   Common  : {'Diya', 'Karthik'}
#   Only A  : {'Aarav'}
#   Only B  : {'Riya'}
# Clue: two groups of students — use intersection and difference
print("Challenge 3:")
print("Target:")
print("  Common  : {'Diya', 'Karthik'}")
print("  Only A  : {'Aarav'}")
print("  Only B  : {'Riya'}")
group_a = {"Aarav", "Diya", "Karthik"}
group_b = {"Diya", "Karthik", "Riya"}
print("Common  :", group_a & group_b)
print("Only A  :", group_a - group_b)
print("Only B  :", group_b - group_a)

print()

# --- Challenge 4 ---
# Output: 3
# Clue: list has duplicates; count unique words
# set() deduplicates; len() counts what remains
print("Challenge 4:")
print("Target: 3")
words = ["hello", "world", "hello", "python", "world"]
print("Result:", len(set(words)))

print()

# --- Challenge 5 (design challenge) ---
# Output:
#   Priya attended: {'Yoga', 'Art', 'Science'}
#   Excluded from 'Yoga' and 'Science' → Art only
# Clue: start with what she attended; subtract the excluded clubs
print("Challenge 5:")
all_clubs      = {"Art", "Science", "Yoga", "Music"}
priya_clubs    = {"Art", "Yoga", "Science"}
excluded_clubs = {"Yoga", "Science"}
remaining      = priya_clubs - excluded_clubs

print("Priya attended:", priya_clubs)
print("Excluded:", excluded_clubs, "→", remaining)

# Think:
# 1. In Challenge 1, what is the construct {n for n in ...} called?
# 2. How would you modify Challenge 4 to also count how many times each word appears?
