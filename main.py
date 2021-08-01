from typing import Optional
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class ModelName(str, Enum):
    rafael = "rafael"
    luan = "luan"

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
async def read_root():
    return {"Hello":"World"}

#this example skip and limit is not required and default 0
@app.get("/items/")
async def read_items(skip: int=0, limit: int=0):
    return fake_items_db[skip: skip+limit]

@app.get("/need/{item_id}")
async def need_items(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id":item_id, "q":q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name":item.name, 
            "item_price":item.price,
            "is_offer":item.is_offer,
            "item_id":item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if(model_name == ModelName.luan):
        return {"model_name":model_name, "message":"olha seu nome é luan!"}
    if(model_name.value == ModelName.rafael):
        return {"model_name":model_name, "message": "olha seu nome é rafael"}
    
    return {"model_name":"não achei", "message":"não achei nada"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}