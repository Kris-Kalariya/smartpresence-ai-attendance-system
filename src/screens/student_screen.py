import streamlit as st
import os
from src.components.header import get_base64_image
from src.components.footer import footer_home
from src.ui.base_layout import background_dashboard
from PIL import Image
import numpy as np

def student_screen():

    # Apply dark theme background class hook (triggers CSS rules for dashboards)
    background_dashboard()
    
    # Header Layout: Logo on the left, Back to Home button on the right
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "..", "logo.png")
    logo_base64 = get_base64_image(logo_path)

    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.markdown(f"""
            <div class="dashboard-logo-container">
                <img src="{logo_base64}" class="dashboard-logo">
            </div>
        """, unsafe_allow_html=True)
    with header_col2:
        # Styled as type="secondary" to make it Pink
        if st.button("Go back to Home ↗", type="secondary", key="back_home"):
            st.session_state['login_type'] = None
            st.rerun()

    st.markdown(f"""
        <h3 class="dashboard-title">
            Login using FaceID
        </h3>
    """, unsafe_allow_html=True)

    photo_source = st.camera_input("Position your face in the center")
    
    if photo_source:
        np.array(Image.open(photo_source))

    footer_home()