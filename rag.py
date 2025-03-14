from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables (API Key)
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Perform a web search
response = client.responses.create(
    model="gpt-4o",
    input="Tell me about quanta ai labs",
    tools=[{
        "type":"file_search",
        "vector_store_ids":["vs_67d27996a5f08191aa2410db1dbacfe6"],
        }],
)               

print(response.output_text)