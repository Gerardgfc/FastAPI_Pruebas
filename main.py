from typing import Union
from fastapi import FastAPI

# Creacion de Aplicacion FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello' : 'Word!'}

@app.get('/hola')
def read_root():
    return {'Hola' : 'Mundo!'}