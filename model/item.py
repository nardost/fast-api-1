
from pydantic import BaseModel
from model.genre import Genre

class Item(BaseModel):
    id: int
    genre: Genre
    title: str
    price: float
    author: str | None = None
