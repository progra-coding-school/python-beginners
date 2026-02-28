# Program Code: STR-HOT-03
# Title: Mad Libs Story Generator — Create a Funny Story with Strings!
# Cognitive Skill: Higher Order Thinking (Creative synthesis)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Mad Libs is a game where you fill in the blanks of a story
# with random words — and it creates hilarious results!
# Aarav wants to build a Mad Libs generator using strings.
# You will collect words from the user and BUILD the story!
# ============================================================

print("=" * 55)
print("    MAD LIBS STORY GENERATOR — PROGRA EDITION!")
print("=" * 55)

print("""
Welcome to Progra Mad Libs!
You'll give me some words — I'll make a funny story.
DON'T read the story first. Just answer the questions!
""")

# -------------------------------------------------------
# STEP 1: Collect words (user doesn't know the story yet!)
# -------------------------------------------------------
print("-" * 50)
print("STEP 1: Give me some words (no peeking at the story!)")
print("-" * 50)

name1        = input("Enter a student's name        : ").strip().title()
animal       = input("Enter an animal               : ").strip().lower()
subject      = input("Enter a school subject        : ").strip().title()
verb_ing     = input("Enter an action word (-ing)   : ").strip().lower()
food         = input("Enter your favourite food     : ").strip().title()
place        = input("Enter a place in your city    : ").strip().title()
number       = input("Enter a number (1-100)        : ").strip()
adjective    = input("Enter a describing word       : ").strip().lower()
teacher_name = input("Enter a funny teacher name    : ").strip().title()

# -------------------------------------------------------
# STEP 2: Build the story using string concatenation
# -------------------------------------------------------
print("\n" + "=" * 55)
print("         HERE IS YOUR MAD LIBS STORY!")
print("=" * 55)

story = (
    "\nOne day, " + name1 + " was quietly sitting in " + subject + " class\n"
    + "when suddenly a " + adjective + " " + animal + " walked through the door!\n"
    + "\nEveryone in the class started " + verb_ing + " loudly.\n"
    + "Teacher " + teacher_name + " looked up from the board and said,\n"
    + '"Why is there a ' + animal + ' in my class?!"\n'
    + "\n" + name1 + " calmly walked up, gave the " + animal + " some " + food + ",\n"
    + 'and said, "Don\'t worry sir, it followed me from ' + place + '."\n'
    + "\nThe whole class burst into laughter. The " + animal + " sat down\n"
    + "and attended " + subject + " for the next " + number + " minutes —\n"
    + "and got full marks!\n"
    + "\nTHE END 😄\n"
)

print(story)

# -------------------------------------------------------
# STEP 3: Count some stats about the story
# -------------------------------------------------------
print("-" * 55)
print("STORY STATS:")
print("  Characters in story :", len(story))
print("  Your name appeared  :", story.count(name1), "times")
print("  Animal appeared     :", story.count(animal), "times")
print("-" * 55)

# -------------------------------------------------------
# BONUS: Let them play again with different words
# -------------------------------------------------------
print("\nWant to create another story? Run the program again!")
print("Try different words for a completely different story!")

# ============================================================
# REFLECTION:
# 1. How does concatenation (+) help in building the story?
# 2. How did count() help you find how many times a word appeared?
# 3. Can you write your OWN story template with 5+ blanks?
# 4. What would happen if name1 = "aarav" without .title()?
# ============================================================
