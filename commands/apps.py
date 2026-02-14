import pyautogui
import webbrowser
import pywhatkit
import time
import pygetwindow as gw


# Focus the YouTube tab specifically
def focus_youtube_tab():
    for title in gw.getAllTitles():
        if "youtube" in title.lower():
            try:
                win = gw.getWindowsWithTitle(title)[0]
                win.activate()
                time.sleep(0.5)
                return True
            except:
                pass
    return False


# Open any app via Windows search
def open_app(app_name, speak):
    try:
        speak(f"Opening {app_name}")
        pyautogui.press("win")
        time.sleep(1)
        pyautogui.write(app_name)
        time.sleep(1)
        pyautogui.press("enter")
        return True
    except:
        speak("Could not open the app")
        return False


def handle_app_commands(command, speak):
    # OPEN YOUTUBE
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        return True

    # PLAY SONG
    elif "play" in command:
        song = command.replace("play", "").strip()
        if song:
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)
            return True

    # PAUSE VIDEO
    elif any(word in command for word in ["pause", "pass", "pose", "paws"]):
        speak("Pausing")
        if focus_youtube_tab():
            pyautogui.press("k")
        else:
            speak("YouTube tab not found")
        return True

    # RESUME VIDEO
    elif "resume" in command:
        speak("Resuming")
        if focus_youtube_tab():
            pyautogui.press("k")
        else:
            speak("YouTube tab not found")
        return True

    # GENERIC OPEN APP
    elif "open" in command:
        app_name = command.replace("open", "").strip()
        if app_name:
            return open_app(app_name, speak)

    return False