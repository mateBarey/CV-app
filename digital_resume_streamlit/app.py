import streamlit as st

# Hide Streamlit's default UI
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp { background: white; }
    </style>
""", unsafe_allow_html=True)

# This actually works - components.html renders real HTML
st.components.v1.html("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="refresh" content="0; url='https://cubas.dev'" />
    </head>
    <body>
        <p>Redirecting to <a href="https://cubas.dev">cubas.dev</a>...</p>
    </body>
    </html>
""", height=100)
