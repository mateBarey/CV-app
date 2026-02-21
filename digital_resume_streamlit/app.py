import streamlit as st

# Hide everything
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp { background: white; }
    </style>
""", unsafe_allow_html=True)

# JavaScript that breaks out of iframe
st.components.v1.html("""
    <script>
        // Break out of any iframe
        if (window.top !== window.self) {
            window.top.location.href = "https://cubas.dev";
        } else {
            window.location.href = "https://cubas.dev";
        }
    </script>
    <noscript>
        <meta http-equiv="refresh" content="0; url='https://cubas.dev'">
    </noscript>
""", height=0)
