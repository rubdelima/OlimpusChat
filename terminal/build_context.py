from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from lib.background import (
    debater_prompt_pt, debater_prompt_en, jury_prompt_pt, jury_prompt_en, 
    backgrounds_pt, backgrounds_en, jury_ask_prompt_pt, jury_ask_prompt_en,
    last_message_prompt_pt, last_message_prompt_en, jury_verdict_prompt_pt, jury_verdict_prompt_en,
    first_message_prompt_pt, first_message_prompt_en, second_message_prompt_pt, second_message_prompt_en,   
)

from lib.models import GlobalModel

def build_context_pt(
    god1:GlobalModel, 
    god2:GlobalModel, 
    gods:list[str],
    gods_type:str,
    gods_model:str, 
    gods_color:str,
    theme, idea1, idea2):
    
    jury_dict : dict[str, GlobalModel] = {}
    
    for god in gods:
        jury_dict[god] = GlobalModel(
            model_name=gods_model, 
            model_type=gods_type, 
            user_name=god, 
            messages=[],
            temperature=0.2,
            color=gods_color
        )
        
        jury_dict[god].messages.append(SystemMessage(content=jury_prompt_pt.format(
            godj_name=god, debat_topic=theme, background=backgrounds_pt.get(god, ""),
            god1_name=god1.user_name, god1_idea=idea1, 
            god2_name=god2.user_name, god2_idea=idea2,
        )))
    
    
    god1.messages = [SystemMessage(content=debater_prompt_pt.format(
        debat_topic=theme, background=backgrounds_pt.get(god1.user_name, ""),
        god1_name=god1.user_name, god1_idea=idea1,
        god2_name=god2.user_name, god2_idea=idea2,
    ))]

    god2.messages = [SystemMessage(content=debater_prompt_pt.format(
        debat_topic=theme, background=backgrounds_pt.get(god2.user_name, ""),
        god1_name=god1.user_name, god1_idea=idea1,
        god2_name=god2.user_name, god2_idea=idea2,
    ))]
    
    return god1, god2, jury_dict, (jury_ask_prompt_pt, first_message_prompt_pt,
                                   second_message_prompt_pt, last_message_prompt_pt, jury_verdict_prompt_pt,
                                   f"Escolha um deus do Juri para fazer uma pergunta: {', '.join([god.user_name for god in jury_dict.values()])} \n",
                                   "Você pode orientar o deus do juri a fazer uma pergunta específica, ou apenas apertar enter para que ele faça uma pergunta aleatória. \n",
                                   "Deus do juri não encontrado. Tente novamente.")
    
    
    