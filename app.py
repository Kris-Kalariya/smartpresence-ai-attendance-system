import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen_register
from src.screens.student_screen import student_screen
from src.ui.base_layout import base_layout

def main():
    base_layout()

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'student':
            student_screen()

        case 'teacher':
            teacher_screen_register()
        
        case None:
            home_screen()


if __name__ == "__main__":
    main()