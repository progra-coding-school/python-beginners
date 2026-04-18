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
Riya and Arjun were best friends.

Every day after school, they played cricket in the small ground near their house.

One evening, Arjun brought a brand new cricket bat.

“Be careful,” he said. “It’s my favorite.”

Riya smiled. “Of course.”

They started playing.

Riya took the bat and got ready to hit.

The ball came fast.

She swung hard.

THUD!

The ball flew… not to the ground… but straight into a nearby window.

CRASH!

The glass shattered.

Both of them froze.

They looked at each other.

Riya’s heart started racing.

“Oh no… what do we do?” she whispered.

Arjun quickly said,
“Just leave it. No one saw us.”

Riya looked at the broken window.

Then she looked at the bat in her hand.

“It was my shot,” she said slowly.

“But we’ll get into trouble!” Arjun replied.

Riya didn’t move.

For a moment, she thought…
“Maybe I can just walk away.”

No one was around.

No one would know.

But something inside her didn’t feel right.

She took a deep breath.

“I think we should tell the truth,” she said.

Arjun shook his head.
“You’re crazy.”

But Riya had already started walking toward the house.

Her steps were slow… but steady.

She knocked on the door.

An old uncle opened it.

He looked at the broken window… and then at Riya.

“Did you do this?” he asked.

Riya swallowed.

“Yes… I’m sorry. It was my mistake.”

There was silence.

Arjun stood far behind, nervous.

The uncle looked at her for a few seconds.

Then his expression softened.

“Thank you for telling the truth,” he said.

“I was watching from inside.”

Riya blinked in surprise.

“I saw everything. You could have run away… but you didn’t.”

He smiled gently.

“Mistakes happen. But honesty is what matters.”

Riya felt something lift off her chest.

“I will help fix it,” she said.

The uncle nodded.

“That’s called responsibility.”

Arjun slowly walked forward.

He looked at Riya.

“You weren’t crazy,” he said quietly.

Riya smiled.

That day, they didn’t just play cricket.

They learned something bigger.

Doing the wrong thing is easy.

But taking responsibility…
that is what makes you strong.
"""

engine.say(story)
engine.runAndWait()
engine.stop()