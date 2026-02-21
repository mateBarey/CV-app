import streamlit as st
import time

# Hide the Streamlit header/footer
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# JavaScript redirect (stronger than meta)
st.markdown("""
    <script>
        window.location.replace("https://cubas.dev");
    </script>
""", unsafe_allow_html=True)

# Fallback message
st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <h3>Redirecting to <a href="https://cubas.dev">cubas.dev</a>...</h3>
        <p>Click the link if not redirected automatically.</p>
    </div>
""", unsafe_allow_html=True)

# Wait then force redirect via Python too
time.sleep(2)
st.switch_page("https://cubas.dev")  # This won't work but trying anyway
