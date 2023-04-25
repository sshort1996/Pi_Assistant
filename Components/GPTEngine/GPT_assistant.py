import openai
import os 
from icecream import ic

openai.api_key = "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" 

class GPTChatbot:
    def __init__(self, model_name="gpt-3.5-turbo", hyperparams = ""):
        self.model_name = model_name
        self.hyperparams = hyperparams

    def generate_response(self, prompt):
        completion = openai.ChatCompletion.create( 
        model = 'gpt-3.5-turbo',
        messages = [
            {'role': 'user', 'content': prompt}
        ],
        temperature = 0.5 
        )
        return completion['choices'][0]['message']['content']

    def chat(self):
        print("Welcome to the GPT Chatbot! Type 'quit' to exit.\n")
        while True:
            prompt = input("You: ")
            if prompt.lower() == "quit":
                break
            elif 'Ted' in prompt:
                response = self.generate_response(prompt)
                print("Bot:", response)
            else: 
                pass