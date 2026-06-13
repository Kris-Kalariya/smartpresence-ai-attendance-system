import streamlit as st
import os
from src.components.header import header_home, get_base64_image
from src.components.footer import footer_home
from src.ui.base_layout import background_home

def home_screen():
    background_home()
    header_home()
    
    # 2 columns for Student and Teacher portals
    col1, col2 = st.columns(2)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # --- Student Card (Column 1) ---
    with col1:
        st.markdown("""
            <div class="card-title-container">
                <h3 class="card-title">I'm Student</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Load and display Student image
        student_path = os.path.join(current_dir, "..", "student.png")
        student_base64 = get_base64_image(student_path)
        
        st.markdown(f"""
            <div class="card-image-container">
                <img src="{student_base64}" class="card-image">
            </div>
        """, unsafe_allow_html=True)

        if st.button('Student Portal ↗', key='btn_student'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    # --- Teacher Card (Column 2) ---
    with col2:
        st.markdown("""
            <div class="card-title-container">
                <h3 class="card-title">I'm Teacher</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Load and display Teacher image
        teacher_path = os.path.join(current_dir, "..", "teacher.png")
        teacher_base64 = get_base64_image(teacher_path)
        
        st.markdown(f"""
            <div class="card-image-container">
                <img src="{teacher_base64}" class="card-image">
            </div>
        """, unsafe_allow_html=True)

        if st.button('Teacher Portal ↗', key='btn_teacher'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()