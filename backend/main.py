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
    Person(id=2, name="Chappelow", age= 92)

]


@app.get("/api")
def read_root():
    return DB


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
