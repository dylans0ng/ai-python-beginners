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

print('Starter Prompt\n')
print(response.choices[0].message.content)




# METHOD 1 - Clear instructions and goal
user_prompt = """
I am someone who has never coded before. Please explain what a Python list is
and use 3 different analogies to help my understanding."""

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print('--------------------------------------------')
print('METHOD 1 - CLEAR INSTRUCTIONS AND GOAL\n')
print(response.choices[0].message.content)


# METHOD 2 - Specific tone
user_prompt = 'Explain what a Python list is. Please use a friendly and encouraging tone.'

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print()
print()
print('--------------------------------------------')
print('METHOD 2 - SPECIFIC TONE\n')
print(response.choices[0].message.content)


# METHOD 3 - Specific Format
user_prompt = """
Explain what a Python lists is to someone learning programming for the first time.

Format your response with:
1. A one-sentence definition
2. A simple Python code example
3. A one-sentence explanation of the code
"""

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print()
print()
print('--------------------------------------------')
print('METHOD 3 - SPECIFIC FORMAT\n')
print(response.choices[0].message.content)


# METHOD 4 - One-shot Prompting
user_prompt = """
Explain programming concepts in this style:

Topic: Python lists

Explanation:
A Python list is like a shopping basket that can hold multiple items in one place.

Code:
fruits = ["apple", "banana", "orange"]

Code explanation:
This list stores three fruit names in one variable.

Now explain Python lists using the same beginner-friendly style and structure.
"""

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print()
print()
print('--------------------------------------------')
print('METHOD 4 - ONE-SHOT PROMPTING\n')
print(response.choices[0].message.content)

# BUILD A DYNAMIC PROMPT!
topic = 'Python lists'
audience = 'Someone who has never coded in their life before.'
tone = 'Friendly and encouraging'
format_instructions = """
Format your response with:
1. A one-sentence definition
2. A simple Python code example
3. A one-sentence explanation of the code
"""

user_prompt = f"""
Explain {topic} to {audience}.

Please respond in this {tone} tone.

Format instructions...
{format_instructions}
"""

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print()
print()
print('--------------------------------------------')
print('DYNAMIC PROMPT\n')
print(response.choices[0].message.content)


# Interactive Prompting Tool
print('--------------------------------------------')
print('INTERACTIVE PROMPTING TOOL\n')
print('--------------------------------------------')
topic = input('What Python topic are you interested in learning? ')
audience = 'Someone who has never coded in their life before.'
tone = input('Which kind of tone is best suited for your learning (friendly, professional, etc)? ')
format_instructions = """
Format your response with:
1. A one-sentence definition
2. A simple Python code example
3. A one-sentence explanation of the code
"""

user_prompt = f"""
Explain {topic} to {audience}.

Please respond in this {tone} tone.

Format instructions...
{format_instructions}
"""

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print()
print()
print(response.choices[0].message.content)
