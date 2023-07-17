from typing import Optional
from pydantic import BaseModel


class WorkPlaceCreate(BaseModel):
    Name: str
    
    class Config:
        orm_mode = True
        
class WorkPlaceReturn(BaseModel):
    id:int
    Name: str
    
    class Config:
        orm_mode = True
        