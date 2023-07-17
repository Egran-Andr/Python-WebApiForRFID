from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.genders import GenderCreate
from db.session import get_db
from db.repository.genders import create_new_gender

router = APIRouter()


@router.post("/")
def create_gender(gender : GenderCreate,db: Session = Depends(get_db)):
    gender = create_new_gender(gender=gender,db=db)
    return gender 