from fastapi import FastAPI
from enum import Enum # 리스트를 딕셔너리처럼 집합으로 만들어줌 >> 직관적임

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "INGYUWORLD HI"}

@app.post("/items/")
async def create_item(item : None):
    return item

@app.get("/user/{user_id}")
async def user(user_id : str):
    if user_id == "me":
        return {"Current User" : "킹갓최인규"}
    else:
        return {"Current User" : user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def readfile(file_path : str):
    return {"File_path" : file_path, "Message" : "씨발"}

@app.get("/jot")
async def jot(skip : int = 0, limit : int = 10):
    return fake_items_db[skip : skip + limit]
