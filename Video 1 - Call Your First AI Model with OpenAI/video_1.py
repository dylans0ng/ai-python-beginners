from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai = OpenAI()

# --------------
# BASIC API CALL
# --------------
system_prompt = 'You are an expert Python developer that is providing assistant to beginners learning programming for the first time.'
user_prompt = 'Explain what a Python variable is in one sentence.'

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print(response.choices[0].message.content)

# -----------------------------------
# LANDING PAGE CONTENT IDEA GENERATOR
# -----------------------------------
product_name = input("\nProduct name: ")
target_audience = input("Target audience: ")
main_problem = input("Main problem this product solves: ")
main_benefit = input("Main benefit of the product: ")
tone = input("Tone of the landing page: ")

system_prompt = """
You are a landing page copywriting assistant.

Your job is to help beginners create clear and persuasive landing page content.

For every request, generate:
1. A hero headline
2. A short subheadline
3. Three key benefits
4. Three feature bullets
5. One call-to-action button
6. Three FAQ questions and answers

Keep the writing simple, specific, and beginner-friendly.
Avoid sounding too salesy or exaggerated.
"""

user_prompt = f"""
Generate landing page content for this product:

Product name: {product_name}
Target audience: {target_audience}
Main problem: {main_problem}
Main benefit: {main_benefit}
Tone: {tone}
"""

response = openai.chat.completions.create(
    model='gpt-4.1-mini',
    messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}]
)

print(response.choices[0].message.content)
