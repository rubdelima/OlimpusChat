import streamlit as st
from lib.models import Chat

def render_chat(chat_id : str):
    st.header(chat_id)