from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String,nullable= False)
    Surname = Column(String,nullable= False)
    lastname = Column(String)
    birthdate= Column(Date,nullable= False)
    gender = Column(Integer, ForeignKey("genders.id"))
    photopath=Column(String)
    
    carduser = relationship("UserCard", cascade="all,delete-orphan",back_populates="cardholder")
    userbalance = relationship("Balance",cascade="all,delete-orphan", back_populates="balanceholder")
    usergender = relationship("Gender", back_populates="usergendercon")
    userworkcon = relationship("UserWorkplace",cascade="all,delete-orphan" ,back_populates="userworkplace")
    userhistorycon = relationship("UserHistory",cascade="all,delete-orphan", back_populates="userhistory")