from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()
class request_obj(BaseModel):
    sensor1 : List[int]

class response_obj(BaseModel):
    predicted : bool

@app.get('/')
async def read_root():
    return {"Hello": "World"}

@app.post('/predict')
async def predict(request :request_obj):
    if len(request.sensor1):
        pred = response_obj(predicted = True)
    else:
        pred = response_obj(predicted = False)
    return pred
    
