import streamlit as st
from app.utils.homepage_texts import get_text

from app.utils.user_preferences import initialize_preferences, refresh_cookies

initialize_preferences()
refresh_cookies()

col1, col2, col3 = st.columns([1,2,1])

col2.image("./images/olimpus_logo.png", use_container_width=True)

st.title("OlimpusChat")

st.markdown(get_text(st.session_state.language))