import os
import openai

def chat_completion(prompt):
    openai.api_key = os.environ['CHATGPT_KEY']  # ChatGPT auth

    message = [{"role": "system", "content": prompt}]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message,
    )

    answer = response.choices[0].message.content
    return answer


def convert_instructions(prompt):
    response = chat_completion(prompt)
    return response