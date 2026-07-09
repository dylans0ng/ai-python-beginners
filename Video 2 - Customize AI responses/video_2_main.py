from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai = OpenAI()

system_prompt = 'You are an expert Python developer that is providing assistant to beginners learning programming for the first time.'
user_prompt = 'Explain what a Python list is.'

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print('1: Starter Prompt\n')
print(response.choices[0].message.content)

# METHOD 1 - Clear instructions and goal

# METHOD 2 - Specific tone


# METHOD 3 - Specific Format


# METHOD 4 - One-shot Prompting


# BUILD A DYNAMIC PROMPT!


# Interactive Prompting Tool
