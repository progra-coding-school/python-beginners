import pyttsx3

engine = pyttsx3.init()

# Slower storytelling pace for kids
engine.setProperty('rate', 70)
engine.setProperty('volume', 1.0)

# Find Indian voice
voices = engine.getProperty('voices')

indian_voice = None
for voice in voices:
    if "India" in voice.name or "Rishi" in voice.name or "Veena" in voice.name:
        indian_voice = voice.id
        break

# If Indian voice found, use it
if indian_voice:
    engine.setProperty('voice', indian_voice)
else:
    print("Indian voice not found. Please install Rishi or Veena from Mac settings.")

story = """
The Red Light That Rohan Ignored

Rohan loved speed.

Whether it was running, cycling, or even finishing his homework quickly—he always wanted to be the fastest.

One evening, Rohan and his mother were walking home from the park. They reached a busy road.

“Stop, Rohan,” his mother said calmly. “Wait for the signal to turn green.”

Rohan looked at the road.
There were no cars nearby.

“Amma, nothing is coming! I can go fast,” he said.

“Wait,” she repeated firmly. “Always follow the signal.”

But Rohan thought, I know better.

The moment his mother looked away, he dashed forward.

Suddenly—

🚗 HONK! HONK!

A car turned the corner at high speed.

Rohan froze in the middle of the road.

His heart started beating fast.

The car screeched to a stop just a few steps away from him.

For a moment… everything was silent.

His mother rushed forward and pulled him back to the sidewalk.

She didn’t shout.

She didn’t scold.

She just held his shoulders and said softly,

“Rohan… signals are not there to stop you. They are there to protect you.”

Rohan looked at the red light again.

This time, it felt different.

It wasn’t just a light anymore.

It was a warning.

A guide.

A protector.

The signal turned green.

His mother said, “Now we can go.”

Rohan held her hand tightly.

This time… he waited.
"""

engine.say(story)
engine.runAndWait()
engine.stop()