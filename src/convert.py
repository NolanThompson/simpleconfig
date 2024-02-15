import os
from openai import OpenAI
from dotenv import load_dotenv, dotenv_values
load_dotenv()

#openai auth
client = OpenAI()

def chat_completion(prompt):
    message = [{"role": "system", "content": prompt}]
    response = client.chat.completions.create(model="gpt-4", messages=message)
    answer = response.choices[0].message.content
    return answer

def convert_instructions(prompt):
    response = chat_completion(prompt)
    return response