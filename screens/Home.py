import streamlit as st

def first_screen():
    col1, col2 = st.columns([1, 3])

    # Image in the first column
    with col1:
        st.image("screens/assets/logo.jpg", width=200)  # Placeholder for the logo

    # Text in the second column
    with col2:
        st.write("### ConfigPilot")
        st.write("**Simplify your navigation**")
        st.write(
            "ConfigPilot automates and simplifies network device configurations for routers, switches, and servers, "
            "offering step-by-step guidance for both IT professionals and non-technical users."
        )
    # Step-by-step guide (dummy data)
    st.title("Integrate with the App in Just a Few Steps")
    steps = [
        "Step 1: Navigate the type of your device.",
        "Step 2: Select the network device provider.",
        "Step 3: Ask queries to solve your problem",
        "Step 4: Monitor and manage your network efficiently."
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
