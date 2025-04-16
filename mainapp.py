import streamlit as st
# Page Settings
try:
    st.set_page_config(page_title="OlimpusChat", layout="centered", initial_sidebar_state="collapsed", page_icon="./images/olimpus_logo.png")
except:
    traceback.print_exc()
    pass

from app.utils.login import setup
from app.utils.chat import render_chat
import app.utils.user_preferences as preferences
import traceback

st.logo("./images/olimpus_logo.png", size="large")

# Build Sesion State, and update Cookies
preferences.initialize_preferences()
preferences.refresh_cookies()

# Language Settings
preferences.language_selector()

# Login
setup()

# Pages Settings
pages = {
    "Discovery" : [
        st.Page("./app/meet_gods.py", title="Conheça os Deuses", url_path="discovery"),
        st.Page("./app/about.py", default=True, title="Sobre")
    ]
}

chat_pages = {}

if st.session_state.user is not None:
    user = st.session_state.user
    pages["Chats"] = []
    
    for chat_id, chat_title in user.chat_ids.items():
        chat_page = st.Page(lambda : render_chat(chat_id), title=chat_title, icon="💬", url_path=f"chat_{chat_id}")
        chat_pages[chat_id] = chat_page
        pages["Chats"].append(chat_page)
    
    pages["Chats"].insert(0, st.Page('./app/new_chat.py', title="Novo Chat", icon="💬", url_path="new_chat"))

if "redirect_to_chat_id" in st.session_state and st.session_state.redirect_to_chat_id:
    chat_id = st.session_state.redirect_to_chat_id
    st.session_state.redirect_to_chat_id = None
    st.switch_page(f"chat_{chat_id}")

pg = st.navigation(pages, position="hidden")

with st.sidebar:
    st.subheader("Discovery")
    st.page_link("./app/meet_gods.py", label="Conheça os Deuses", icon="🔍")
    st.page_link("./app/about.py", label="Sobre", icon="ℹ️")
    
    if "user" in st.session_state and st.session_state.user is not None:
        st.subheader("Chats")
        st.page_link("./app/new_chat.py", label="Novo Chat", icon="💬")
        for chat_id, chat_title in st.session_state.user.chat_ids.items():
            st.page_link(chat_pages[chat_id], label=chat_title, icon="💬")
            
pg.run()
