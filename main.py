import argparse

parser = argparse.ArgumentParser(description="Example of parameter passing")

# Args
parser.add_argument("--file", type=str, help="Name of the file to save the conversation", required=False, default="")
parser.add_argument("--file_type", type=str, help="The type of output text", required=False, choices=["txt", "json", "md"], default="txt")
parser.add_argument("--language", type=str, help="The language of the conversation", required=False, choices=["pt", "en"], default="en")
parser.add_argument("--supervisioned", type=bool, help="If the model is supervised or not", required=False, default=False)
parser.add_argument("--n_rounds", type=int, help="Number of debate rounds", required=False, default=4)
args = parser.parse_args()


gods_list = ["Apholo", "Aphrodite", "Ares", "Artemis", "Athena", "Dionysus", "Hades", "Hera", "Hermes", "Poseidon", "Zeus"]
avaliable_gemini_models = ["gemini-1.5-turbo", "gemini-1.5-flash", "gemini-2.0-flash"]

if __name__ == "__main__" :
    import os
    from dotenv import load_dotenv
    load_dotenv()

    from prompt_toolkit import prompt
    from prompt_toolkit.completion import WordCompleter
    
    from lib.models import GlobalModel, colors
    from terminal.chat import chat
    from terminal.build_context import build_context_pt
    
    avaliable_model_types :list[str] = []
    
    if os.getenv("GOOGLE_API_KEY") is not None:
        avaliable_model_types.append("google")
    
    try:
        import ollama
        avaliable_ollama_models = [
            model.model for model in ollama.list().models
        ]
        avaliable_model_types.append("ollama")
    except:
        avaliable_ollama_models = []
    
    if not avaliable_ollama_models:
        raise ValueError("No available models found. Please install Ollama or check your installation or check your GOOGLE_API_KEY in .env.")
    
    types_completer = WordCompleter(avaliable_model_types, ignore_case=True)
    ollama_completer = WordCompleter(avaliable_ollama_models, ignore_case=True)
    gemini_completer = WordCompleter(avaliable_gemini_models, ignore_case=True)
    
    
    theme = input("Escolha o tema que será debatido: ")
    
    gods :list[GlobalModel] = []
    ideas :list[str] = []
    selected_gods :set[str] = set({})
    selected_colors :set[str] = set({})
    
    for i in range(1,3):
        print()
        gods_completer = WordCompleter(gods_list, ignore_case=True)
        god_name = prompt(f"Select an God: ", completer=gods_completer)
        gods_list.remove(god_name)
        model_type = prompt(f"Select a model type for {god_name}: ", completer=types_completer)
        model_name=prompt(f"Select a model name for {god_name}: ", completer=ollama_completer if model_type == "ollama" else gemini_completer)
        color_completer = WordCompleter(list(set(colors.keys()) - selected_colors), ignore_case=True)
        color = prompt(f"Select a color for {god_name}: ", completer=color_completer)
        selected_colors.add(color)
        ideas.append(prompt(f"Describe an idea for {god_name}: "))
        
        gods.append(GlobalModel(
            model_name=model_name,
            model_type=model_type,
            user_name=god_name,
            color=color
        ))
        
        print(f"God {i} ({gods[i-1].user_name}) is ready.")
    
    gods_str = []
    while gods_list:
        gods_completer = WordCompleter(gods_list + ["Exit"], ignore_case=True)
        god_name = prompt(f"Select a God to be the jury (type Exit to exit): ", completer=gods_completer)
        if god_name in gods_list:
            gods_list.remove(god_name)
            gods_str.append(god_name)
        elif god_name == "Exit":
            break
    
    if len(gods_str) < 0:
        raise ValueError("Insufficient Jury Gods. Please select at least one.")
    
    model_type = prompt(f"Select a model type for jury:", completer=types_completer)
    model_name=prompt(f"Select a model name for jury:", completer=ollama_completer if model_type == "ollama" else gemini_completer)
    color_completer = WordCompleter(list(set(colors.keys()) - selected_colors), ignore_case=True)
    color = prompt(f"Select a color for {god_name}: ", completer=color_completer)
    
    god1, god2, jury_dict, prompts = build_context_pt(
        gods[0], gods[1], gods_str, model_type, model_name, color, theme, ideas[0], ideas[1]   
    )
    
    chat(
        god1=god1, 
        god2=god2, 
        jury_dict=jury_dict, 
        supervisioned=args.supervisioned, 
        rounds=args.n_rounds, 
        prompts=prompts, 
        file=args.file, 
        file_type=args.file_type,
    )    