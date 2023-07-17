from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

class UserWorkplace(Base):
    __tablename__ = "userworkplace"

    workerid = Column(Integer, ForeignKey("users.id",ondelete='CASCADE'),nullable= False,primary_key=True)
    workplaceid=Column(Integer, ForeignKey("workplacelist.id"),nullable= False,primary_key=True)
    userworkplace = relationship("User",cascade="all,delete", back_populates="userworkcon")
