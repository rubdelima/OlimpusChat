from langchain_ollama.llms import OllamaLLM
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, AIMessage, BaseMessageChunk, BaseMessage
from langchain.base_language import BaseLanguageModel
from dotenv import load_dotenv
import warnings
import re
from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime

load_dotenv()
warnings.filterwarnings("ignore")

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

class God(BaseModel):
    name : str
    background_pt : str
    background_en : str
    image : str

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
    
class UserBase(BaseModel):
    username: str
    email: str
    password :str
    google_api_key : str


class User(UserBase):
    id: str
    chat_ids: Dict[str, str] = {}

class GodsChat(BaseModel):
    name : str
    content : str

class Chat(BaseModel):
    id: str
    user_id: str
    # last_change : datetime 
    
    theme: str
    rounds : int
    audio_mode : bool = False
    
    god1 : str
    god1_idea : str
    god1_type : str
    god1_model : str
    
    god2 : str
    god2_idea : str
    god2_type : str
    god2_model : str
    
    gods : List[str]
    gods_type : str
    
    
    chat : List[GodsChat]