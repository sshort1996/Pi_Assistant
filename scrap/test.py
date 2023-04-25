import pyttsx3
import time 


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice to one with a more questioning intonation
voices = engine.getProperty('voices')
index = 0
while True:
    try:    
        engine.setProperty('voice', voices[index].id)

        # Set the voice rate and volume
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1)

        # Speak the response with intonation
        print(voices[index].id)
        engine.say("Yes")
        engine.runAndWait()
        index += 1
        time.sleep(0.5)
    except Exception as err:
        print(err)
        break