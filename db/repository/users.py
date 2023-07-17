from sqlalchemy.orm import Session
from datetime import datetime, date

from schemas.users import UserCreate,HistoryCreate,CardUserConnect,ShowUser
from db.models.users import User
from db.models.workerhistory import UserHistory
from db.models.usercard import UserCard

def create_new_user(user:UserCreate,db:Session):
    user = User(Name=user.Name,
        Surname=user.Surname,
        lastname=user.lastname,
        birthdate=user.birthdate,
        gender=user.gender,
        photopath=user.photopath
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
    
def create_new_history(history:HistoryCreate,db:Session):
    history = UserHistory(
    workerid=history.workerid,
    workplaceid=history.workplaceid,
    entertimestamp=datetime.strptime(history.entertimestamp, '%Y-%m-%d %H:%M:%S'))
    db.add(history)
    db.commit()
    db.refresh(history)
    return history
    
def connect_new_card(usercard:CardUserConnect,db:Session):
    usercard = UserCard(
    RFID_CardNumber=usercard.RFID_CardNumber,
    Userid=usercard.Userid)
    db.add(usercard)
    db.commit()
    db.refresh(usercard)
    return usercard
    
def get_all_users(db:Session):
    Item = db.query(User).all()
    return Item
    
def get_user_image(id:int,db:Session):
    Item = db.query(User.photopath).filter(User.id == id).first()
    return Item   

def get_user_byid(id:int,db:Session):
    Item = db.query(User).filter(User.id == id).first()
    return Item

def get_user_history(id:int,db:Session):
    Item = db.query(UserHistory).filter(UserHistory.workerid == id).all()
    return Item
    
def get_history_period(id:int,datebegin:date,dateend:date,db:Session):
    if not id:
        Item = db.query(UserHistory).filter(UserHistory.entertimestamp >= datebegin,UserHistory.entertimestamp <= dateend).order_by(UserHistory.entertimestamp.desc()).all()
    else:
        Item = db.query(UserHistory).filter(UserHistory.workerid == id,UserHistory.entertimestamp >= datebegin,UserHistory.entertimestamp <= dateend).order_by(UserHistory.entertimestamp.desc()).all()
    return Item

def get_cards(id:int,db:Session):
    if not id:
        Item = db.query(UserCard).all()
    else:
        Item = db.query(UserCard).filter(UserCard.Userid==id).all()
    return Item
    
def update_user_by_id(id:int, user: UserCreate,db: Session):
    updated_user = db.query(User).filter(User.id == id)
    if not updated_user.first():
        return 0
    updated_user.update(user.__dict__)
    db.commit()
    return 1
    
def delete_user_by_id(id:int,db: Session):
    existing_user = db.query(User).filter(User.id == id)
    if not existing_user.first():
        return 0
    existing_user.delete(synchronize_session=False)
    db.commit()
    return 1
    
def delete_card_by_name(cardid:str,db: Session):
    existing_card = db.query(UserCard).filter(UserCard.RFID_CardNumber == cardid)
    if not existing_card.first():
        return 0
    existing_card.delete(synchronize_session=False)
    db.commit()
    return 1