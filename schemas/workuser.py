from typing import Optional
from pydantic import BaseModel


#properties required during user creation
class UserWorkplcaeCreate(BaseModel):
    workerid: int
    workplaceid:int