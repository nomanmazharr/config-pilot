import streamlit as st
from openai_client import get_gpt4o_mini_response  # Import the OpenAI function

def third_screen():
    device = st.session_state['device_selected']
    st.title(f"Configure Your {device}")
    
    # Ask user-specific questions based on the device selected
    issue = st.text_input(f"What issue are you facing with your {device}?")
    config_type = st.selectbox("Do you need basic or advanced configurations?", ["Basic", "Advanced"])
    
    if st.button("Submit"):
        # Prepare the prompt for the model
        prompt = (f"I am trying to configure a {device}. "
                  f"I am facing the following issue: {issue}. "
                  f"I require {config_type.lower()} configurations. "
                  f"Please analyze the situation thoroughly and suggest effective troubleshooting steps or best practices that could help resolve the issue. "
                  f"Consider potential causes and solutions, and provide detailed explanations or recommendations.")

        # Get response from the model
        response = get_gpt4o_mini_response(prompt)
        
        # Display the model's response
        st.write("### AI Response:")
        st.write(response)

        # Optionally allow user to refine the input for more tailored results
        if st.button("Refine Input"):
            st.session_state['screen'] = 'device_questions'  # Go back to previous screen to refine
