# Add and Remove Items in a Set
# Six methods for modifying a set: add, update, remove, discard, pop, clear.
# Key rule: discard() is safe (silent if missing); remove() raises KeyError.

hobbies = {"reading", "cricket", "drawing"}
print("Original:", hobbies)
print()

# --- ADD items ---

# .add() — adds ONE item; if already present, it is silently ignored (no duplicate, no error)
hobbies.add("coding")
hobbies.add("cricket")     # already there — no duplicate, no error
print("After add('coding')  :", hobbies)

# .update() — adds MULTIPLE items at once from a list, tuple, or another set
hobbies.update(["swimming", "chess"])
print("After update(...)    :", hobbies)

print()

# --- REMOVE items ---

# .remove() — removes the item; raises KeyError if NOT found (risky if item might be missing)
hobbies.remove("drawing")
print("After remove('drawing'):", hobbies)

try:
    hobbies.remove("painting")   # not in set — ERROR
except KeyError as e:
    print("KeyError with remove():", e)

print()

# .discard() — removes if present; SILENTLY ignores if NOT found (safe choice!)
# Use discard() when you are not sure if the item exists
hobbies.discard("chess")
print("After discard('chess') :", hobbies)

hobbies.discard("yoga")    # not in set — no error, no crash
print("After discard('yoga')  :", hobbies)

print()

# .pop() — removes and returns a RANDOM item (sets are unordered, so you can't predict which)
removed = hobbies.pop()
print("pop() removed:", removed)
print("After pop()  :", hobbies)

print()

# .clear() — removes ALL items, leaving an empty set
temp = {"a", "b", "c"}
temp.clear()
print("After clear():", temp)   # set()

print()

# --- Summary ---
print("Add/Remove Summary:")
print("  .add(item)       → add one item (safe if already exists)")
print("  .update(items)   → add multiple items")
print("  .remove(item)    → remove; KeyError if missing")
print("  .discard(item)   → remove; silent if missing (safe!)")
print("  .pop()           → remove a random item")
print("  .clear()         → remove everything")

# Think:
# 1. When would you choose .discard() over .remove()?
# 2. Why is .pop() unpredictable for sets but predictable for lists?
