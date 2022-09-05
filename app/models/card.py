from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .carousel_message import CarouselMessage  # noqa: F401


class Card(Base):
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String, nullable=False)
    text = Column(String, nullable=False)
    message_id = Column(Integer, ForeignKey("carouselmessage.id"))
    message = relationship("CarouselMessage", back_populates="cards")
    buttons = relationship("CardButton", back_populates="card")
