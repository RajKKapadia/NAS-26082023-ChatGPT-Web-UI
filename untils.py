import os

import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')


def chat_completion(messages: list) -> list[str]:
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            stream=True
        )
        collected_messages = []
        for chunk in response:
            delta = chunk['choices'][0]['delta']
            if 'content' in delta.keys():
                collected_messages.append(delta['content'])
        return collected_messages
    except:
        return ['We are facing a technical issue at this moment.']

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
    formated_messages = format_messages(chatbot)
    bot_messages = chat_completion(formated_messages)
    chatbot[-1][1] = ''
    chatbot[-1][1] = ''
    for bm in bot_messages:
        chatbot[-1][1] += bm
        yield chatbot
    return chatbot

def set_user_query(text: str, chatbot: list[list]) -> tuple:
    chatbot += [[text, None]]
    return '', chatbot
