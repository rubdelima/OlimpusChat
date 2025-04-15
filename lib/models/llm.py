from langchain_ollama.llms import OllamaLLM
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, AIMessage, BaseMessageChunk, BaseMessage
from langchain.base_language import BaseLanguageModel
import re

colors = {
    "reset": "\033[0m",
    "bold": "\033[1m", 
    "reverse": "\033[7m",
    "black": "\033[30m", 
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m", 
    "blue": "\033[34m", 
    "magenta": "\033[35m",
    "cyan": "\033[36m", 
    "white":"\033[37m",
}


class GlobalModel():
    llm : BaseLanguageModel
    def __init__(self, model_name: str, model_type: str, user_name: str, messages: list[BaseMessage] = [], temperature: float = 0.2, color: str = "blue"):
        self.model_name = model_name
        self.model_type = model_type
        self.user_name = user_name
        self.color = color
        self.temperature = temperature
        self.messages :list[BaseMessage] = messages
        
        if model_type == "ollama":
            self.llm = OllamaLLM(model=model_name, temperature=temperature)
        elif model_type == "google":
            self.llm = ChatGoogleGenerativeAI(model=model_name, temperature=temperature)
        else:
            raise ValueError("Invalid model type. Choose 'ollama' or 'google'.")
        
    def chat(self):
        stream = self.llm.stream(self.messages)
        print()
        print(f"\033[7m\033[1m{self.user_name} ({self.model_name}):\033[0m{colors.get(self.color, '\033[0m')}")
        response = ""
        for chunk in stream:
            if isinstance(chunk, BaseMessageChunk):
                chunk = chunk.content
            response += str(chunk)
            print(chunk, end='', flush=True)
        print("\033[0m")
            
        
        response = re.sub(r"<think>.*?</think>", "", response)
        self.messages.append(AIMessage(content=response))
        return response