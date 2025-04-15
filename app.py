import streamlit as st
from app_utils.homepage_texts import get_text

# Page Settings
st.set_page_config(page_title="OlimpusChat", layout="centered", initial_sidebar_state="collapsed", page_icon="./images/olimpus_logo.png")

# Language Settings
if 'language' not in st.session_state:
    st.session_state.language = "Português(BR)"

st.session_state.language = st.sidebar.selectbox(
    "Select Language", 
    ("Português(BR)", "English"), 
    index=0 if st.session_state.language == "Português(BR)" else 1
)

# Home Page
col1, col2, col3 = st.columns([1,2,1])

col2.image("./images/olimpus_logo.png", use_container_width=True)

st.title("OlimpusChat")

st.markdown(get_text(st.session_state.language))