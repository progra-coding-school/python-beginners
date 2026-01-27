import pyttsx3
import random
import time

def speak(text):
    engine = pyttsx3.init()          # re-initialize every time
    engine.setProperty('rate', 150)
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

actions = [
    "sit",
    "stand",
    "jump",
    "turn around",
    "clap your hands",
    "touch your head",
    "stretch your hands",
    "raise your hands",
    "spin once"
]

print("🎮 Simon Says Voice Game Started!")
print("Follow ONLY if you hear 'Simon says'\n")

rounds = 12

for i in range(rounds):
    time.sleep(2)

    action = random.choice(actions)

    if random.choice([True, False]):
        command = f"Simon says {action}"
    else:
        command = action

    speak(command)

print("\n🎉 Game Over! Well done kids!")
speak("Game over. Well done kids!")