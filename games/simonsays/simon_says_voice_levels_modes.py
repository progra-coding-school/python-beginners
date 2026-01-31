import pyttsx3
import random
import time


# ---------- SPEAK FUNCTION ----------
def speak(text, rate):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


# ---------- USER INPUT (SAFE DEFAULTS) ----------
mode = input("Enter mode (sitting / standing / online) [default: sitting]: ").strip().lower()
level_input = input("Enter level (1 to 5) [default: 1]: ").strip()

if mode == "":
    mode = "standing"

if level_input == "":
    level = 1
else:
    try:
        level = int(level_input)
        if level < 1 or level > 5:
            level = 1
    except:
        level = 1


# ---------- LEVEL SETTINGS ----------
# Higher level → faster speech + shorter pause
level_settings = {
    1: {"rate": 160, "delay": 2.5},
    2: {"rate": 170, "delay": 2.0},
    3: {"rate": 180, "delay": 1.5},
    4: {"rate": 190, "delay": 1.0},
    5: {"rate": 220, "delay": 0.6}
}

speech_rate = level_settings[level]["rate"]
delay_time = level_settings[level]["delay"]


# ---------- ACTION SETS ----------
sitting_actions = [
    "sit down",
    "sit straight",
    "sit like a statue",
    "touch your nose",
    "touch your ears",
    "touch your head",
    "touch your shoulders",
    "touch your knees",
    "wiggle your fingers",
    "wiggle your toes",
    "clap your hands softly",
    "raise your right hand",
    "raise your left hand",
    "raise both hands",
    "put both hands on your head",
    "cross your arms",
    "fold your hands",
    "blink your eyes",
    "wink your right eye",
    "wink your left eye",
    "smile",
    "make a happy face",
    "make a sad face",
    "wave hello",
    "wave goodbye",
    "nod your head",
    "shake your head slowly",
    "pucker your lips",
    "pat your belly"
]

standing_actions = [
    "stand straight",
    "stand on one foot",
    "stand like a statue",
    "clap your hands",
    "slowly clap your hands",
    "turn around slowly",
    "turn your head left",
    "turn your head right",
    "stretch your hands",
    "stretch your arms up",
    "stretch your arms sideways",
    "shake your right arm",
    "shake your left arm",
    "shake both arms gently",
    "raise both hands in the air",
    "raise your right hand",
    "raise your left hand",
    "touch your head",
    "touch your ears",
    "touch your shoulders",
    "touch your knees",
    "smile",
    "nod your head",
    "pretend you are a robot",
    "pretend you are driving a car"
]


online_actions = [
    "touch your nose",
    "touch your head",
    "blink your eyes",
    "smile at the camera",
    "raise your right hand",
    "raise your left hand",
    "nod your head",
    "wave hello",
    "talk like a robot"
]


# ---------- MODE SELECTION ----------
if mode == "sitting":
    actions = sitting_actions
    speak("Sitting mode activated. Stay seated.", speech_rate)
elif mode == "standing":
    actions = standing_actions
    speak("Standing mode activated. You may stand.", speech_rate)
elif mode == "online":
    actions = online_actions
    speak("Online mode activated. Stay in front of the camera.", speech_rate)
else:
    mode = "sitting"
    actions = sitting_actions
    speak("Invalid mode. Defaulting to sitting mode.", speech_rate)


# ---------- GAME START ----------
print(f"\n🎮 Simon Says Started | MODE: {mode.upper()} | LEVEL: {level}")
print("Follow ONLY if you hear 'Simon says'\n")

rounds = 50

for i in range(rounds):
    time.sleep(delay_time)

    action = random.choice(actions)

    if random.choice([True, False]):
        command = f"Simon says {action}"
    else:
        command = action

    speak(command, speech_rate)


print("\n🎉 Game Over! Well done kids!")
speak("Game over! Well done kids!", speech_rate)
