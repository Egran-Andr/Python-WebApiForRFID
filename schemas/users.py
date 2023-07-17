from typing import Optional,Dict
from datetime import datetime, date
from pydantic import BaseModel,validator


#properties required during user creation
class UserCreate(BaseModel):
    Name: str
    Surname:str
    lastname:Optional[str]
    birthdate:date
    @validator("birthdate", pre=True)
    def parse_birthdate(cls, value):
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()
    gender:int
    photopath:Optional[str]
    
    class Config:
        orm_mode = True
    
class HistoryCreate(BaseModel):
    workerid: Optional[int]
    workplaceid:int
    entertimestamp:str
    
    class Config:
        orm_mode = True
    
class CardUserConnect(BaseModel):
    Userid:int
    RFID_CardNumber: str
    
    class Config:
        orm_mode = True
    
class ShowHistory(HistoryCreate):
    workerid: int 
    workplaceid:int
    entertimestamp:datetime
    
class Image(BaseModel):
    photopath:str

    class Config:
        orm_mode = True
    
class ShowUser(BaseModel):
    id:int
    Name: str
    Surname:str
    lastname:str
    birthdate:date
    gender:int
    photopath:str
    
    class Config:
        orm_mode = True
