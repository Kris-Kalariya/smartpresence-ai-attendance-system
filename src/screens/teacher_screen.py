import streamlit as st
import os
from src.components.header import get_base64_image
from src.components.footer import footer_home
from src.ui.base_layout import background_dashboard

def teacher_screen():
    # Initialize the teacher mode state if it doesn't exist
    if 'teacher_mode' not in st.session_state:
        st.session_state['teacher_mode'] = 'login'

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

    # 1. Determine Title based on active mode
    if st.session_state['teacher_mode'] == 'login':
        title_text = "Login to your teacher profile"
    else:
        title_text = "Register your teacher profile"

    # 2. Render Title (called BEFORE st.columns, so it renders above the form container)
    st.markdown(f"""
        <h3 class="dashboard-title">
            {title_text}
        </h3>
    """, unsafe_allow_html=True)

    # 3. Form Container Columns (Centers the form card on the page)
    form_col_left, form_col, form_col_right = st.columns([1, 4, 1])

    with form_col:
        # Dynamic Form State: Login Mode
        if st.session_state['teacher_mode'] == 'login':
            # Username Field
            st.text_input("Enter username", placeholder="@username", key="teacher_login_username")
            
            # Password Field
            st.text_input("Enter password", type="password", placeholder="Enter your password", key="teacher_login_password")
            
            # Spacer
            st.markdown('<div class="form-spacer"></div>', unsafe_allow_html=True)
            
            # Action Buttons Row
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                # Primary (blue) Login button
                if st.button("🔑 Login Now", type="primary", use_container_width=True, key="teacher_login_btn"):
                    st.success("Login mockup submitted!")
            with btn_col2:
                # Secondary (pink) Register switch button
                if st.button("👤 Register instead", type="secondary", use_container_width=True, key="teacher_register_switch"):
                    st.session_state['teacher_mode'] = 'register'
                    st.rerun()

        # Dynamic Form State: Register Mode
        else:
            # Username Field
            st.text_input("Enter username", placeholder="@username", key="teacher_register_username")
            
            # Name Field
            st.text_input("Enter name", placeholder="Enter your full name", key="teacher_register_name")
            
            # Password Field
            st.text_input("Enter password", type="password", placeholder="Enter your password", key="teacher_register_password")
            
            # Confirm Password Field
            st.text_input("Confirm password", type="password", placeholder="Confirm your password", key="teacher_register_confirm_password")
            
            # Spacer
            st.markdown('<div class="form-spacer"></div>', unsafe_allow_html=True)
            
            # Action Buttons Row
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                # Primary (blue) Register button
                if st.button("👤 Register Now", type="primary", use_container_width=True, key="teacher_register_btn"):
                    st.success("Registration mockup submitted!")
            with btn_col2:
                # Secondary (pink) Login switch button
                if st.button("🔑 Login instead", type="secondary", use_container_width=True, key="teacher_login_switch"):
                    st.session_state['teacher_mode'] = 'login'
                    st.rerun()

    footer_home()