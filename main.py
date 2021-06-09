from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class ItemModel(BaseModel):
    name: str
    price: float
    apply_offer: Optional[bool] = None

@app.get('/')
async def entry_point():
    return {'Hello': 'World'}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemModel):
    return {
        'item_name': item.name,
        'item_ide': item_id
    }