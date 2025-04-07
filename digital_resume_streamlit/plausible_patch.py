import os
import streamlit as st

def patch_plausible():
    index_path = os.path.join(os.path.dirname(st.__file__), "static", "index.html")
    backup_path = index_path + ".original"
    script_tag = """
    <script defer data-domain="digital-resume-ms4l.onrender.com" src="https://plausible.io/js/script.js"></script>
    """

    if not os.path.exists(backup_path):
        with open(index_path, "r", encoding="utf-8") as f:
            original = f.read()
        with open(backup_path, "w", encoding="utf-8") as f:
            f.write(original)

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    if script_tag not in html:
        patched = html.replace("<head>", f"<head>\n{script_tag}")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(patched)
        print("✅ Patched Plausible into Streamlit head.")
    else:
        print("ℹ️ Already patched.")
