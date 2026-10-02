from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai = OpenAI()

### OLD CODE FROM VIDEO 3!!! 

# def ask_ai(prompt):
#     response = openai.chat.completions.create(
#             model='gpt-4.1-mini',
#             messages=[{'role': 'system', 'content': 'You are an assistant that provides academic support.'}, 
#                       {'role': 'user', 'content': prompt}]
#     )
    
#     return response.choices[0].message.content
    
# while True:
#     user_prompt = input('You: ')
    
#     if user_prompt.lower() == 'quit':
#         print('Chat has ended.')
#         break
    
#     response = ask_ai(user_prompt)

#     print(f'AI: {response}')

messages = [
    {
        'role': 'system',
        'content': 'You are an assistant that provides academic support.'
    }
]

def ask_ai(messages):
    response = openai.chat.completions.create(
            model='gpt-4.1-mini',
            messages=messages
    )
    
    return response.choices[0].message.content
    

    
while True:
    user_prompt = input('You: ')
    
    if user_prompt.lower() == 'quit':
        print('Chat has ended.')
        break
    
    messages.append({'role': 'user', 'content': user_prompt})
    
    response = ask_ai(messages)
    
    messages.append({
        "role": "assistant",
        "content": response
    })

    print(f'AI: {response}')


