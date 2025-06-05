from fastapi import FastAPI
from repository.items import items
from model.item import Item

app = FastAPI()

@app.get("/")
async def my_endpoint():
    return {"message": "Hello World"}

@app.get("/items/{id}")
async def get_item_by_id(id: int) -> Item | None:
    return next((item for item in items if item.get("id") == id),None)
