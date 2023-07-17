from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship

from db.base_class import Base


class UserHistory(Base):
    __tablename__ = "history"

    workerid=Column(Integer, ForeignKey("users.id",ondelete='CASCADE'),nullable= False,primary_key=True)
    workplaceid=Column(Integer, ForeignKey("workplacelist.id"),nullable= False,primary_key=True)
    entertimestamp=Column(DateTime(timezone=False),nullable= False,primary_key=True)
    userhistory = relationship("User",cascade="all,delete", back_populates="userhistorycon")