from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.models.message import Message

if TYPE_CHECKING:
    from .card import Card  # noqa: F401


class CarouselMessage(Message):
    id = Column(
        Integer,
        ForeignKey("message.id", ondelete="CASCADE"),
        primary_key=True,
        index=True,
    )
    cards = relationship("Card", back_populates="message")

    __mapper_args__ = {"polymorphic_identity": "carousel message"}
