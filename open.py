import openai
from openai import OpenAI

# openai.api_key = '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' # adding to the code for now

client = OpenAI(api_key="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") # setting locally

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)