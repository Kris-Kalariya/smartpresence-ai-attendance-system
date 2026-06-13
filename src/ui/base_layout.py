import streamlit as st
import os

def get_css_content():
    """Reads style.css content dynamically."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(current_dir, "style.css")
    try:
        with open(css_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def background_home():
    """Triggers the home screen styling by inserting the .home-container marker class."""
    st.markdown('<div class="home-container"></div>', unsafe_allow_html=True)

def background_dashboard():
    """Triggers the dashboard styling by inserting the .dashboard-container marker class."""
    st.markdown('<div class="dashboard-container"></div>', unsafe_allow_html=True)

def base_layout():
    """Reads style.css content and injects it as a global stylesheet."""
    css_content = get_css_content()
    if css_content:
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)