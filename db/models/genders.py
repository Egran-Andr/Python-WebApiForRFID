from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Gender(Base):
    __tablename__ = "genders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    usergendercon = relationship("User", back_populates="usergender")