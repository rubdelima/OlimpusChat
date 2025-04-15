import streamlit as st
from app_utils.meet_gods_texts import get_text

if 'language' not in st.session_state:
    st.session_state.language = "Português(BR)"

title, content = get_text(st.session_state.language)

st.set_page_config(page_title=title, layout="centered", initial_sidebar_state="collapsed", page_icon="./images/olimpus_logo.png")

st.title(f"🔍 {title}")

st.markdown(content)

from lib.gods import gods_dict, gods_list

gods_tabs = st.tabs(gods_dict.keys())

for i, tab in enumerate(gods_tabs):
    god = gods_list[i]
    
    tab.subheader(god.name)
    
    cg1, cg2, cg3 = tab.columns([1, 2, 1])
    
    cg2.image(god.image, use_container_width=True)
    
    tab.markdown(
        god.background_pt if st.session_state.language == "Português(BR)"
        else god.background_en
    )

