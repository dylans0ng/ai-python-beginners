from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai = OpenAI()

system_prompt = 'You are an expert Python developer that is providing assistant to beginners learning programming for the first time.'
user_prompt = 'Explain what a Python variable is.'

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print('1: Starter Prompt\n')
print(response.choices[0].message.content)

# Clear instructions and goal
user_prompt = 'Explain what a Python variable is to someone learning programming for the first time. Help them understand why variables are useful.'

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print('2: Specific Instructions & Goal\n')
print(response.choices[0].message.content)

