from fastapi import FastAPI

app = FastAPI()

@app.get('/books/{book_id}')
# Por defecto si async def get_book(book_id): no le asignamos el valor de int muestra una list con un str.
async def get_book(book_id):
    return {'book_id': {book_id}}
# Si queremos que retorne un int le asignamos el valor int.
#async def get_book(book_id: int):
     # return {'book_id' : '{book_id}'}