from openai import OpenAI
import properties

data = properties.properties_read()
chat_key = data["key"]
chat_engine = data["engine"]
chat_history = []

def message_prompt(prompt):
    if len(chat_history) == 20 :
        chat_history.pop(0)
        chat_history.pop(0)

    user_format = {"role":"user","content": str(prompt)}
    chat_history.append(user_format)
    client = OpenAI(api_key=chat_key)

    response = client.chat.completions.create(
    model=chat_engine,
    messages=chat_history,
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    chat_message_response = response.choices[0].message.content

    assistance_format = {"role":"assistant","content": chat_message_response}
    chat_history.append(assistance_format)

    return chat_message_response

