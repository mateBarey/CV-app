import streamlit as st

# Force redirect immediately
st.set_page_config(page_title="Redirecting...")  # THIS IS NOW THE FIRST AND ONLY CALL

html = """
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url='https://cubas.dev'" />
</head>
<body>
    <p>Redirecting to <a href="https://cubas.dev">cubas.dev</a>...</p>
</body>
</html>
"""

st.components.v1.html(html, height=600)
