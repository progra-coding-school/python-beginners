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
The Broken Robot and the Bigger Heart.

In a small house in Chennai lived two siblings,
Arjun and his little sister Meera.

Arjun loved building things.
After weeks of hard work,
he finished building a small robot.

'Don't touch it,' Arjun said gently.
'It is very delicate.'

But Meera was curious.

Suddenly... crash!

The robot fell.
One wheel broke.

When Arjun saw it,
he felt angry.

That night, their father asked him,
'Which is bigger, your robot... or your heart?'

Arjun thought deeply.

The next morning, he said,
'I forgive you, Meera.'

They repaired the robot together.

Forgiveness is choosing love over anger.

And that is how strong hearts are built.
"""

engine.say(story)
engine.runAndWait()
engine.stop()