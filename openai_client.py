import os
import logging  # Added for logging
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")  # Uncomment if using a custom base URL
)

# Set up logging
logging.basicConfig(level=logging.ERROR)

# Function to get GPT-4o Mini response
def get_gpt4o_mini_response(prompt, max_tokens=100):
    try:
        greetings = ["hi", "hello", "hey", "greetings", "good morning", "good evening"]
        
        if any(greet in prompt.lower() for greet in greetings):
            # Return a friendly greeting if the user's input is casual
            return "Hello! I'm here to help with any router configuration or networking tasks you have. How can I assist you today?"

        response = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant designed to help users configure routers efficiently and accurately."},
                {"role": "user", "content": f"I need assistance with router configuration. Specifically, {prompt}."},
            ],
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error while generating response: {e}")  # Log the actual error
        return "Sorry, an error occurred while generating your idea. Please try again later."
