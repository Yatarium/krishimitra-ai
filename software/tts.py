"""
tts.py — KrishiMitra AI
Converts Hindi text to speech, fully offline (pyttsx3 wraps espeak on Linux/Pi).
Install on the Pi with: sudo apt install espeak && pip install pyttsx3
"""
import pyttsx3


def speak(text, rate=140):
    """Speaks the given Hindi text aloud through the connected speaker."""
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)

    # Try to select a Hindi voice if available on the system
    for voice in engine.getProperty("voices"):
        if "hi" in voice.id.lower() or "hindi" in voice.name.lower():
            engine.setProperty("voice", voice.id)
            break

    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python tts.py <hindi_text>")
        sys.exit(1)
    speak(sys.argv[1])
