import streamlit as st
from lib.models import Chat
from lib.gods import gods_dict, gods_list
import ollama

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

god1_col = st.columns(4, vertical_alignment="bottom")
god1_name = god1_col[0].selectbox("Selecione o deus 1:", options=list(gods_dict.keys()))
god_info(god1_col[1], god1_name)
god1_type = god1_col[2].selectbox("Selecione o tipo 1", options=models_type.keys())
god1_model = god1_col[3].selectbox("Selecione o modelo 1", options=models_type.get(god1_type, [])) # type:ignore
god1_idea = st.text_input("Insira o Pensamento do Deus 1")

st.divider()

god2_col = st.columns(4, vertical_alignment="bottom")
god2_name = god2_col[0].selectbox("Selecione o deus 2:", options=list(gods_dict.keys()))
god_info(god2_col[1], god2_name)
god2_type = god2_col[2].selectbox("Selecione o tipo 2", options=models_type.keys())
god2_model = god2_col[3].selectbox("Selecione o modelo 2", options=models_type.get(god1_type, [])) # type:ignore
god2_idea = st.text_input("Insira o Pensamento do Deus 2")

st.divider()

st.button("Iniciar Chat")