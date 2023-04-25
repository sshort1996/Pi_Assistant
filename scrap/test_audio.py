import pyttsx3

def speak(text):
    # Initialize the engine
    engine = pyttsx3.init()
    # Convert the text to speech
    engine.say(text)
    # Play the speech
    engine.runAndWait()

speak('Hello')