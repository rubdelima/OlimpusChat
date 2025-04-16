import streamlit as st
from lib.models import Chat
from lib.gods import gods_dict, gods_list
import ollama
from app.utils.user_preferences import initialize_preferences, refresh_cookies
import uuid
from lib.firebase import firestore

initialize_preferences()
refresh_cookies()

def god_info(popover, god_name):
    with popover.popover("Info"):
        if god_name is not None:
            god = gods_dict[god_name]
            cg1, cg2, cg3 = st.columns([1, 2, 1])
    
            cg2.image(god.image, use_container_width=True)

            st.markdown(
                god.background_pt if st.session_state.language == "Português(BR)"
                else god.background_en
            )
        
try:
    ollama_models = [
        model.model for model in ollama.list().models
    ]
except:
    ollama_models = []

models_type = {
    "ollama" : ollama_models,
    "google" : ["gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-pro"]
}

st.header("💬 Novo Chat")

theme = st.text_input("Insira um tema para o debate: ")

st.divider()

god1_name, god2_name, gods = None, None, []

god1_col = st.columns(4, vertical_alignment="bottom")
god1_type = god1_col[0].selectbox("Selecione o tipo 1", options=models_type.keys())
god1_model = god1_col[1].selectbox("Selecione o modelo 1", options=models_type.get(god1_type, [])) # type:ignore
god1_name = god1_col[2].selectbox("Selecione o deus 1:", options=set(gods_dict.keys()) - ({god2_name} | set(gods)))
god_info(god1_col[3], god1_name)
god1_idea = st.text_input("Insira o Pensamento do Deus 1")

st.divider()

god2_col = st.columns(4, vertical_alignment="bottom")
god2_type = god2_col[0].selectbox("Selecione o tipo 2", options=models_type.keys())
god2_model = god2_col[1].selectbox("Selecione o modelo 2", options=models_type.get(god2_type, [])) # type:ignore
god2_name = god2_col[2].selectbox("Selecione o deus 2:", options=list(set(gods_dict.keys())-({god1_name} | set(gods))))
god_info(god2_col[3], god2_name)
god2_idea = st.text_input("Insira o Pensamento do Deus 2")

st.divider()

gods = st.multiselect("Selecione ao menos 2 deues para serem a quantidade de jurados", options=list(set(gods_dict.keys())-{god1_name, god2_name}))
gods_col = st.columns(4, vertical_alignment="bottom")
gods_type = gods_col[0].selectbox("Selecione o tipo 3", options=models_type.keys())
gods_model = gods_col[1].selectbox("Selecione o modelo 3", options=models_type.get(gods_type, [])) # type:ignore
god2_name = gods_col[2].selectbox("Selecione um deus:", options=gods)
god_info(gods_col[3], god2_name)

# Settings Controllers
sett_cols = st.columns(2, vertical_alignment="center")
supervisioned_mode = sett_cols[0].checkbox("Modo Supervisionado")
rounds = sett_cols[1].slider("Selecione a quantidade de rounds", min_value=2, max_value=10, step=2)

def laucher_chat():
    chat = Chat(
        id = str(uuid.uuid4()), user_id= st.session_state.user.id,
        theme=theme, rounds=rounds, audio_mode=False, supervisioned=supervisioned_mode,
        god1=god1_name, god1_type=god1_type, god1_model=god1_model,god1_idea=god1_idea,
        god2=god2_name, god2_type=god2_type, god2_model=god1_model,god2_idea=god2_idea,
        gods=gods, gods_type=gods_type, gods_models=gods_model
    )
    # Adiciona o chat no usuário do session state
    st.session_state.user.chat_ids[chat.id] = chat.theme
    
    # Atualiza no banco de dados
    firestore.add_chat(st.session_state.user, chat)
    
    print(chat) #debug
    
    st.session_state.redirect_to_chat_id = chat.id
    st.rerun()
    

st.button(
    "Iniciar Chat",
    disabled= not all((
        theme,
        god1_name, god1_type, god1_model, god1_idea,
        god2_name, god2_type, god2_model, god2_idea,
        len(gods) >= 2, gods_type, gods_model
    )),
    on_click= laucher_chat
)