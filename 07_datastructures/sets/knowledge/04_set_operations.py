# Set Operations — Union, Intersection, Difference, Symmetric Difference
# Sets support Venn-diagram operations directly in Python.
# Think of | as "either", & as "both", - as "only first", ^ as "only one".

cricket_fans  = {"Aarav", "Diya", "Karthik", "Riya"}
football_fans = {"Diya", "Ananya", "Riya", "Vivek"}

print("Cricket fans :", cricket_fans)
print("Football fans:", football_fans)
print()

# --- UNION — everyone from EITHER set (| or .union()) ---
# Like the full circle of a Venn diagram — all items from both sides
print("Union — all fans:")
all_fans = cricket_fans | football_fans
print("Union (|)       :", all_fans)
print("Union (.union()):", cricket_fans.union(football_fans))

print()

# --- INTERSECTION — only those in BOTH sets (& or .intersection()) ---
# Like the overlapping middle of a Venn diagram
print("Intersection — fans of both sports:")
both_fans = cricket_fans & football_fans
print("Intersection (&)        :", both_fans)
print("Intersection (.inter...):", cricket_fans.intersection(football_fans))

print()

# --- DIFFERENCE — in the first set but NOT in the second (- or .difference()) ---
# Order matters: a - b is NOT the same as b - a
print("Difference — cricket-only fans:")
cricket_only = cricket_fans - football_fans
print("Difference (-)         :", cricket_only)
print("Difference (.diff...)  :", cricket_fans.difference(football_fans))

football_only = football_fans - cricket_fans
print("Football only fans     :", football_only)

print()

# --- SYMMETRIC DIFFERENCE — in one set but NOT in both (^ or .symmetric_difference()) ---
# Like the outer parts of the Venn diagram — everyone who likes exactly ONE sport
print("Symmetric Difference — fans of only ONE sport:")
one_sport_only = cricket_fans ^ football_fans
print("Sym. diff (^)         :", one_sport_only)
print("Sym. diff (.sym_diff):", cricket_fans.symmetric_difference(football_fans))

print()

# --- Subset and Superset ---
# issubset → every item in a is also in b
# issuperset → a contains all items of b
# isdisjoint → no items in common at all
print("Subset / Superset:")
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(str(a) + " is subset of " + str(b) + "  :", a.issubset(b))      # True
print(str(b) + " is superset of " + str(a) + ":", b.issuperset(a))    # True
print("Disjoint? " + str(a) + " & " + str(b) + "  :", a.isdisjoint(b))  # False — share 1,2,3

# Think:
# 1. Which operation gives you the Venn diagram's middle section?
# 2. How would you find students who are in class A but NOT in class B?
