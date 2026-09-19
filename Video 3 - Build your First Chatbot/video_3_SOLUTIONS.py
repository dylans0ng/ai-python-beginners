from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai = OpenAI()

# system_prompt = 'You are an expert Python developer that is providing assistant to beginners learning programming for the first time.'
# user_prompt = 'Explain what a Python variable is in one sentence.'

# response = openai.chat.completions.create(
#     model='gpt-4.1-mini',
#     messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
# )

# print(response.choices[0].message.content)

# while True:
#     user_input = input('You: ')
    
#     if user_input.lower() == 'quit':
#         print('Chat ended.')
#         break

#     response = openai.chat.completions.create(
#         model='gpt-4.1-mini',
#         messages=[{'role': 'system', 'content': 'You are an AI assistant that provides academic support in math and computer science.'}, 
#                 {'role': 'user', 'content': user_input}]
#     )

#     print(f"AI: {response.choices[0].message.content}")

def ask_ai(prompt):
    response = openai.chat.completions.create(
        model='gpt-4.1-mini',
        messages=[{'role': 'system', 'content': 'You are an AI assistant that provides academic support in math and computer science.'}, 
                {'role': 'user', 'content': prompt}]
    )

    return response.choices[0].message.content

while True:
    user_input = input('You: ')
    
    if user_input.lower() == 'quit':
        print('Chat ended.')
        break

    response = ask_ai(user_input)

    print(f'AI: {response}')