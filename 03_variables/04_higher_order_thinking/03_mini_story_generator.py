# Program Code: VAR-HOT-03
# Title: Mini Story Generator
# Cognitive Skill: Higher Order Thinking (Synthesis)
# Topic: Variables in Python

# Enter some words — the program turns them into a story!

player_name = input("A cricket player's name: ")
opponent_team = input("An opponent team name: ")
runs_scored = input("A big number (runs): ")
lucky_food = input("Your favourite food: ")
celebration_move = input("A funny dance move: ")
crowd_size = input("A big crowd number: ")
funny_animal = input("A funny animal: ")
color = input("Your favourite colour: ")

# Story 1
print("--- The Greatest Cricket Match ---")
print("It was the final match.", player_name, "walked onto the field")
print("to face the mighty", opponent_team)
print("The crowd of", crowd_size, "people held their breath.")
print(player_name, "scored", runs_scored, "runs in one over!")
print("The crowd started doing the", celebration_move)
print("After the match,", player_name, "ate 100 plates of", lucky_food)
print("wearing a", color, "cape. THE END!")

input("Press Enter for Story 2...")

# Story 2 — same variables, completely different story!
print("--- The Craziest School Day ---")
print("One morning,", player_name, "walked into school")
print("wearing a", color, "uniform made entirely of", lucky_food)
print("A real", funny_animal, "sat in the front row")
print("and scored", runs_scored, "marks in the test!")
print("All", crowd_size, "students started doing the", celebration_move)
print(player_name, "and the", funny_animal, "won Student of the Year! THE END!")

# Notice: the SAME 8 variables created TWO different stories.
# Think:
# 1. What changed between the two stories? What stayed the same?
# 2. Try writing a Pongal story using the same variables!
