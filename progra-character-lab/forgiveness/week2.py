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
n a bright classroom in Chennai, two siblings studied in the same school — Rahul in Grade 5 and his younger sister Ananya in Grade 3.

Rahul loved drawing superheroes.
Ananya loved colouring flowers and rainbows.

One Sunday evening, Rahul had carefully arranged his favourite colour box — 24 beautiful crayons, all neatly placed.

“Please don’t use these without asking,” Rahul told Ananya.
“These are special.”

The next afternoon, Ananya had an art assignment.
She searched for her crayons… but couldn’t find them.

She saw Rahul’s colour box on the table.

“I’ll just use them carefully,” she thought.

She coloured slowly. She was careful.
But while sharpening the red crayon, it snapped in half.

“Oh no…”

She tried fixing it, but the crayon was clearly broken.

When Rahul returned from tuition, he opened his colour box.

“My red crayon! Who touched my colours?” he shouted.

Ananya stood quietly.

“I’m sorry, Anna… I needed it for school. I tried to be careful…”

Rahul was very upset. He had kept that set perfect for months.
He didn’t talk to her the entire evening.

That night, Amma noticed the silence.

She asked Rahul,
“If someone makes a mistake and says sorry, what matters more — the mistake or the relationship?”

Rahul didn’t answer.

Later, he saw Ananya sitting alone, trying to tape the broken crayon together.

She wasn’t careless.
She was scared.

Rahul felt something change inside him.

The next morning, he walked to her.

“I was angry… but I forgive you.”

Ananya looked up slowly.
“Really?”

“Yes. Next time, just ask me. We can share.”

Ananya smiled.

That evening, Rahul did something unexpected.

He gave her three crayons from his box.

“Now we both have special colours,” he said.

From that day, their colouring became more fun — not because the crayons were perfect…

…but because their bond was.
"""

engine.say(story)
engine.runAndWait()
engine.stop()