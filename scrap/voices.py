import pyttsx3

engine = pyttsx3.init('espeakng')
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id)
