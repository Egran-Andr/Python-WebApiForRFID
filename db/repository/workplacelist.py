from sqlalchemy.orm import Session

from schemas.worklist import WorkPlaceCreate,WorkPlaceReturn
from db.models.workplace import WorkplaceList


def create_new_workplace(workplace:WorkPlaceCreate,db:Session):
    workplace = WorkplaceList(Name=workplace.Name
        )
    db.add(workplace)
    db.commit()
    db.refresh(workplace)
    return workplace

def get_list_workplaces(db:Session):
    Item = db.query(WorkplaceList).all()
    return Item

