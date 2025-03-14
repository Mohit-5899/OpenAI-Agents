import os
from dotenv import load_dotenv
from openai import OpenAI
from agents import Agent, function_tool, Runner

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Define a tool to get weather information
@function_tool
def get_weather(city: str) -> str:
    # Placeholder implementation
    return f"The weather in {city} is sunny."

# Create an agent with the weather tool
agent = Agent(
    name="WeatherAgent",
    instructions="Provide current weather information for a given city.",
    model="gpt-4o",
    tools=[get_weather],
)

# Function to run the agent with a given input
def run_agent(input_text: str):
    result = Runner.run_sync(agent, input_text)
    return result.final_output

# Example usage
if __name__ == "__main__":
    city_name = "Mumbai"
    weather_info = run_agent(f"What is the weather in {city_name}?")
    print(weather_info)
