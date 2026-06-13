import streamlit as st

def footer_home():
    # --- Custom Footer ---
    st.markdown("""
        <div style="
            display: flex; 
            justify-content: center; 
            align-items: center; 
            gap: 8px; 
            margin-top: 50px; 
            font-family: 'Poppins', sans-serif; 
            color: #FFFFFF; 
            font-size: 1.1rem;
            font-weight: 600;
        ">
            Created with <span style="color: #FF4B4B;">❤️</span> by 
            <span style="color: #FFC045; font-family: 'Bungee', sans-serif;">KRIS</span> 
            <span style="color: #FFFFFF; font-family: 'Bungee', sans-serif;">KALARIYA</span>
        </div>
    """, unsafe_allow_html=True)