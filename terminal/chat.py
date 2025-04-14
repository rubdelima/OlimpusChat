import json
import random
import traceback
from langchain_core.messages import SystemMessage, HumanMessage
from lib.models import GlobalModel
from terminal.build_context import build_context_pt
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def chat(
    god1:GlobalModel,
    god2:GlobalModel,
    jury_dict:dict[str, GlobalModel],
    supervisioned:bool,
    rounds:int,
    prompts:tuple[str],
    file:str="",
    file_type:str="txt",
    
):
    jury_ask_prompt, first_message_prompt, \
        second_message_prompt, last_message_prompt, jury_verdict_prompt, \
            select_god, sys_god, god_not_found = prompts # type:ignore
    
    all_messages = []
    
    gods_avaliabes = WordCompleter(list(jury_dict.keys()), ignore_case=True)
    
    for round in range(rounds):
        try:
            while True:
                
                jury_select = prompt(select_god, completer=gods_avaliabes) \
                    if supervisioned else random.choice(list(jury_dict.keys()))
                
                jury_info = input(sys_god) \
                    if supervisioned else ""

            
                if jury_select in jury_dict.keys():
                    break
                print(god_not_found)

            jury_dict[jury_select].messages.append(SystemMessage(content=jury_ask_prompt.format(text=jury_info)))
            jury_response = jury_dict[jury_select].chat()
            all_messages.append({jury_select: jury_response})

            for jury in jury_dict.values():
                jury.messages.append(HumanMessage(content=f"Jury: {jury_select} Ask: {jury_response}"))

            god1.messages.append(HumanMessage(content=f"{jury_select}: {jury_response}"))
            god2.messages.append(HumanMessage(content=f"{jury_select}: {jury_response}"))

            round_god1 = god1 if round % 2 == 0 else god2
            round_god2 = god2 if round % 2 == 0 else god1

            round_god1.messages.append(SystemMessage(content=first_message_prompt))
            round_god1_response = round_god1.chat()
            round_god2.messages.append(HumanMessage(content=f"{round_god1.user_name}: {round_god1_response}"))
            all_messages.append({round_god1.user_name: round_god1_response})

            round_god2.messages.append(SystemMessage(content=second_message_prompt))
            round_god2_response = round_god2.chat()
            round_god1.messages.append(HumanMessage(content=f"{round_god2.user_name}: {round_god2_response}"))
            all_messages.append({round_god2.user_name: round_god2_response})            

            for jury in jury_dict.values():
                jury.messages.append(HumanMessage(content=f"{round_god1.user_name}: {round_god1_response}"))
                jury.messages.append(HumanMessage(content=f"{round_god2.user_name}: {round_god2_response}"))

        except Exception as e:
            print(traceback.format_exc())
            continue
        
    god1.messages.append(SystemMessage(content=last_message_prompt))
    god1_response = god1.chat()
    all_messages.append({god1.user_name: god1_response})

    god2.messages.append(SystemMessage(content=last_message_prompt))
    god2_response = god2.chat()
    all_messages.append({god2.user_name: god2_response})

    for jury in jury_dict.values():
        jury.messages.append(HumanMessage(content=f"{god1.user_name}: {god1_response}"))
        jury.messages.append(HumanMessage(content=f"{god2.user_name}: {god2_response}"))
        jury.messages.append(SystemMessage(content=jury_verdict_prompt))
        jury_response = jury.chat()

        all_messages.append({jury.user_name: jury_response})

    if file:
        if file_type == "txt":
            with open(file, "w", encoding='utf-8') as f:
                for message in all_messages:
                    for key, value in message.items():
                        f.write(f"{key}: {value}\n")
        elif file_type == "json":
            with open(file, "w", encoding='utf-8') as f:
                json.dump(all_messages, f, indent=4, ensure_ascii=False)
        elif file_type == "md":
            with open(file, "w", encoding='utf-8') as f:
                for message in all_messages:
                    for key, value in message.items():
                        f.write(f"**{key}**: {value}\n\n")
