import os

import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')


def chat_completion(messages: list[dict]) -> str:
    try:
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages
        )
        return completion.choices[0].message['content']
    except:
        return 'We are facing an issue.'

# print(chat_completion([
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ]))


def format_messages(chat_history: list[list]) -> list[dict]:
    formated_messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    for i in range(len(chat_history)):
        ch = chat_history[i]
        formated_messages.append(
            {
                "role": "user",
                "content": ch[0]
            }
        )
        if ch[1] != None:
            formated_messages.append(
                {
                    "role": "assistant",
                    "content": ch[1]
                }
            )
    return formated_messages

# chat_history = [['hi', None] ['']]

# print(format_messages(chat_history))


def generate_response(text: str, chatbot: list[list]) -> tuple:
    print(chatbot)
    formated_messages = format_messages(chatbot)
    print(formated_messages)
    response = chat_completion(formated_messages)
    chatbot[-1][1] = response
    return '', chatbot

def set_user_query(text: str, chatbot: list[list]) -> tuple:
    chatbot += [[text, None]]
    print(chatbot)
    return '', chatbot
