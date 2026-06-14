import streamlit as st
import os
from src.components.header import get_base64_image
from src.components.footer import footer_home
from src.ui.base_layout import background_dashboard
from src.database.database import check_teacher_exist, register_teacher, login_teacher

def register_teacher_ui(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All fields are required"
    if check_teacher_exist(teacher_username):
        return False, "Username already taken"
    if teacher_pass != teacher_pass_confirm:
        return False, "Password doesn't match"
    
    try:
        register_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Successfully created! Login now"
    except Exception as e:
        return False, "Unexpected Error!"


def login_teacher_ui(username, password):
    if not username or not password:
        return False
    
    teacher = login_teacher(username, password)
    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    
    return False


def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    st.header(f"""
        Welcome, {teacher_data['name']}""")



def teacher_screen_register():
    # Initialize the teacher mode state if it doesn't exist
    if 'teacher_data' in st.session_state:
        teacher_dashboard()
        return
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
            teacher_login_username = st.text_input("Enter username", placeholder="@username")
            
            # Password Field
            teacher_login_pass = st.text_input("Enter password", type="password", placeholder="Enter your password")
            
            # Spacer
            st.markdown('<div class="form-spacer"></div>', unsafe_allow_html=True)
            
            # Action Buttons Row
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                # Primary (blue) Login button
                if st.button("🔑 Login Now", type="primary", use_container_width=True, key="teacher_login_btn"):
                    if login_teacher_ui(teacher_login_username, teacher_login_pass):
                        st.toast('Welcome Back!', icon='👋')
                        import time
                        time.sleep(2)
                        st.rerun()
                    else:
                        st.error("Invalid username or password")
            with btn_col2:
                # Secondary (pink) Register switch button
                if st.button("👤 Register instead", type="secondary", use_container_width=True, key="teacher_register_switch"):
                    st.session_state['teacher_mode'] = 'register'
                    st.rerun()

        # Dynamic Form State: Register Mode
        else:
            # Username Field
            teacher_username = st.text_input("Enter username", placeholder="@username")
            
            # Name Field
            teacher_name = st.text_input("Enter name", placeholder="Enter your full name")
            
            # Password Field
            teacher_pass = st.text_input("Enter password", type="password", placeholder="Enter your password")
            
            # Confirm Password Field
            teacher_pass_confirm = st.text_input("Confirm password", type="password", placeholder="Confirm your password")
            
            # Spacer
            st.markdown('<div class="form-spacer"></div>', unsafe_allow_html=True)
            
            # Action Buttons Row
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                # Primary (blue) Register button
                if st.button("👤 Register Now", type="primary", use_container_width=True, key="teacher_register_btn"):
                    success, message = register_teacher_ui(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
                    if success:
                        st.success(message)
                        import time
                        time.sleep(2)
                        st.session_state.teacher_mode = "login"
                        st.rerun()
                    else:
                        st.error(message)
            with btn_col2:
                # Secondary (pink) Login switch button
                if st.button("🔑 Login instead", type="secondary", use_container_width=True, key="teacher_login_switch"):
                    st.session_state['teacher_mode'] = 'login'
                    st.rerun()

    footer_home()