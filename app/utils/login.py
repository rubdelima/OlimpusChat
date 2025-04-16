import streamlit as st
from lib.models import UserBase, User
from lib.firebase import firestore

if 'user_logged_in' not in st.session_state:
    st.session_state.user_logged_in = False
    st.session_state.user = None

@st.dialog("Login")
def show_login_signup():
    with st.form(key="login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            try:
                user = firestore.get_user(email, password)
                st.session_state.user_logged_in = True
                st.session_state.user = user
                st.success("Login successful!")
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {str(e)}")

@st.dialog("Sign up")
def show_signup():
    with st.form(key="signup_form"):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        google_api_key = st.text_input("Google API Key", type="password")
        
        submit_button = st.form_submit_button("Sign Up")
        
        if submit_button:
            user_base = UserBase(username=username, email=email, password=password, google_api_key=google_api_key)
            try:
                new_user = firestore.add_user(user_base)
                st.session_state.user_logged_in = True
                st.session_state.user = new_user
                st.success("Cadastro e login bem-sucedidos!")
                st.rerun()
            except Exception as e:
                st.error(f"Erro: {str(e)}")

def logout():
    st.session_state.update({"user_logged_in": False, "user" : None})
    st.rerun()
                            
def setup():
    # print(f"User: {st.session_state.user}")
    st.sidebar.subheader(f"Bem vindo, {st.session_state.user.username}" if st.session_state.user_logged_in
                 else "Faça o Login")
    
    bt1, bt2 = st.sidebar.columns(2)
    
    if st.session_state.user_logged_in:
        
        bt1.button("Logout",use_container_width=True,  on_click=logout)
        bt2.button("Configurações",use_container_width=True,  on_click=lambda: st.session_state.update({"settings": True}))
    
    else:
        bt1.button("Login",use_container_width=True,  on_click=show_login_signup)
        bt2.button("Sign Up",use_container_width=True,  on_click=show_signup)