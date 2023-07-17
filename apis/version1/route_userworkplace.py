from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import Depends,HTTPException,status
from typing import List ,Optional

from schemas.workuser import UserWorkplcaeCreate
from schemas.worklist import WorkPlaceReturn
from db.session import get_db
from db.repository.workeruser import create_new_userwork_con,update_user_workplace_con,get_users_workplace

router = APIRouter()


@router.post("/")
def Create_conection_User_and_Workplace(workplacecon : UserWorkplcaeCreate,db: Session = Depends(get_db)):
    workplacecon = create_new_userwork_con(workplacecon=workplacecon,db=db)
    return workplacecon 
    
@router.put("/update/{id}/{workplaceid}")   
def update_user_workplace(id:int,workplaceid:int,db: Session = Depends(get_db)):
    message = update_user_workplace_con(id=id,workplaceid=workplaceid,db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    return {"msg":"Successfully updated data."}
    
@router.get("/{id}",response_model=WorkPlaceReturn) 
def get_user_workplace(id:int,db:Session = Depends(get_db)):
    userworkplace = get_users_workplace(id=id,db=db)
    if not userworkplace:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Uneable to get info")
    return userworkplace