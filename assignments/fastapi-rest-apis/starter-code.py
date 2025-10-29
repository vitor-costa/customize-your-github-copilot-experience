from typing import Optional, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Exemplo - FastAPI")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# armazenamento em memória (id -> Item)
items: Dict[int, Item] = {}
next_id = 1


@app.get("/items")
def list_items():
    return list(items.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return items[item_id]


@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id
    # garantir id único mesmo se o cliente enviar um id
    item.id = next_id
    items[next_id] = item
    next_id += 1
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    item.id = item_id
    items[item_id] = item
    return item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    del items[item_id]
    return None


# Nota: rode com `uvicorn starter-code:app --reload`
