import os
import logging  # Added for logging
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")  # Uncomment if using a custom base URL
)

# Set up logging
logging.basicConfig(level=logging.ERROR)

# Function to get GPT-4o Mini response
def get_gpt4o_mini_response(user_input, max_tokens=300):
    try:
        # Retrieve stored device and company info from session state
        device = st.session_state.get('device_selected', None)
        company = st.session_state.get('company_selected', None)

        # Classify the type of user input (greeting, technical query, or unclear)
        intent = classify_intent(user_input)

        # Handle greetings separately
        if intent == "greeting":
            return "Hello! How can I assist you today with your network configuration?"

        # If device or company info is missing, prompt the user to provide them
        if not device or not company:
            return handle_missing_info(device, company)

        # Build a dynamic prompt based on provided context
        system_prompt = f"""
        You are a technical assistant specializing in networking devices like routers, switches, and servers.
        You help users configure their devices and troubleshoot issues.
        The user is working with a {device or 'network device'}, from a company that may be new or less common: {company or 'an unspecified company'}.
        Analyze the problem and provide relevant steps to solve the issue.
        Adjust your response based on the user's input and intent.
        If the input is unclear, ask clarifying questions to help the user more effectively.
        """

        user_query = f"""
         "{user_input}"
        """

        # Call the OpenAI API to generate a response
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query},
            ],
            max_tokens=max_tokens,
        )

        if response.choices:
            return response.choices[0].message.content
        else:
            return "It seems I couldn't generate a specific response. Could you provide more details about your device or issue?"


    except Exception as e:
        logging.error(f"Error while generating response: {e}")
        return "Sorry, an error occurred while generating your response. Please try again later."

def classify_intent(user_input):
    """
    Classifies the user's intent based on their input.
    Could be 'greeting', 'technical', or 'unclear'.
    """
    greetings = ["hi", "hello", "hey", "greetings", "good morning", "good evening"]
    
    # Check if input is a greeting
    if any(greet in user_input.lower() for greet in greetings):
        return "greeting"
    
    # Add more sophisticated checks for technical or general questions
    if "configure" in user_input.lower() or "issue" in user_input.lower():
        return "technical"
    
    return "unclear"

def handle_missing_info(device, company):
    """
    Checks for missing device or company information and asks the user to provide them.
    """
    if not device:
        return "Could you please specify which device you're working with (e.g., router, switch, server)?"
    
    if not company:
        return "Could you please provide the brand of the device you're using?"

    return "Could you please specify which device and company you're working with (e.g., router, Cisco)?"
