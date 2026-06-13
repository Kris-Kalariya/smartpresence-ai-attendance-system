import streamlit as st

def background_home():
    """Sets the dark gradient background, centers the cards, and disables vertical scrolling."""
    st.markdown("""
        <style>
            /* Disable vertical scrollbar on the home screen */
            .stApp {
                background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 100%) !important;
                overflow: hidden !important;
                height: 100vh !important;
            }
            
            /* Center the entire columns block horizontally and space it tightly */
            div[data-testid="stHorizontalBlock"] {
                display: flex !important;
                justify-content: center !important;
                gap: 30px !important; /* Space between the two cards */
                max-width: 560px !important; /* Caps the block size to fit 2 small cards */
                margin: 10px auto 0 auto !important; /* Tight top margin */
            }
            
            /* Styles the columns as compact centered cards */
            div[data-testid="stColumn"] {
                background: rgba(30, 41, 59, 0.45) !important; 
                backdrop-filter: blur(10px) !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                border-radius: 20px !important;
                padding: 20px !important; /* Tighter padding */
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3) !important;
                transition: all 0.3s ease-in-out !important;
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                justify-content: center !important;
                min-height: 270px !important; /* Compact card height */
                max-width: 240px !important;  /* Compact width */
                margin: 0 auto !important;
            }
            
            /* Card hover animation */
            div[data-testid="stColumn"]:hover {
                transform: translateY(-4px) !important;
                background: rgba(30, 41, 59, 0.6) !important;
                border-color: rgba(255, 255, 255, 0.2) !important;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4) !important;
            }
            
            /* Target any vertical block inside the column and center it */
            div[data-testid="stColumn"] [data-testid="stVerticalBlock"] {
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                justify-content: center !important;
                width: 100% !important;
                gap: 12px !important; /* Tighter spacing */
            }

            /* Target the direct children containers of the block to center their items */
            div[data-testid="stColumn"] [data-testid="stVerticalBlock"] > div {
                display: flex !important;
                justify-content: center !important;
                align-items: center !important;
                width: 100% !important;
            }
            
            /* Compact capsule buttons centered inside the cards */
            div[data-testid="stColumn"] button {
                background: #EB459E !important; /* Discord Blurple */
                border-radius: 1.5rem !important;
                padding: 6px 18px !important;
                font-size: 0.9rem !important;
                font-weight: 600 !important;
                box-shadow: 0 4px 12px rgba(88, 101, 242, 0.3) !important;
                color: white !important;
                border: none !important;
                margin: 20px auto 0 10px !important; /* Tight margin */
                width: 90% !important; 
            }
            
            div[data-testid="stColumn"] button:hover {
                transform: translateY(-2px) scale(1.03) !important;
                filter: brightness(1.15) !important;
            }
        </style>
    """, unsafe_allow_html=True)

def background_dashboard():
    """Sets a clean, dark obsidian blue background for the dashboards."""
    st.markdown("""
        <style>
            .stApp {
                background: #0B0F19 !important;
            }
        </style>
    """, unsafe_allow_html=True)

def base_layout():
    """Applies the core dark theme styling, typography, and button states."""
    st.markdown("""
        <style>
            /* Separate Font Imports (More reliable for Streamlit) */
            @import url('https://fonts.googleapis.com/css2?family=Bungee&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

            /* Hide Top toolbar & standard Streamlit branding */
            #MainMenu, footer, header {
                visibility: hidden;    
            }
            
            .block-container {
                padding-top: 0.5rem !important; /* Reduced top padding to avoid scrolling */
            }
            
            /* Text Color overrides for Dark Theme */
            h1, h2 {
                font-family: 'Bungee', sans-serif !important;
                color: #FFFFFF !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0.5rem !important;
                text-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
            }

            h3, h4, p, span, label {
                font-family: 'Poppins', sans-serif !important;
                color: #E2E8F0 !important;
            }
            
            /* Inputs Dark Style */
            div[data-baseweb="input"], div[data-baseweb="select"] {
                background-color: #1E293B !important;
                border: 1px solid #334155 !important;
                border-radius: 0.75rem !important;
            }
        </style>
    """, unsafe_allow_html=True)