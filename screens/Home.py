import streamlit as st

def first_screen():
    st.image("screens/assets/logo.jpg", width=150)  # Placeholder for the logo

    # Step-by-step guide (dummy data)
    st.title("How to Integrate with the App")
    steps = [
        "Step 1: Install the app on your device.",
        "Step 2: Connect the app to your router, switch, or server.",
        "Step 3: Follow the prompts for automatic configuration.",
        "Step 4: Monitor and manage your network remotely."
    ]
    
    for step in steps:
        st.write(step)

    # Dummy content for each menu item
    if st.session_state.get('screen') == 'routers':
        st.markdown("<h2>Routers</h2>", unsafe_allow_html=True)
        st.write("Information about routers goes here...")

    elif st.session_state.get('screen') == 'switches':
        st.markdown("<h2>Switches</h2>", unsafe_allow_html=True)
        st.write("Information about switches goes here...")

    elif st.session_state.get('screen') == 'servers':
        st.markdown("<h2>Servers</h2>", unsafe_allow_html=True)
        st.write("Information about servers goes here...")

    # "Let's Start" button to move to the next part of the app
    if st.button("Let's Start"):
        st.session_state['screen'] = 'device_selection'
