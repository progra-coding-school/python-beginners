# Program Code: SE-FC-03
# Title: Memory Recall Challenge
# Cognitive Skill: Focus and Concentration
# Topic: Sets in Python

# Study the sets below for 30 seconds.
# Then scroll down and answer questions FROM MEMORY.
# Run to verify!

# ─── Memorise these sets ─────────────────────────────────────────
class_red   = {"Aarav", "Diya", "Karthik", "Riya", "Ananya"}
class_blue  = {"Diya", "Vivek", "Karthik", "Priya"}
class_green = {"Riya", "Ananya", "Priya", "Arjun"}

print("=== Sets to Memorise (30 seconds) ===")
print(f"Red   class : {sorted(class_red)}")
print(f"Blue  class : {sorted(class_blue)}")
print(f"Green class : {sorted(class_green)}")

print()
print("─" * 50)
print("Answer questions below WITHOUT looking up ↑")
print("─" * 50)
print()

# --- Q1: How many students in Red class? ---
print(f"Q1: Size of Red class  = {len(class_red)}")

# --- Q2: Who is in both Red and Blue? ---
red_and_blue = class_red & class_blue
print(f"Q2: Red ∩ Blue         = {sorted(red_and_blue)}")

# --- Q3: Who is in Blue but NOT in Green? ---
blue_not_green = class_blue - class_green
print(f"Q3: Blue − Green       = {sorted(blue_not_green)}")

# --- Q4: How many unique students across all three? ---
all_students = class_red | class_blue | class_green
print(f"Q4: Total unique       = {len(all_students)}")

# --- Q5: Is Arjun in Red class? ---
print(f"Q5: 'Arjun' in Red?   = {'Arjun' in class_red}")

# --- Q6: Who appears in ALL three classes? ---
all_three = class_red & class_blue & class_green
print(f"Q6: In all 3 classes  = {sorted(all_three)}")

# --- Q7: Who is ONLY in Green class? ---
only_green = class_green - class_red - class_blue
print(f"Q7: Only in Green     = {sorted(only_green)}")

print()
print("─" * 50)
print("Score yourself:")
print("  7/7 correct → Exceptional focus!")
print("  5-6 correct → Great — minor lapses.")
print("  3-4 correct → Good — try once more with a 45-second study.")
print("  0-2 correct → Use a technique: group, visualise, or draw a Venn diagram.")

# Think:
# 1. Which question was hardest to answer from memory? Why?
# 2. How does drawing a Venn diagram help you memorise set relationships?
