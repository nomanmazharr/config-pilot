import os
import logging  # Added for logging
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY"),
#     base_url=os.getenv("OPENAI_API_BASE")  # Uncomment if using a custom base URL
# )

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

# Set up logging
logging.basicConfig(level=logging.ERROR)

# Function to get GPT-4o Mini response
def get_gpt4o_mini_response(user_input):
    try:
        # Retrieve stored device and company info from session state
        device = st.session_state.get('device_selected', None)
        company = st.session_state.get('company_selected', None)

        # Classify the type of user input (greeting, technical query, or unclear)
        intent = classify_intent(user_input)

        # If device or company info is missing, prompt the user to provide them
        if not device or not company:
            return handle_missing_info(device, company)

        # Build a dynamic prompt based on provided context
        system_prompt = f"""
        You are a technical assistant specializing in networking devices like routers, switches, and servers.
        You help users configure their devices and troubleshoot issues.
        The user is working with a {device or 'network device'}, from a company that may be new or less common: {company or 'an unspecified company'}.
        Always start by acknowledging the user's greeting if present and responding to it in a friendly manner.
        If the user has any issues related to network configurations, analyze the problem and provide relevant steps to solve it.
        If the user asks about topics outside of network configurations, inform them that you specialize in networking and invite them to ask relevant questions.
        If the input is unclear, ask clarifying questions to help the user more effectively.
        """

        user_query = f"""
         "{user_input}"
        """

        # Call the OpenAI API to generate a response
        response = client.chat.completions.create(
            # model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
            model="llama-3.2-3b-preview",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query},
            ],
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
    
    # Add more sophisticated checks for technical or general questions
    if "configure" in user_input.lower() or "issue" in user_input.lower() or "network" in user_input.lower():
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
