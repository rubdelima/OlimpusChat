import streamlit as st
from streamlit_cookies_controller import CookieController #type:ignore

controller = CookieController()

def initialize_preferences():
    cookies = controller.getAll()
    
    if 'language' not in st.session_state:
        saved_language = cookies.get("language")
        st.session_state.language = saved_language if saved_language else "Português(BR)"
    
    if 'user_logged_in' not in st.session_state:
        logged_in = cookies.get("logged_in") == "True"
        st.session_state.user_logged_in = logged_in
        
    if 'user' not in st.session_state and logged_in:
        user_id = cookies.get("user_id")
        if user_id:
            try:
                from lib.firebase import firestore
                st.session_state.user = firestore.get_user_by_id(user_id)
            except Exception:
                st.session_state.user = None

def refresh_cookies():
    if 'language' in st.session_state:
        controller.set("language", st.session_state.language)
    
    if st.session_state.get('user_logged_in', False):
        controller.set("logged_in", "True")
        if st.session_state.get('user') and hasattr(st.session_state.user, 'id'):
            controller.set("user_id", str(st.session_state.user.id))
    else:
        controller.set("logged_in", "False")

def language_selector():
    previous_language = st.session_state.language
    
    st.session_state.language = st.sidebar.selectbox(
        "Select Language", 
        ("Português(BR)", "English"), 
        index=0 if st.session_state.language == "Português(BR)" else 1
    )
    
    if previous_language != st.session_state.language:
        refresh_cookies()