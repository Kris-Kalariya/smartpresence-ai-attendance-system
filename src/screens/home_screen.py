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
        # Clean centered Bungee title (smaller size)
        st.markdown("""
            <div style="width: 100%; text-align: center;">
                <h3 style="
                    font-family: 'Bungee', sans-serif !important; 
                    font-size: 1.20rem; 
                    color: #FFFFFF; 
                    margin: 0;
                ">
                    I'm Student
                </h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Load and display Student image (smaller circle dimensions)
        student_path = os.path.join(current_dir, "..", "student.png")
        student_base64 = get_base64_image(student_path)
        
        st.markdown(f"""
            <div style="display: flex; justify-content: center; width: 100%;">
                <img src="{student_base64}" style="
                    height: 100px; 
                    width: 100px; 
                    object-fit: cover; 
                    border-radius: 50%; 
                    border: 2px solid rgba(255, 255, 255, 0.2);
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
                ">
            </div>
        """, unsafe_allow_html=True)

        if st.button('Student Portal ↗', key='btn_student'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    # --- Teacher Card (Column 2) ---
    with col2:
        # Clean centered Bungee title (smaller size)
        st.markdown("""
            <div style="width: 100%; text-align: center;">
                <h3 style="
                    font-family: 'Bungee', sans-serif !important; 
                    font-size: 1.20rem; 
                    color: #FFFFFF; 
                    margin: 0;
                ">
                    I'm Teacher
                </h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Load and display Teacher image (smaller circle dimensions)
        teacher_path = os.path.join(current_dir, "..", "teacher.png")
        teacher_base64 = get_base64_image(teacher_path)
        
        st.markdown(f"""
            <div style="display: flex; justify-content: center; width: 100%;">
                <img src="{teacher_base64}" style="
                    height: 100px; 
                    width: 100px; 
                    object-fit: cover; 
                    border-radius: 50%; 
                    border: 2px solid rgba(255, 255, 255, 0.2);
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
                ">
            </div>
        """, unsafe_allow_html=True)

        if st.button('Teacher Portal ↗', key='btn_teacher'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()