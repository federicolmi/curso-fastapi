from enum import Enum
from fastapi import FastAPI

class CarDealer(Enum):
    honda = 'autoshonda'
    bmw = 'autosbmw'
    ford = 'autosford'

app = FastAPI()
# Vale aclarar que como parametro ingreso el valor de la varable.
@app.get('/models/{car_dealer}')
async def get_models(car_dealer: CarDealer):
    if car_dealer == CarDealer.honda:
        return {'car_dealer': car_dealer, 'massage': 'es japones'}
    elif car_dealer ==  CarDealer.bmw:
        return {'car_dealer': car_dealer, 'message': 'es aleman'}
    else:
        return {'car_dealer': car_dealer, 'message': 'es americano'}
    
# Para ejecutar en terminal: fastapi dev .\nombre_de_archivo.