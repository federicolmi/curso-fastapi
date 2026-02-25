'''from fastapi import FastAPI

app = FastAPI()

cars_list = [
    {'car_name' : 'honda'},
    {'car_name' : 'vw'},
    {'car_name' : 'torino'},
    {'car_name' : 'vmw'}
]

@app.get('/cars/')
async def get_cars():
    return cars_list'''

# Esta es una forma de incorporar argumentos fuera de la ruta inicial, pero son obligatorios.
# La ruta se solicita: /cars/?skip=1&limit=2
from fastapi import FastAPI

app = FastAPI()

cars_list = [
    {'car_name' : 'honda'},
    {'car_name' : 'vw'},
    {'car_name' : 'torino'},
    {'car_name' : 'vmw'}
]

@app.get('/cars/')
# Esto pide cuantos salta (skip) y cuantos muestra (limt).Ejemp: 1/3 salta el primero y muestro los dos siguientes.
#  Se le puede agregar un valor por defecto: (skip: int = 0, limit: int = 1), lo que lo hace no obligatorio.
async def get_cars(skip: int, limit: int):
# Otra forma: return cars_list[skip: skip + limit] (1/2, salta uno pero muestra dos).
    return cars_list[skip: limit]

'''optional es solo un str para que suceda. Ej /cars/?optional=lachota. Puede valer un boll /?optional=true o /false
sync def get_cars(skip: int = 0, limit: int = 7, optional: str | None = None)
   if optional is not None:
      return {'cars_list': cars_list[0:1]}
'''