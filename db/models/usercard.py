from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class UserCard(Base):
    __tablename__ = "RFID_cards"
    RFID_CardNumber = Column(String, primary_key=True)
    Userid = Column(Integer, ForeignKey("users.id",ondelete='CASCADE'))
    cardholder = relationship("User",cascade="all,delete", back_populates="carduser")
