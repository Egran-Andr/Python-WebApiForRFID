from sqlalchemy.orm import Session

from schemas.workuser import UserWorkplcaeCreate
from db.models.usersWorkplace import UserWorkplace
from db.models.workplace import WorkplaceList
from schemas.worklist import WorkPlaceReturn


def create_new_userwork_con(workplacecon:UserWorkplcaeCreate,db:Session):
    workplacecon = UserWorkplace(workerid=workplacecon.workerid,
    workplaceid=workplacecon.workplaceid
        )
    db.add(workplacecon)
    db.commit()
    db.refresh(workplacecon)
    return workplacecon
    
def update_user_workplace_con(id:int,workplaceid:int,db:Session):
    updated_workplace = db.query(UserWorkplace).filter(UserWorkplace.workerid == id)
    if not updated_workplace.first():
        return 0
    updated_workplace.update({"workerid":id,"workplaceid":workplaceid})
    db.commit()
    return 1
    
def get_users_workplace(id:int,db:Session):
    Item=db.query(WorkplaceList, WorkplaceList.id,WorkplaceList.Name).join(UserWorkplace,WorkplaceList.id==UserWorkplace.workplaceid).filter(UserWorkplace.workerid==id).first()
    if not Item:
        Item={"id":0,"Name":"Не назначено"}
    return Item