from openai import OpenAI
from dotenv import load_dotenv
import os
import gradio as gr

# Load environment variables (API Key)
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(prompt):
    """Generate a response using OpenAI's API based on the user's prompt"""
    response = client.responses.create(
        model="gpt-4o",
        input=prompt
    )
    return response.output_text

# Create Gradio interface
with gr.Blocks(title="OpenAI Response Generator") as demo:
    gr.Markdown("# OpenAI Response Generator")
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="Enter your prompt",
                placeholder="write a Meal plan for week?",
                lines=5
            )
            submit_btn = gr.Button("Generate Response")
        with gr.Column():
            output_text = gr.Textbox(
                label="Generated Response",
                lines=10
            )
    
    submit_btn.click(
        fn=generate_response,
        inputs=input_text,
        outputs=output_text
    )

if __name__ == "__main__":
    demo.launch()
