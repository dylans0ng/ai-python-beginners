from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai = OpenAI()

def ask_ai(prompt):
    response = openai.chat.completions.create(
            model='gpt-4.1-mini',
            messages=[{'role': 'system', 'content': 'You are an assistant that provides academic support.'}, 
                      {'role': 'user', 'content': prompt}]
    )
    
    return response.choices[0].message.content
    
while True:
    user_prompt = input('You: ')
    
    if user_prompt.lower() == 'quit':
        print('Chat has ended.')
        break
    
    response = ask_ai(user_prompt)

    print(f'AI: {response}')
