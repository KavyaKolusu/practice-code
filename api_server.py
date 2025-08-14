
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
@app.get("/api/hello")
def hello():
    return {"message": "Hello,Welcome to python server"}
class Item(BaseModel):
    name:str
    age:int
@app.post("/api/echo")
def echo(item: Item):
    return {"you_sent": item}
