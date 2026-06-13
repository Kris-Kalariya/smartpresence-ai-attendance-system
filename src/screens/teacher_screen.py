import streamlit as st
import os
from src.components.header import get_base64_image
from src.components.footer import footer_home
from src.ui.base_layout import background_dashboard

def teacher_screen():
    # Apply dark theme background
    background_dashboard()
    
    # Header Layout: Logo on the left, Back to Home button on the right
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "..", "logo.png")
    logo_base64 = get_base64_image(logo_path)

    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.markdown(f"""
            <div style='display: flex; align-items: center; margin-top: 5px;'>
                <img src='{logo_base64}' style='height: 40px; width: 150px; object-fit: cover; object-position: center; mix-blend-mode: screen;'>
            </div>
        """, unsafe_allow_html=True)
    with header_col2:
        # Styled as type="secondary" to make it Pink
        if st.button("Go back to Home ↗", type="secondary", key="back_home"):
            st.session_state['login_type'] = None
            st.rerun()

    # Page Title in Bungee Font
    st.markdown("""
        <h3 style="
            font-family: 'Bungee', sans-serif !important; 
            font-size: 2rem; 
            color: #FFFFFF; 
            text-align: center; 
            margin: 30px 0;
            text-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        ">
            Register your teacher profile
        </h3>
    """, unsafe_allow_html=True)

    # Form Container Columns (Centers the form card on the page)
    form_col_left, form_col, form_col_right = st.columns([1, 4, 1])
    
    with form_col:
        # Username Field
        st.text_input("Enter username", placeholder="@username", key="teacher_username")
        
        # Name Field
        st.text_input("Enter name", placeholder="Enter your full name", key="teacher_name")
        
        # Password Field
        st.text_input("Enter password", type="password", placeholder="Enter your password", key="teacher_password")
        
        # Confirm Password Field
        st.text_input("Confirm password", type="password", placeholder="Confirm your password", key="teacher_confirm_password")
        
        # Spacer
        st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)
        
        # Action Buttons Row
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            # Primary (blue) Register button
            if st.button("👤 Register Now", type="primary", use_container_width=True, key="teacher_register"):
                st.success("Registration mockup submitted!")
        with btn_col2:
            # Secondary (pink) Login button
            if st.button("👥 Login instead", type="secondary", use_container_width=True, key="teacher_login"):
                pass

    footer_home()