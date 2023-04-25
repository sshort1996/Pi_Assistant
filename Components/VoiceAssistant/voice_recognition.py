# Import required libraries
import speech_recognition as sr
import pyttsx3
import os


class TriggerAssistant:
    def __init__(self):
        # Initialize the speech recognizer and text-to-speech engine
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

        # Set the voice rate and volume
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1)

        # Start listening
        self.listen()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.pause_threshold = 1
            audio = self.recognizer.listen(source)

            try:
                # Use the speech recognizer to recognize speech from the audio
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                
                # write speech to an environment variable so it can be used by the GPT module
                os.environ['query'] = text

                # Continue listening even if some other word is spoken
                self.listen()

            except sr.UnknownValueError:
                print("Audio could not be recognized")
                self.listen()

    def say(self, text):
        print(f"Chat Assistant: {text}")
        
        # Use the text-to-speech engine to speak the response
        self.engine.say(text)
        self.engine.runAndWait()

# # Create a ChatAssistant object    
# assistant = TriggerAssistant()
