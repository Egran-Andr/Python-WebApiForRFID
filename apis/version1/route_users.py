from fastapi import APIRouter,UploadFile, File
from datetime import datetime, date
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from fastapi.responses import FileResponse
from typing import List ,Optional
import asyncio
import aiofiles

from db.session import LocalImageStorage 

from schemas.users import UserCreate,HistoryCreate,CardUserConnect,ShowHistory,ShowUser,Image
from db.session import get_db
from db.repository.users import create_new_user,create_new_history,connect_new_card,get_user_history,get_user_byid,get_history_period,get_all_users,get_user_image,get_cards,update_user_by_id,delete_user_by_id,delete_card_by_name


router = APIRouter()


@router.post("/")
def create_user(user : UserCreate,db: Session = Depends(get_db)):
    user = create_new_user(user=user,db=db)
    return user 
    
@router.post("/historyadd")
def Create_new_field_in_user_history(history : HistoryCreate,db: Session = Depends(get_db)):
    history = create_new_history(history=history,db=db)
    return history 

@router.post("/cardconnect")
def conect_new_card_to_user(usercard : CardUserConnect,db: Session = Depends(get_db)):
    usercard = connect_new_card(usercard=usercard,db=db)
    return usercard

@router.post("/upload_image")
async def upload(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400,detail=f"File type of {file.content_type} is not supported")
    else: 
        try:
            async with aiofiles.open(LocalImageStorage+file.filename, 'wb') as f:
                contents = file.file.read()
                await f.write(contents)
        except Exception as inst:
            #raise HTTPException(status_code=507,detail=f"There was an error uploading the file")
            raise HTTPException(status_code=507,detail=type(inst))
    return {"message": f"Successfully uploaded {file.filename}"}

@router.get("/image")
def load_user_image(id:int,db:Session = Depends(get_db)):
    file = get_user_image(id=id,db=db)
    if file is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with this  id:{id} does not have image connected")
    else:
        try:
            res =LocalImageStorage+getattr(file, 'photopath')
        except AttributeError:
            res = ""
    if res ==LocalImageStorage:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with this  id:{id} does not have image connected")
    return FileResponse(res)

    
@router.get("/gethistory/{id}",response_model=List[ShowHistory])
def read_history(id:int,db:Session = Depends(get_db)):
    history = get_user_history(id=id,db=db)
    if history is None or len(history)==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"History with this user id:{id} does not exist")
    return history
    
@router.get("/user",response_model=ShowUser)
def get_user_info_byid(id:int= None,db:Session = Depends(get_db)):
    user = get_user_byid(id=id,db=db)
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with this id:{id} does not exist")
    return user
    
@router.get("/user/all",response_model=List[ShowUser])
def get_users(db:Session = Depends(get_db)):
    user = get_all_users(db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Error: No users in system")
    return user
    
    
@router.get("/cardlist/",response_model=List[CardUserConnect])
def get_user_cards(id:int=None,db:Session = Depends(get_db)):
    user = get_cards(id=id,db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Error: No users in system")
    return user

@router.get("/gethistory/{datebegin}/{dateend}",response_model=List[ShowHistory]) 
def read_history_in_period(datebegin:date,dateend:date,id:Optional[int]= None,db:Session = Depends(get_db)):
    history = get_history_period(id=id,datebegin=datebegin,dateend=dateend,db=db)
    if not history or len(history)==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Uneable to get history of this period")
    return history

@router.put("/update/{id}")   
def update_user(id: int,user : UserCreate,db: Session = Depends(get_db)):
    message = update_user_by_id(id=id,user=user,db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    return {"msg":"Successfully updated data."}

@router.delete("/delete/{id}")
def delete_user(id: int,db: Session = Depends(get_db)):
    message = delete_user_by_id(id=id,db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    return {"msg":"Successfully deleted."}
    
@router.delete("/deletecard/{cardnum}")
def delete_card(cardnum:str,db: Session = Depends(get_db)):
    message = delete_card_by_name(cardid=cardnum,db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"card with numer {cardnum} not found")
    return {"msg":"Successfully deleted."}