# Program Code: CS-HO-03
# Title: Mini Story Generator (Mad Libs!)
# Cognitive Skill: Higher Order Thinking (Synthesis - combining variables creatively)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Can variables tell a STORY?
# You will enter some words and numbers,
# and the program will weave them into a funny story!
# This is called "Mad Libs" - a word game where YOUR inputs
# create unexpected, hilarious stories!
# ============================================================

print("=== Mini Story Generator ===")
print("Enter some words and watch a funny story appear!")
print()

# Collect story ingredients from the user
print("--- Give me some words! ---")
player_name = input("A cricket player's name: ")
opponent_team = input("An opponent team name: ")
runs_scored = input("A big number (runs scored): ")
lucky_food = input("Your favorite food: ")
celebration_move = input("A funny dance move (e.g., moonwalk, chicken dance): ")
crowd_size = input("A really big number (crowd size): ")
funny_animal = input("A funny animal: ")
color = input("Your favorite color: ")

# ===== STORY 1: The Cricket Match =====
print()
print("=" * 50)
print("THE GREATEST CRICKET MATCH EVER")
print("=" * 50)
print()
print(f"It was the final match. {player_name} walked onto the field")
print(f"to face the mighty {opponent_team}.")
print(f"The crowd of {crowd_size} people held their breath.")
print()
print(f"{player_name} looked at the bowler and smiled.")
print(f"WHACK! The ball flew like a {funny_animal} with wings!")
print(f"{player_name} scored {runs_scored} runs in one over!")
print()
print(f"The crowd went WILD! Everyone started doing the {celebration_move}!")
print(f"Even the umpire joined in!")
print()
print(f"After the match, {player_name} celebrated by eating")
print(f"100 plates of {lucky_food} while wearing a {color} cape.")
print(f"The {funny_animal} from the crowd became the team mascot.")
print()
print("THE END!")

input("\nPress Enter for Story 2...")

# ===== STORY 2: The School Day =====
print()
print("=" * 50)
print("THE CRAZIEST SCHOOL DAY")
print("=" * 50)
print()
print(f"One morning, {player_name} walked into school")
print(f"wearing a {color} uniform... made entirely of {lucky_food}!")
print()
print(f"The teacher said, 'Today we will learn from a {funny_animal}.'")
print(f"A real {funny_animal} walked into the classroom!")
print(f"It sat in the front row and scored {runs_scored} marks in the test!")
print()
print(f"At lunch, the canteen served {lucky_food} to all {crowd_size} students.")
print(f"Everyone was so happy they started doing the {celebration_move}!")
print(f"The principal announced: '{player_name} and the {funny_animal}")
print(f"are the Students of the Year!'")
print()
print("THE END!")
print()

# ===== YOUR TURN! =====
print("=" * 50)
print("NOW IT'S YOUR TURN!")
print("=" * 50)
print()
print("You just saw how variables create stories.")
print("The SAME variables made TWO different stories!")
print()
print("Challenge: Can you modify the story above to make")
print("a DIWALI or PONGAL celebration story?")
print()
print("Hint: Change the print() messages but keep the same variables!")
print("Example:")
print(f'  print(f"On Diwali night, {{{player_name}}} lit {{{runs_scored}}} diyas!")')
print(f'  print(f"A {{{funny_animal}}} burst {{{crowd_size}}} crackers!")')

# ============================================================
# REFLECTION PROMPTS:
# 1. The SAME 8 variables created TWO completely different stories.
#    How is that possible? What changed, and what stayed the same?
# 2. You are the CREATOR here. The variables are your building blocks.
#    How is this like building with LEGO? (Same blocks, different designs!)
# 3. Try this: Use the same variables to write a story about
#    a Pongal celebration, a birthday party, or a space adventure!
#    The variables are your ingredients - the story is YOUR recipe!
# ============================================================
