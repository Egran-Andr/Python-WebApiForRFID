from fastapi import APIRouter, Query,FastAPI
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List ,Optional

from schemas.worklist import WorkPlaceCreate,WorkPlaceReturn
from db.session import get_db
from db.repository.workplacelist import create_new_workplace,get_list_workplaces

router = APIRouter()


@router.post("/",response_model=WorkPlaceCreate)
def create_workplace(workplace : WorkPlaceCreate,db: Session = Depends(get_db)):
    workplace = create_new_workplace(workplace=workplace,db=db)
    return workplace

@router.get("/all",response_model=List[WorkPlaceReturn])
def get_workplace_list(db:Session = Depends(get_db)):
    worlplacelist = get_list_workplaces(db=db)
    if not worlplacelist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Error: No workplaces in system.Please create workspace!")
    return worlplacelist    
