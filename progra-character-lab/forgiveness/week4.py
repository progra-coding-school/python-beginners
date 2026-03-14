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
At school, the teacher announced an exciting activity.

“Next week,” she said, “every group will present a science project.”

Nisha and Aman were placed in the same team.

Nisha had a great idea.

“Let’s build a volcano model that erupts!” she said.

For three days they worked after school.
They shaped the mountain using clay, painted it brown and green, and prepared the special mixture that would make the volcano erupt.

Their project looked amazing.

“Don’t touch it until tomorrow,” Nisha told Aman.
“We will present it in class.”

The next morning, Aman came early to school.

He looked at the volcano.

“I wonder how big the eruption will be,” he thought.

He poured the mixture into the volcano.

But he added too much.

Suddenly—

FOOOOSH!

The volcano overflowed.

Red liquid spilled everywhere.
The top of the volcano collapsed.

When Nisha arrived, she was shocked.

“Our project! What happened?” she cried.

Aman looked down.

“I… I tried the experiment early. I wanted to see if it worked.”

Nisha felt angry.

“We worked so hard for this!”

Aman’s eyes filled with tears.

“I’m really sorry. I didn’t think it would break.”

For a moment, Nisha stayed silent.

Then she remembered something her grandmother once told her:

“Mistakes are part of learning.
What matters is how we treat people after the mistake.”

Nisha took a deep breath.

“We still have time,” she said.

“Let’s fix it together.”

Aman looked surprised.

“You’re not angry anymore?”

“I was,” Nisha said, smiling a little.
“But I forgive you. Now let’s rebuild our volcano.”

During lunch break, they repaired the model together.

When it was time for presentation, their volcano erupted perfectly.

The whole class clapped.

But Nisha knew something more important had happened.

They didn’t just fix a project.

They strengthened their friendship.
"""

engine.say(story)
engine.runAndWait()
engine.stop()