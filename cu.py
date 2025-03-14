from enum import auto
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables (API Key)
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Perform a web search
response = client.responses.create(
    model="computer-use-preview",
    tools=[{
        "type": "computer_use_preview",
        "display_width": 1024,
        "display_height": 768,
        "envirnment":"browser"
    }],
    input=[
        {
        "role":"user",
        "content":"Check the latest open ai blog post"
    }
    ],
    truncation="auto"
)               



print(response.output)