from pydantic import BaseModel
from typing import Dict

class UserBase(BaseModel):
    username: str
    email: str
    password :str
    google_api_key : str

class User(UserBase):
    id: str
    chat_ids: Dict[str, str] = {}