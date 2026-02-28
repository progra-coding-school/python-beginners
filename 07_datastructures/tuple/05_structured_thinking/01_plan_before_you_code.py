# Program Code: TU-ST-01
# Title: Plan Before You Code
# Cognitive Skill: Structured Thinking
# Topic: Tuples in Python

# Task: Build a cinema seat booking system.
# Seats are identified by (row, seat_number) — a perfect tuple use case.

# ─── PLANNING TEMPLATE ───────────────────────────────────────────
# Problem  : Track which cinema seats are booked.
# Inputs   : Seat requests as (row, col) tuples
# Outputs  : Confirm booking, show booked vs available, reject duplicates
# Structure: set of tuples — each booked seat is a (row, col) tuple
# Steps    :
#   1. Define the hall (rows A-E, seats 1-6)
#   2. Create a set to track booked seats
#   3. Book a seat — check if already taken
#   4. Cancel a booking
#   5. Display the seating chart
# Edge cases: Booking the same seat twice? Cancelling an unbooked seat?
# ─────────────────────────────────────────────────────────────────

print("=== Cinema Seat Booking System ===")

# --- Step 1: Define hall ---
rows  = ['A', 'B', 'C', 'D', 'E']
seats = [1, 2, 3, 4, 5, 6]

# --- Step 2: Booked seats ---
booked = set()

# --- Step 3: Book a seat ---
def book(row, seat):
    s = (row, seat)
    if s in booked:
        print(f"  Sorry! Seat {row}{seat} is already booked.")
    else:
        booked.add(s)
        print(f"  Seat {row}{seat} booked successfully!")

# --- Step 4: Cancel ---
def cancel(row, seat):
    s = (row, seat)
    if s in booked:
        booked.discard(s)
        print(f"  Seat {row}{seat} booking cancelled.")
    else:
        print(f"  Seat {row}{seat} was not booked.")

# --- Step 5: Display ---
def display_hall():
    print("\n  Seat Map (X=booked, O=available)")
    print("      " + "  ".join(str(s) for s in seats))
    for row in rows:
        row_display = ""
        for seat in seats:
            row_display += "  X" if (row, seat) in booked else "  O"
        print(f"  {row}  {row_display}")
    print()

# --- Demo ---
book("A", 1)
book("B", 3)
book("A", 1)    # duplicate
book("C", 5)
book("D", 2)
display_hall()

cancel("B", 3)
cancel("Z", 9)  # invalid
display_hall()

print(f"Total booked: {len(booked)} seats")
print("Booked seats:", sorted(booked))

# Think:
# 1. Why is a tuple (row, seat) better than a string "A1" for identifying a seat?
# 2. Write the 5-step plan for a "bus route stop tracker" before coding it.
