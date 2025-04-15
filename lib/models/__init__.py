from pydantic import BaseModel
from .llm import GlobalModel, colors
from .chat import GodsChat, Chat
from .user import User, UserBase

class God(BaseModel):
    name : str
    background_pt : str
    background_en : str
    image : str
