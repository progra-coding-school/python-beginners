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
One evening after school, a group of children gathered in the playground to play football.
Among them were Karthik and his best friend Dev.

They always played on the same team.
They passed the ball to each other.
They celebrated every goal together.

That day, the match was very close.

One goal would decide the winner.

Dev ran quickly with the ball and saw Karthik standing near the goalpost.

“Karthik! Pass the ball!” Dev shouted.

But Karthik thought, If I score this goal, everyone will cheer for me.

So he didn’t pass.

He tried to shoot… but missed.

The other team quickly took the ball and scored.

The match was over.

Dev was upset.

“You should have passed the ball! We could have won!” he said.

Karthik felt embarrassed, but his pride stopped him from admitting it.

“Well, you could have scored earlier too!” he replied angrily.

For the first time in months, the two friends walked home without speaking.

That night, Karthik kept thinking about the match.

He remembered Dev always sharing the ball with him.
He remembered how they had helped each other win many games.

Karthik slowly realized something.

He had chosen pride over friendship.

The next day at school, he walked up to Dev during recess.

“I’m sorry,” Karthik said quietly.

“I should have passed the ball. I was thinking only about scoring myself.”

Dev looked at him for a moment.

Then he smiled.

“That’s okay. Friends make mistakes… but friends also forgive.”

Later that evening, they played football again.

This time, when Karthik ran with the ball, he saw Dev near the goal.

He passed the ball.

Dev scored.

Both of them laughed and celebrated together.

And Karthik learned an important lesson:

Winning a match feels good.
But keeping a friendship is even better.
"""

engine.say(story)
engine.runAndWait()
engine.stop()