import pyautogui
import webbrowser
import pywhatkit
import time
import pygetwindow as gw


# Focus the browser window
def focus_browser():
    browsers = ["chrome", "edge", "firefox", "brave"]
    for title in gw.getAllTitles():
        for browser in browsers:
            if browser in title.lower():
                try:
                    win = gw.getWindowsWithTitle(title)[0]
                    win.activate()
                    time.sleep(0.5)  # allow focus to switch
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
        if focus_browser():
            pyautogui.press("k")
        else:
            speak("Browser not found")
        return True

    # RESUME VIDEO
    elif "resume" in command:
        speak("Resuming")
        if focus_browser():
            pyautogui.press("k")
        else:
            speak("Browser not found")
        return True

    # GENERIC OPEN APP
    elif "open" in command:
        app_name = command.replace("open", "").strip()
        if app_name:
            return open_app(app_name, speak)

    return False