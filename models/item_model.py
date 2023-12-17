from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel): 
    name: str
    price: float
    is_offer: Union[bool, None] = None 