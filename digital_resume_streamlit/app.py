import streamlit as st
from streamlit_redirect import redirect

# Hide Streamlit junk
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Redirect immediately
redirect("https://cubas.dev")

# This line never runs but keeps Streamlit happy
st.write("Redirecting...")
