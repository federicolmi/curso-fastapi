from fastapi import FastAPI
# app es el objeto principal donde vas registrando rutas (/, /movies, etc.).
app = FastAPI()
# Lo que sigue es un decorador, y le dice a la fastapi,
# cuando alguien quiera tomar esta ruta mostra la siguiente pagina (http://127.0.0.1:8000/)
@app.get("/")
# async, es una funcion que se va a ejecutar una vez que peguen la ruta.
# root es solo un nombre que le asignaste vos a la funcion.
async def root():
    # retornas un dic de python que fastapi automaticamente la convierte en json.
    return {'massage': 'Hola Mundo!!!!'} 