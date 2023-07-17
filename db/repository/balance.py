from sqlalchemy.orm import Session
from schemas.balance import BalanceCreate
from db.models.userbalance import Balance




def create_new_balance(balance:BalanceCreate,db:Session):
    balance = Balance(workerid=balance.workerid,
        balance=balance.balance
        )
    db.add(balance)
    db.commit()
    db.refresh(balance)
    return balance

def update_balance_by_id(id:int,balance:float,db:Session):
    updated_balance = db.query(Balance).filter(Balance.workerid == id)
    if not updated_balance.first():
        return 0
    updated_balance.update({"balance":balance,"workerid":id})
    db.commit()
    return 1
    
def get_balance_all(db:Session):
    Item = db.query(Balance).all()
    return Item   
    
def get_balance_id(workerid:int,db:Session):
    Item = db.query(Balance).filter(Balance.workerid == workerid).first()
    return Item