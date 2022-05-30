from fastapi import FastAPI

# Import Union since our Item object will have tags thate can be string or a list
from typing import Union
# BaseModel from Pydantic is used to define data objects
from pydantic import BaseModel

# Declare the data object with its componentes and theis type.
class Url(BaseModel):
    url: str

# Instantiate the app.
app = FastAPI()

# Define a GET on the specified endpoint.
@app.get("/test/{url}")
async def test_url(url: str):
    retorno = url + "_olha_"
    return retorno