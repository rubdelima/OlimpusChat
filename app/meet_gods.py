import streamlit as st
from app.utils.meet_gods_texts import get_text
from lib.gods import gods_dict, gods_list
from app.utils.user_preferences import initialize_preferences, refresh_cookies

initialize_preferences()
refresh_cookies()

if 'language' not in st.session_state:
    st.session_state.language = "Português(BR)"

title, content = get_text(st.session_state.language)

st.title(f"🔍 {title}")

st.markdown(content)


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

