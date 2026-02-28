# Program Code: SE-KN-04
# Title: Set Operations — Union, Intersection, Difference
# Cognitive Skill: Knowledge
# Topic: Sets in Python

# Think of sets like Venn diagrams from Maths class!

cricket_fans  = {"Aarav", "Diya", "Karthik", "Riya"}
football_fans = {"Diya", "Ananya", "Riya", "Vivek"}

print("Cricket fans :", cricket_fans)
print("Football fans:", football_fans)
print()

# --- UNION — everyone from both sets (| or .union()) ---
print("=== Union — all fans ===")
all_fans = cricket_fans | football_fans
print("Union (|)       :", all_fans)
print("Union (.union()):", cricket_fans.union(football_fans))

print()

# --- INTERSECTION — only those in BOTH sets (& or .intersection()) ---
print("=== Intersection — fans of both sports ===")
both_fans = cricket_fans & football_fans
print("Intersection (&)        :", both_fans)
print("Intersection (.inter...):", cricket_fans.intersection(football_fans))

print()

# --- DIFFERENCE — in first but NOT in second (- or .difference()) ---
print("=== Difference — cricket only fans ===")
cricket_only = cricket_fans - football_fans
print("Difference (-)         :", cricket_only)
print("Difference (.diff...)  :", cricket_fans.difference(football_fans))

football_only = football_fans - cricket_fans
print("Football only fans     :", football_only)

print()

# --- SYMMETRIC DIFFERENCE — in one but NOT in both (^ or .symmetric_difference()) ---
print("=== Symmetric Difference — fans of only ONE sport ===")
one_sport_only = cricket_fans ^ football_fans
print("Sym. diff (^)         :", one_sport_only)
print("Sym. diff (.sym_diff):", cricket_fans.symmetric_difference(football_fans))

print()

# --- Subset and Superset ---
print("=== Subset / Superset ===")
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(f"{a} is subset of {b}  :", a.issubset(b))      # True
print(f"{b} is superset of {a}:", b.issuperset(a))     # True
print(f"Disjoint? {a} & {b}  :", a.isdisjoint(b))     # False (share 1,2,3)

# Think:
# 1. Which operation gives you the Venn diagram's middle section?
# 2. How would you find students who are in class A but NOT in class B?
