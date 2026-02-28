# Program Code: TU-PS-01
# Title: Coordinate Tracker
# Cognitive Skill: Problem Solving
# Topic: Tuples in Python

# Problem:
# A robot on a grid starts at position (0, 0).
# It receives movement commands: 'U', 'D', 'L', 'R'.
# Track its path using tuples and find:
# 1. Final position
# 2. All visited positions
# 3. Distance from start (Manhattan distance)

# --- Setup ---
start    = (0, 0)
commands = ['R', 'R', 'U', 'U', 'U', 'L', 'D', 'R', 'R', 'U']

moves = {
    'U': ( 0,  1),
    'D': ( 0, -1),
    'L': (-1,  0),
    'R': ( 1,  0),
}

print("=== Robot Coordinate Tracker ===")
print(f"Start    : {start}")
print(f"Commands : {commands}")
print()

# --- Step 1: Track the path ---
path     = [start]
current  = start

for cmd in commands:
    dx, dy  = moves[cmd]
    x, y    = current
    current  = (x + dx, y + dy)   # create a NEW tuple — tuples are immutable
    path.append(current)

print("=== Path taken ===")
for i, pos in enumerate(path):
    label = " ← START" if i == 0 else (" ← END" if i == len(path)-1 else "")
    print(f"  Step {i:>2}: {pos}{label}")

print()

# --- Step 2: Final position ---
final = path[-1]
print(f"Final position : {final}")

# --- Step 3: Manhattan distance from start ---
manhattan = abs(final[0] - start[0]) + abs(final[1] - start[1])
print(f"Distance from start (Manhattan): {manhattan} steps")

print()

# --- Step 4: Were any positions revisited? ---
print("=== Revisited positions ===")
visited      = set()
revisited    = []
for pos in path:
    if pos in visited:
        revisited.append(pos)
    visited.add(pos)

if revisited:
    print("Revisited:", revisited)
else:
    print("No position was revisited.")

# Think:
# 1. Why is a tuple better than a list for storing a coordinate (x, y)?
# 2. How would you extend this to a 3D coordinate (x, y, z)?
