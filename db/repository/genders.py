from sqlalchemy.orm import Session
from schemas.genders import GenderCreate
from db.models.genders import Gender



def create_new_gender(gender:GenderCreate,db:Session):
    gender = Gender(title=gender.title,
        )
    db.add(gender)
    db.commit()
    db.refresh(gender)
    return gender