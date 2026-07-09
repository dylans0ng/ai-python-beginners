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
user_prompt = 'Explain what a Python list is to someone learning programming for the first time. Help them understand why lists are useful.'

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print('----------------------------------------------')
print('2: Specific Instructions & Goal\n')
print(response.choices[0].message.content)

# METHOD 2 - Specific tone
user_prompt = """
Explain what a Python lists is to someone learning programming for the first time.
Help them understand why lists are useful.
Use a friendly and encouraging tone.
"""

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print('----------------------------------------------')
print('3: Specific Tone\n')
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

print('----------------------------------------------')
print('4: Specific Format\n')
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

Now explain Python variables using the same beginner-friendly style and structure.
"""

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print('----------------------------------------------')
print('5: One-shot Prompting\n')
print(response.choices[0].message.content)

# BUILD A DYNAMIC PROMPT!
topic = "Python variables"
audience = "someone learning programming for the first time"
tone = "friendly and encouraging"
format_instructions = """
1. A one-sentence definition
2. A simple Python code example
3. A one-sentence explanation of the code
"""

user_prompt = f"""
Explain {topic} to {audience}.

Use a {tone} tone.

Format your response with:
{format_instructions}
"""

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print('----------------------------------------------')
print('DYNAMIC PROMPT\n')
print(response.choices[0].message.content)

# Interactive Prompting Tool
topic = input('What Python topic do you want to learn? ')
audience = "someone learning programming for the first time"
tone = input('What kind of tone is best for your learning (professional, friendly, humorous, etc)? ')
format_instructions = """
1. A one-sentence definition
2. A simple Python code example
3. A one-sentence explanation of the code
"""

user_prompt = f"""
Explain {topic} to {audience}.

Use a {tone} tone.

Format your response with:
{format_instructions}
"""

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print('----------------------------------------------')
print('INTERACTIVE PROMPTING TOOL\n')
print(response.choices[0].message.content)