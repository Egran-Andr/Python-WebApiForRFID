from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Numeric
from sqlalchemy.orm import relationship

from db.base_class import Base

class Balance(Base):
    __tablename__ = "balance"

    workerid = Column(Integer, ForeignKey("users.id",ondelete='CASCADE'),nullable= False,primary_key=True)
    balance=Column(Numeric(12, 2),nullable= False,default=0.0)
    balanceholder = relationship("User",cascade="all,delete", back_populates="userbalance")