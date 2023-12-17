from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# Creacion de Aplicacion FastAPI

app = FastAPI()

class Item(BaseModel): 
    name: str
    price: float
    is_offer: Union[bool, None] = None 

@app.get('/')
def read_root():
    return {'Hello' : 'Word!'}

@app.get('/hola')
def read_root():
    return {'Hola' : 'Mundo!'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}

@app.get('/calculadora')

def calcular(num1: int, num2: int):
    return {'suma': num1 + num2}

#solicitud de tipo PUT
#PUT = Actualizar
#POST = Crear
