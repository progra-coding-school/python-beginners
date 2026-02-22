# Program Code: CF-KN-04
# Title: While Loop, Break, and Continue
# Cognitive Skill: Knowledge
# Topic: Control Flow in Python

# ── WHILE LOOP ─────────────────────────────────────────────────────────────
# Keep repeating AS LONG AS the condition is True.

count = 0
while count < 5:
    print(count)
    count += 1        # increment — MUST do this or loop runs forever!
print("Loop finished!")

# Explanation:
# count starts at 0.
# The loop continues as long as count < 5.
# Each iteration prints count, then adds 1.
# When count becomes 5, the condition is False → loop stops.

# ── BREAK — exit the loop immediately ─────────────────────────────────────
print("--- break in a for loop ---")
for i in range(1, 10):
    if i == 5:
        break
    print(i)
print("Loop ended at break.")

# Explanation:
# Runs i = 1,2,3,4. When i becomes 5, break exits immediately.
# 5,6,7,8,9 are never printed.

print("--- break in a while loop ---")
count = 0
while count < 10:
    if count == 5:
        break
    print(count)
    count += 1
print("Loop finished!")

# ── CONTINUE — skip this iteration, go to next ────────────────────────────
print("--- continue in a for loop ---")
for i in range(1, 10):
    if i == 5:
        continue       # skip 5, keep going
    print(i)
    print("Hello", i)

print("--- continue in a while loop ---")
count = 0
while count < 10:
    if count == 5:
        count += 1
        continue       # skip printing 5
    print(count)
    count += 1

# ── REAL-WORLD EXAMPLE: Seat Booking with break ───────────────────────────
print("--- Seat booking system ---")
for seat in range(10):
    if seat == 6:
        print("Seats 6-9 are reserved. Booking closed.")
        break
    print("Ticket is booked for seat", seat)

# Think:
# 1. What makes a while loop different from a for loop?
# 2. What happens if you forget count += 1 inside a while loop?
# 3. In the seat booking example, how would you change it to allow 8 seats?
