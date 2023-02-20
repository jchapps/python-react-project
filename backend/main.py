from typing import List
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name="Josh", age=29),
    Person(id=2, name="Chappelow", age= 92),
    Person(id=3, name="Chris", age= 60)


]


# Remember to run uvicorn main:app --reload for serv and npm start for frontend

@app.get("/api")
def read_root():
    return DB


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
