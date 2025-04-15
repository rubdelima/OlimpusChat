from pydantic import BaseModel

class God(BaseModel):
    name : str
    background_pt : str
    background_en : str
    image : str