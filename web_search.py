from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables (API Key)
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Perform a web search
response = client.responses.create(
    model="gpt-4o",
    tools=[{"type":"web_search_preview"}],
    input="tell me about quanta AI labs by Mohit mandawat?"
)               

print(response.output_text)
