from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException

import uvicorn

app = FastAPI()
class request_obj(BaseModel):
    sensor1 : List[int]

class response_obj(BaseModel):
    predicted : bool

@app.post('/predict')
def predict(request :request_obj):
    if len(request.sensor1):
        pred = response_obj(predicted = True)
    else:
        pred = response_obj(predicted = False)
    return pred
    


if __name__ == "__main__":
    config = uvicorn.Config(app, port=5012, host = '192.168.1.11')
    server = uvicorn.Server(config)
    server.run()