from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

class WorkplaceList(Base):
    __tablename__ = "workplacelist"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String,nullable= False)