import streamlit as st
from PIL import Image

def second_screen():
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
    
    st.title("Choose Your Device")

    # Define images for devices
    router_img = Image.open("screens/assets/router.jpg")
    switch_img = Image.open("screens/assets/switches.jpg")
    server_img = Image.open("screens/assets/server.jpeg")

    # Display images and use st.radio to allow selecting only one device
    device_options = {
        "Router": router_img,
        "Switch": switch_img,
        "Server": server_img
    }
    
    # Show the device images as radio options
    selected_device = st.radio(
        "Select a device to configure:", 
        options=list(device_options.keys()),  # Radio options: Router, Switch, Server
        format_func=lambda device: f"{device}"
    )

    # Show the selected device's image below the radio buttons
    st.image(device_options[selected_device], caption=selected_device, width=200)

    # Conditional display for "Router" selection
    if selected_device == "Router":
        # Show router company options
        company = st.selectbox(
            "Select the router company:",
            ["Cisco", "Huawei", "TP-Link"]
        )
        
        # Proceed button for Router
        if st.button("Proceed"):
            st.session_state['device_selected'] = selected_device
            st.session_state['company_selected'] = company
            st.session_state['screen'] = 'device_questions'
    
    # Display message for other devices
    else:
        st.warning(f"{selected_device} configuration is coming in the next release!")
