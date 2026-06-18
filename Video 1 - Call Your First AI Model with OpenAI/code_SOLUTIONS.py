from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai = OpenAI()

system_prompt = 'You are an expert Python developer that is providing assistant to beginners learning programming for the first time.'
user_prompt = 'Explain what a Python variable is in one sentence.'

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt},{'role': 'user', 'content': user_prompt}]
)

print(response.choices[0].message.content)