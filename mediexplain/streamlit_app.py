import os
import sys

import streamlit as st

# Package root (folder that contains app/, app_synthetic/, core/, …)
_ROOT = os.path.dirname(os.path.abspath(__file__))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

st.set_page_config(page_title="MediExplain", layout="wide")

# Paths relative to this file so `streamlit run` works from any working directory
Synthetic_App = st.Page(
    os.path.join(_ROOT, "app_synthetic", "synthetic_app.py"),
    title="Synthetic App",
)

chat_app = st.Page(
    os.path.join(_ROOT, "app_synthetic", "chat_app.py"),
    title="MediExplain Chatbot",
)

validator_app = st.Page(
    os.path.join(_ROOT, "app_synthetic", "validator", "validator_app.py"),
    title="Validator Console",
)

pages = {
    "Home": [
        Synthetic_App,
        chat_app,
        validator_app,
    ]
}

st.navigation(pages).run()
