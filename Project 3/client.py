from openai import OpenAI

client = OpenAI(
    api_key = "your api key"
)

from openai import OpenAI

client = OpenAI(
  api_key="your api key"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "you are a virtual assistant Jarvis, skilled in general tasks like alexa and google assistant"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message);

