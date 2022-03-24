from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


app = FastAPI()




@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[int] = None):
    q = item_id + 10
    return {"item_id": item_id, "q": q}


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax > 0:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/items_query/")
async def create_items_query(skip: int = 0, limit: int = 10):
    return skip + limit

@app.get("/items_query_func/")
async def create_q_func(q: Optional[str]):
    return q


