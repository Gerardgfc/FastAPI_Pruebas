from typing import Union
from fastapi import FastAPI
from models.item_model import Item

# Creacion de Aplicacion FastAPI
app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello' : 'Word!'}

@app.get('/hola')
def read_root():
    return {'Hola' : 'Mundo!'}


@app.get('/calculadora')
def calcular(num1: int, num2: int):
    return {'suma': num1 + num2}

#solicitud de tipo PUT
#PUT = Actualizar
#POST = Crear


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    """_summary_

    Args:
        item_id: Este objeto es de tipo int e indica que es obligatorio ya que no esta acompañado de None.
        
        q: En este caso el None indica que no es de caracter obligatorio y el none al que esta igualdo indica que por defecto el valor es None.

    Returns:
        El id (obligatorio) y el "q" que no es obligatorio.
    """
    return {'item_id': item_id, 'q': q}

#Actualizacion de item_id
@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    """esta funcion retorna un producto con los datos que soliciten, se puede escalar para hacer que diga si un producto se encuntra en oferta o no

    Args:
        item_id (int): id del producto
        
        item (Item): nombre del producto

    Returns:
        _type_: retorna el nombre del producto y su id
    """
    return {'item_name': item.name, 'item_id': item_id,'item_price': item.price, 'item_offer': item.is_offer}
