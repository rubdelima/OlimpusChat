import streamlit as st
from app.utils.login import setup
from app.utils.chat import render_chat
from lib.models import User

# Page Settings
st.set_page_config(page_title="OlimpusChat", layout="centered", initial_sidebar_state="collapsed", page_icon="./images/olimpus_logo.png")
st.logo("./images/olimpus_logo.png", size="large")

# Language Settings
if 'language' not in st.session_state:
    st.session_state.language = "Português(BR)"

st.session_state.language = st.sidebar.selectbox(
    "Select Language", 
    ("Português(BR)", "English"), 
    index=0 if st.session_state.language == "Português(BR)" else 1
)

# Login
setup()

# Discovery
pages = {
    "Discovery" : [
        st.Page("./app/meet_gods.py", title="Conheça os Deuses", url_path="discovery"),
        st.Page("./app/about.py", default=True, title="Sobre")
    ]
}

if st.session_state.user is not None:
    user : User = st.session_state.user
    pages["Chats"] = [
        st.Page(lambda : render_chat(chat_id), title=chat_title, icon="💬", url_path=chat_id)
        for chat_id, chat_title in user.chat_ids.items()
    ]
    pages["Chats"].insert(0, st.Page('./app/new_chat.py', title="Novo Chat", icon="💬", url_path="new_chat"))

pg = st.navigation(pages, position="hidden")

with st.sidebar:
    st.subheader("Discovery")
    st.page_link("./app/meet_gods.py", label="Conheça os Deuses", icon="🔍")
    st.page_link("./app/about.py", label="Sobre", icon="ℹ️")
    
    if "user" in st.session_state and st.session_state.user is not None:
        st.subheader("Chats")
        st.page_link("./app/new_chat.py", label="Novo Chat", icon="💬")
        for chat_id, chat_title in st.session_state.user.chat_ids.items():
            st.page_link(f"/{chat_id}", label=chat_title, icon="💬")
            
pg.run()
