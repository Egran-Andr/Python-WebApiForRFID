from typing import Optional
from pydantic import BaseModel


#properties required during user creation
class BalanceCreate(BaseModel):
 balance:float
 workerid:int
 class Config:
    orm_mode = True