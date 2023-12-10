import os
from openai import OpenAI
from get_secrets import get_open_api_key

client = OpenAI(
    # This is the default and can be omitted
    api_key=get_open_api_key(),
)


def test_chat_completion(question, model="gpt-3.5-turbo"):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model=model,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        message = "Error: Couldn't integrate with openai." + str(e)
        return message
    

class ChatGPTService:
    def ask(self, question,  model="gpt-3.5-turbo"):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model=model,
        )
        return chat_completion.choices[0].message.content