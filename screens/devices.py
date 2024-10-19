import streamlit as st
from PIL import Image

def second_screen():
    st.image("F:\\lablab_hackathon\\Edge Runner\\screens\\assets\\logo.jpg", width=150)  # Placeholder for the logo
    
    # Menu bar
    st.markdown("""
    <div style="text-align: right;">
        <a href='#'>Routers</a> | 
        <a href='#'>Switches</a> | 
        <a href='#'>Servers</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.title("Choose Your Device")
    
    col1, col2, col3 = st.columns(3)
    
    # Router selection
    with col1:
        router_img = Image.open("F:\\lablab_hackathon\\Edge Runner\\screens\\assets\\router.jpg")
        st.image(router_img, caption="Router")
        if st.button("Select Router"):
            st.session_state['device_selected'] = "Router"
            st.session_state['screen'] = 'device_questions'
    
    # Switch selection
    with col2:
        switch_img = Image.open("F:\\lablab_hackathon\\Edge Runner\\screens\\assets\\switches.jpg")
        st.image(switch_img, caption="Switch")
        if st.button("Select Switch"):
            st.session_state['device_selected'] = "Switch"
            st.session_state['screen'] = 'device_questions'
    
    # Server selection
    with col3:
        server_img = Image.open("F:\\lablab_hackathon\\Edge Runner\\screens\\assets\\server.jpeg")
        st.image(server_img, caption="Server")
        if st.button("Select Server"):
            st.session_state['device_selected'] = "Server"
            st.session_state['screen'] = 'device_questions'
