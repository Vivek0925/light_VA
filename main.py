import speech_recognition as sr
import pyttsx3
import webbrowser

from commands.apps import handle_app_commands
from commands.volume import handle_volume_commands

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
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Network error")
        return ""

# Command processor
def run_command(command):
    print("Command received:", command)

    # Stop assistant
    if any(word in command for word in ["stop", "exit", "quit"]):
        speak("Goodbye")
        return False

    # Volume commands
    if handle_volume_commands(command, speak):
        return True

    # App & media commands
    if handle_app_commands(command, speak):
        return True

    # Google search
    if "search for" in command:
        query = command.replace("search for", "").strip()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            return True

    # Open Google
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
        return True

    speak("Command not recognized")
    return True


# Main loop
def main():
    speak("Light is ready")

    running = True
    while running:
        cmd = listen()

        if not cmd:
            continue

        # Wake word detection
        if "light" in cmd:
            command = cmd.replace("light", "").strip()
            if command:
                running = run_command(command)

if __name__ == "__main__":
    main()