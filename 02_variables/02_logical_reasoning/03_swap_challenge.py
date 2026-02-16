# Program Code: CS-LR-03
# Title: The Great Swap Challenge
# Cognitive Skill: Logical Reasoning (Sequential reasoning about state)
# Topic: Variables in Python

# ============================================================
# PROBLEM STATEMENT:
# Amma made laddoos for Aarav and jalebis for Diya.
# But they want to SWAP! Aarav wants jalebis and Diya wants laddoos.
# Sounds simple? But in programming, swapping is a PUZZLE!
# If you pour Aarav's laddoos into Diya's box, what happens
# to Diya's jalebis? They get lost!
# You need a THIRD box (a temporary variable)!
# ============================================================

print("=== The Great Swap Challenge ===")
print()

# ===== LEVEL 1: Simple Swap with a Temp Variable =====
print("--- Level 1: Swap Two Boxes ---")
print()
print("Aarav has LADDOOS, Diya has JALEBIS.")
print("They want to swap. Let us use a temporary box!")
print()

aarav_box = "Laddoos"
diya_box = "Jalebis"

print(f"BEFORE swap:")
print(f"  Aarav's box: {aarav_box}")
print(f"  Diya's box:  {diya_box}")
print()

# The swap - step by step with reasoning
# Step 1: Put Aarav's items in a temporary box
temp_box = aarav_box        # temp_box = "Laddoos"
print(f"Step 1: Put Aarav's {aarav_box} in temp box")

# Step 2: Now Aarav's box is free, put Diya's items there
aarav_box = diya_box        # aarav_box = "Jalebis"
print(f"Step 2: Give Aarav Diya's {diya_box}")

# Step 3: Put temp box items into Diya's box
diya_box = temp_box         # diya_box = "Laddoos"
print(f"Step 3: Give Diya the {temp_box} from temp box")

print()
print(f"AFTER swap:")
print(f"  Aarav's box: {aarav_box}")
print(f"  Diya's box:  {diya_box}")

input("\nPress Enter to continue to Level 2...")
print()

# ===== LEVEL 2: Swap Numbers =====
print("--- Level 2: Swap Two Numbers ---")
print()

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

print(f"\nBEFORE swap: a = {a}, b = {b}")

# Swap using temp
temp = a
a = b
b = temp

print(f"AFTER swap:  a = {a}, b = {b}")

input("\nPress Enter to continue to Level 3...")
print()

# ===== LEVEL 3: The THREE-WAY Circular Swap! =====
print("--- Level 3: Three-Way Circular Swap! ---")
print()
print("Aarav has Laddoos, Diya has Jalebis, Priya has Mysore Pak")
print("They want to rotate: Aarav gets Diya's, Diya gets Priya's,")
print("Priya gets Aarav's!")
print()

aarav = "Laddoos"
diya = "Jalebis"
priya = "Mysore Pak"

print(f"BEFORE: Aarav={aarav}, Diya={diya}, Priya={priya}")

# Think step by step!
# Save Aarav's before it gets overwritten
temp = aarav          # temp = "Laddoos"
aarav = diya          # aarav = "Jalebis"
diya = priya          # diya = "Mysore Pak"
priya = temp          # priya = "Laddoos"

print(f"AFTER:  Aarav={aarav}, Diya={diya}, Priya={priya}")

input("\nPress Enter to continue to the BONUS Level...")
print()

# ===== BONUS: Swap WITHOUT a temp variable! =====
print("--- BONUS: Swap Numbers Without a Temp Variable! ---")
print("(This is a MAGIC trick using math!)")
print()

a = 15
b = 27

print(f"BEFORE: a = {a}, b = {b}")
print()

# The math trick:
print(f"Step 1: a = a + b = {a} + {b} = {a + b}")
a = a + b       # a = 42
print(f"         Now a = {a}, b = {b}")

print(f"Step 2: b = a - b = {a} - {b} = {a - b}")
b = a - b       # b = 15 (the original a!)
print(f"         Now a = {a}, b = {b}")

print(f"Step 3: a = a - b = {a} - {b} = {a - b}")
a = a - b       # a = 27 (the original b!)
print(f"         Now a = {a}, b = {b}")

print()
print(f"AFTER:  a = {a}, b = {b}")
print("The swap worked without any temp variable!")

# ============================================================
# REFLECTION PROMPTS:
# 1. In Level 1, what would happen if we did NOT use a temp box?
#    What would get LOST? Try removing Step 1 and see!
# 2. In the Three-Way Swap, why did we save Aarav's value FIRST?
#    What if we started by saving Diya's instead?
# 3. The BONUS trick uses math (addition and subtraction).
#    Can you trace through it with a = 10, b = 7 on paper?
#    Does the order of steps matter?
# ============================================================
