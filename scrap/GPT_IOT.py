import openai
import os 
from icecream import ic

openai.api_key = "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" 

class GPTChatbot:
    def __init__(self, model_name="gpt-3.5-turbo", hyperparams = ""):
        self.model_name = model_name
        self.hyperparams = hyperparams

    def generate_response(self, prompt):
        ic(f'{prompt}\n{hyperparams["smart_home_network"]}')
        completion = openai.ChatCompletion.create( 
        model = 'gpt-3.5-turbo',
        messages = [
            {'role': 'user', 'content': f'{prompt}\n{hyperparams["smart_home_network"]}'}
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
            response = self.generate_response(prompt)
            print("Bot:", response)

hyperparams = {"smart_home_network":"""Pretend you are a smart home assistant, my
        smart home network consists of a smart bulb in my bedroom, my tv in my bedroom, 
        my tv in my living room, my google nest hub in my bedroom, and my google home speaker
        in my bathroom."""}
    # "question_flag": """IMPORTANT: If your response requires an answer, then flag that your response to my prompt requires me to answer, ie. flag your response as being a question. Give every answer in this conversation in the format:
#     Your response to the prompt
#     flag if the response is a question
#     """}
chatbot = GPTChatbot(hyperparams)
chatbot.chat()