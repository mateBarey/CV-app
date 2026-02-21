import streamlit as st

# Override everything
st.markdown("""
    <style>
        .stApp { background: white; margin: 0; padding: 0; }
        .main { margin: 0; padding: 0; }
        .block-container { margin: 0; padding: 0; max-width: 100%; }
        iframe { width: 100vw; height: 100vh; border: none; }
    </style>
""", unsafe_allow_html=True)

# Full-screen iframe that redirects
st.components.v1.html("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="refresh" content="0; url='https://cubas.dev'" />
    </head>
    <body style="margin:0; padding:0; background:white;">
        <p style="font-family:sans-serif; text-align:center; margin-top:40vh;">
            Redirecting to <a href="https://cubas.dev">cubas.dev</a>...
        </p>
    </body>
    </html>
""", height=1000)
