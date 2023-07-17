from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import Depends,HTTPException,status
from typing import List

from schemas.balance import BalanceCreate
from db.session import get_db
from db.repository.balance import create_new_balance,update_balance_by_id,get_balance_id,get_balance_id,get_balance_all

router = APIRouter()


@router.post("/")
def create_balance(balance : BalanceCreate,db: Session = Depends(get_db)):
    balance = create_new_balance(balance=balance,db=db)
    return balance

@router.put("/update/{id}/{balance}")   
def update_balance(id:int,balance:float,db: Session = Depends(get_db)):
    message = update_balance_by_id(id=id,balance=balance,db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    return {"msg":"Successfully updated data."}
    
@router.get("/all",response_model=List[BalanceCreate])
def get_balance_list(db:Session = Depends(get_db)):
    balance = get_balance_all(db=db)
    if not balance :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"balance with this id:{id} does not exist")
    return balance    
    
@router.get("/by_id",response_model=BalanceCreate)
def get_balance_info_byid(id:int,db:Session = Depends(get_db)):
    balance = get_balance_id(workerid=id,db=db)
    if not balance :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"balance with this id:{id} does not exist")
    return balance