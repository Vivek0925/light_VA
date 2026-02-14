import keyboard

def handle_volume_commands(command, speak):
    if "volume up" in command:
        speak("Increasing volume")
        for _ in range(5):
            keyboard.press_and_release("volume up")
        return True

    elif "volume down" in command:
        speak("Decreasing volume")
        for _ in range(5):
            keyboard.press_and_release("volume down")
        return True

    elif "mute" in command:
        speak("Muting volume")
        keyboard.press_and_release("volume mute")
        return True

    return False