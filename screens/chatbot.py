import streamlit as st
from openai_client import get_gpt4o_mini_response  # Import the OpenAI function

# Function to retrieve device information
def get_device_info():
    device = st.session_state.get('device_selected', "Unknown Device")
    company = st.session_state.get('company_selected', "Unknown Company")
    return device, company

# Main chat screen
def third_screen():
    device, company = get_device_info()
    st.title(f"Configure Your {device}")

    # Introduce the chat-like interface
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display all chat messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Accept user input as a chat input
    if user_input := st.chat_input("Ask your question about the configuration..."):
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Generate response using the AI model
        prompt = (
            f"I am facing an issue with my {device} from {company}. "
            f"My query is: {user_input}. "
        )
        response = get_gpt4o_mini_response(prompt)
        
        # Add AI response to session state
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Display the AI response
        with st.chat_message("assistant"):
            st.markdown(response)
