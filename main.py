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


@app.put('/items/{item_id}')

#Creacion de modelo de datos
def update_item(item_id: int, item: Item):
    """esta funcion retorna un producto con los datos que soliciten, se puede escalar para hacer que diga si un producto se encuntra en oferta o no

    Args:
        item_id (int): id del producto
        
        item (Item): nombre del producto

    Returns:
        _type_: retorna el nombre del producto y su id
    """
    return {'item_name': item.name, 'item_id': item_id,'item_price': item.price, 'item_offer': item.is_offer}
