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
“The Kite That Wouldn’t Fly”

Rohan and his younger sister Meera loved flying kites on their terrace.

One Sunday evening, the sky was perfect. The breeze was cool, and the sunlight was soft and golden.

Rohan had made a brand new kite. It was bright blue, with a long tail that danced in the wind.

He looked at Meera and said,
“Don’t touch it. You might spoil it.”

Meera nodded quietly.

After some time, Rohan went downstairs to get snacks.

Meera looked at the kite again. It was so beautiful.

“I’ll just hold it for a second,” she thought.

She picked it up carefully.

But suddenly… snap.

The kite tore.

Meera froze. Her heart started beating fast.

When Rohan came back and saw the torn kite, his face changed.

“I told you not to touch it!” he shouted.
“You always ruin things!”

Meera’s eyes filled with tears.
“I’m sorry… I didn’t mean to…”

But Rohan turned away.
“I’m not talking to you.”

That night, they didn’t speak.

The next day, they still didn’t speak.

The house felt quiet. The terrace felt empty.

They didn’t play together. They didn’t laugh.

Even when Meera tried to smile at him, Rohan looked away.

On the third day, Rohan went to the terrace.

He saw Meera sitting alone.

She was holding the torn kite, trying to fix it with tape.

Her hands were shaking.

She whispered softly,
“I just wanted to fly it with him…”

Rohan stood there quietly.

For the first time, he started thinking.

“She didn’t want to spoil it… she just wanted to be with me.”

He looked at the kite.

Then he looked at Meera.

He had a choice.

He could stay angry… or he could let it go.

Slowly, he walked towards her.

Without saying anything, he sat next to her.

He gently held the kite and said,
“Let’s fix it together.”

Meera looked up.

Her eyes were still wet… but now there was a small smile.

That evening, the kite flew again.

It didn’t fly perfectly. It moved a little here and there.

But both of them were smiling.

And somehow, that kite felt even more special than before.
"""

engine.say(story)
engine.runAndWait()
engine.stop()