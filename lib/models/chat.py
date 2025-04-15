from pydantic import BaseModel
from typing import List

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