from Components.GPTEngine.GPT_assistant import GPTChatbot
from Components.VoiceAssistant.voice_recognition import TriggerAssistant
import os


listener = TriggerAssistant()
engine = GPTChatbot()
response = engine.generate_response(os.environ['query'])
print(response)