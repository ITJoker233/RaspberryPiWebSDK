import uvicorn
from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr

app = FastAPI()

_version_ = '1.0.0'

class baseRequest(BaseModel):
    num: Optional[int] = None
    ioType:str
    key:str
    status: bool

class baseResponse(BaseModel):
    detail:str
    data:str
    message:str
    status: int
    timestamp: datetime

response = {
    'root':{'data':f'Raspberry Pi Web SDK {_version_} Look at /docs','detail':'','message':'Success','status':1},
    'version':{'data':f'Raspberry Pi Web SDK {_version_}','detail':'','message':'Success','status':1},
    'status':{'data':'','detail':'','message':'','status':0},
}

@app.get("/",response_model=baseResponse)
async def root():
    return JSONResponse(response['root'])

@app.get("/version",response_model=baseResponse)
async def version():
    return JSONResponse(response['version'])
    

@app.get('/status/{gpio_id}',response_model=baseResponse)
async def read_item(gpio_id: int):
    response_ = response['status']
    response_['data']
    response_['message']
    response_['status']
    return JSONResponse(response_)


#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=80,debug=True)