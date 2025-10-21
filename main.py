from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Colors(BaseModel):
    list_colors: list[

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Gridspiration"}

