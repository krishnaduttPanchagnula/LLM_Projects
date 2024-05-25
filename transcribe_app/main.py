from .utills import *
from fastapi import FastAPI,JsonResponse 
from typing import List
from pydantic import BaseModel



app = FastAPI()

class Filenames(BaseModel):
    filenames: List[str]

@app.post("/test")
async def test(filenames: Filenames):
    
    for i in filenames["filenames"]:
        transcribe(i)
    return {"status": "Sucessfully transcribed all the files"}



    
