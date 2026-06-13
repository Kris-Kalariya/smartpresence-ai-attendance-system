import streamlit as st
import base64
import os

def get_base64_image(image_path):
    """Converts a local image to a Base64 string so it can be used inside HTML."""
    try:
        with open(image_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            return f"data:image/png;base64,{encoded}"
    except FileNotFoundError:
        return ""

def header_home():
    current_dir = os.path.dirname(os.path.abspath(__file__)) # src/components/
    logo_path = os.path.join(current_dir, "..", "logo.png")   # src/logo.png
    
    # Convert to Base64
    logo_base64 = get_base64_image(logo_path)

    # Uses object-fit: cover to crop the top/bottom blank spaces inside the image file
    st.markdown(f"""
        <div class="header-logo-container">
            <img src="{logo_base64}" class="header-logo">
        </div>
    """, unsafe_allow_html=True)