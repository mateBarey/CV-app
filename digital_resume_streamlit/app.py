import streamlit as st

# Hide Streamlit garbage
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp { background: white; }
    </style>
""", unsafe_allow_html=True)

# JavaScript redirect (this actually works)
st.markdown("""
    <script>
        window.location.href = "https://cubas.dev";
    </script>
""", unsafe_allow_html=True)

# Fallback message
st.markdown("""
    <div style="text-align: center; margin-top: 50px; font-family: sans-serif;">
        <h2>Redirecting to <a href="https://cubas.dev">cubas.dev</a>...</h2>
        <p>Click the link if not redirected automatically.</p>
    </div>
""", unsafe_allow_html=True)
