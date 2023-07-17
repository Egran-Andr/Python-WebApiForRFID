from typing import Optional
from pydantic import BaseModel


#properties required during user creation
class GenderCreate(BaseModel):
 title:str