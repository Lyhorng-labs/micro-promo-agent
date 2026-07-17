import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)
completion= client.chat.completions.create(
    model="qwen3.7-max",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ],
)
print("REPLY:", completion.choices[0].message.content)