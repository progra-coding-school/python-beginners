# Program Code: TU-PS-02
# Title: RGB Colour Mixer
# Cognitive Skill: Problem Solving
# Topic: Tuples in Python

# Problem:
# Colours on a screen are made of (Red, Green, Blue) values — each 0 to 255.
# Use tuples to store and mix colours.
# Tasks: display a palette, mix two colours, find the brightest.

# --- Colour palette ---
palette = {
    "red"    : (255,   0,   0),
    "green"  : (  0, 255,   0),
    "blue"   : (  0,   0, 255),
    "yellow" : (255, 255,   0),
    "cyan"   : (  0, 255, 255),
    "white"  : (255, 255, 255),
    "black"  : (  0,   0,   0),
    "orange" : (255, 165,   0),
}

print("=== Colour Palette ===")
print(f"  {'Colour':<10} {'R':>4} {'G':>4} {'B':>4}  {'Hex':>8}")
print(f"  {'─'*10} {'─'*4} {'─'*4} {'─'*4}  {'─'*8}")
for name, (r, g, b) in palette.items():
    hex_code = f"#{r:02X}{g:02X}{b:02X}"
    print(f"  {name:<10} {r:>4} {g:>4} {b:>4}  {hex_code:>8}")

print()

# --- Mix two colours (average each channel) ---
def mix_colours(c1, c2):
    r = (c1[0] + c2[0]) // 2
    g = (c1[1] + c2[1]) // 2
    b = (c1[2] + c2[2]) // 2
    return (r, g, b)

print("=== Colour Mixing ===")
red    = palette["red"]
blue   = palette["blue"]
mixed  = mix_colours(red, blue)
print(f"red {red} + blue {blue} = {mixed}")

yellow = palette["yellow"]
cyan   = palette["cyan"]
mixed2 = mix_colours(yellow, cyan)
print(f"yellow {yellow} + cyan {cyan} = {mixed2}")

print()

# --- Brightness: higher total = brighter ---
def brightness(colour):
    return sum(colour)     # R + G + B

print("=== Brightness ===")
for name, rgb in palette.items():
    b = brightness(rgb)
    print(f"  {name:<10} brightness: {b}")

brightest = max(palette, key=lambda n: brightness(palette[n]))
darkest   = min(palette, key=lambda n: brightness(palette[n]))
print(f"\nBrightest: {brightest} {palette[brightest]}")
print(f"Darkest  : {darkest} {palette[darkest]}")

# Think:
# 1. Why is a tuple better than a list for storing an RGB colour?
# 2. What would you change to mix THREE colours instead of two?
