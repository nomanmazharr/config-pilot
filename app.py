import streamlit as st
from screens.Home import first_screen
from screens.devices import second_screen
from screens.chatbot import third_screen

# Initialize session state to track navigation and device selection
if 'screen' not in st.session_state:
    st.session_state['screen'] = 'intro'

if 'device_selected' not in st.session_state:
    st.session_state['device_selected'] = None

# Navigation logic between screens
if st.session_state['screen'] == 'intro':
    first_screen()
elif st.session_state['screen'] == 'device_selection':
    second_screen()
elif st.session_state['screen'] == 'device_questions':
    third_screen()
