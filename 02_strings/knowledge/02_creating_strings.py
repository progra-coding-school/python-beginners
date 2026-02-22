# Program Code: STR-KN-02
# Title: Creating Strings — Three Ways to Write Text!
# Cognitive Skill: Knowledge (Acquiring the concept)
# Topic: Strings in Python

# ============================================================
# PROBLEM STATEMENT:
# Diya is writing a Python diary program. She wants to store:
#   1. A short word
#   2. A sentence with apostrophe (like "don't")
#   3. A multi-line poem
# One type of quote won't always work — let's learn ALL THREE!
# ============================================================

print("=" * 55)
print("     THREE WAYS TO CREATE STRINGS IN PYTHON")
print("=" * 55)

# -------------------------------------------------------
# WAY 1: Single Quotes  '...'
# Best for: short words and simple sentences
# -------------------------------------------------------
print("\n--- WAY 1: Single Quotes ---")

city       = 'Chennai'
fruit      = 'Mango'
greeting   = 'Vanakkam!'

print(f"City     : {city}")
print(f"Fruit    : {fruit}")
print(f"Greeting : {greeting}")

# -------------------------------------------------------
# WAY 2: Double Quotes  "..."
# Best for: sentences that contain an apostrophe (')
# -------------------------------------------------------
print("\n--- WAY 2: Double Quotes ---")

sentence    = "I don't want to stop coding!"
player_bio  = "Virat's batting is amazing."
school_rule = "Today's homework is due tomorrow."

print(f"Sentence    : {sentence}")
print(f"Player bio  : {player_bio}")
print(f"School rule : {school_rule}")

# -------------------------------------------------------
# WHY DOUBLE QUOTES? — The Apostrophe Problem
# -------------------------------------------------------
# ❌ WRONG: 'I don't want to stop!'  → Python gets confused!
# ✅ RIGHT: "I don't want to stop!"  → Works perfectly!

# -------------------------------------------------------
# WAY 3: Triple Quotes  """..."""  or  '''...'''
# Best for: multi-line text (poems, paragraphs, diary entries)
# -------------------------------------------------------
print("\n--- WAY 3: Triple Quotes (Multi-line) ---")

diya_poem = """
Roses are red,
Violets are blue,
Python is fun,
And I love coding too!
"""

cricket_rules = '''
Rule 1: Bat first or field.
Rule 2: 6 balls in an over.
Rule 3: Highest score wins!
'''

print("Diya's Poem:")
print(diya_poem)

print("Cricket Rules:")
print(cricket_rules)

# -------------------------------------------------------
# SUMMARY TABLE
# -------------------------------------------------------
print("=" * 55)
print("  SUMMARY: Which quote to use when?")
print("=" * 55)
print("  Single Quotes  ' '  → Short words, simple text")
print("  Double Quotes  \" \" → Text with apostrophes")
print("  Triple Quotes  \"\"\" → Multi-line text, paragraphs")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. What happens if you use single quotes for "I don't know"?
# 2. Can you write a 3-line poem using triple quotes?
# 3. Are 'hello' and "hello" the same? (Hint: Yes! Try it!)
# ============================================================
