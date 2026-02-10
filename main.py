import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import pyautogui

# Text to speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 180)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Listen to voice
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.3)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

# Command processor
def run_command(command):
    print("Command received:", command)

    # STOP assistant
    if "stop" in command or "exit" in command or "quit" in command:
        speak("Goodbye")
        return False

    # OPEN YOUTUBE
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    # PLAY SONG
    elif "play" in command and "youtube" in command:
        song = command.replace("play", "").replace("on youtube", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    # PAUSE VIDEO (multiple variations)
    elif any(word in command for word in ["pause", "pass", "pose", "paws"]):
        speak("Pausing")
        pyautogui.press("k")

    # RESUME VIDEO
    elif "resume" in command or "play video" in command:
        speak("Resuming")
        pyautogui.press("k")

    # SEARCH GOOGLE
    elif "search for" in command:
        query = command.replace("search for", "")
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # OPEN GOOGLE
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    else:
        speak("Command not recognized")

    return True


# Main loop (Alexa-style)
speak("Light is ready")

running = True
while running:
    cmd = listen()

    if not cmd:
        continue

    # Only respond if wake word is present
    if "light" in cmd:
        command = cmd.replace("light", "").strip()
        if command:
            running = run_command(command)