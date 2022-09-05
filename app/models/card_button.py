from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.models.button import Button

if TYPE_CHECKING:
    from .card import Card  # noqa: F401


class CardButton(Button):
    id = Column(
        Integer,
        ForeignKey("button.id", ondelete="CASCADE"),
        primary_key=True,
        index=True,
    )
    card_id = Column(Integer, ForeignKey("card.id"))
    card = relationship("Card", back_populates="buttons")

    __mapper_args__ = {"polymorphic_identity": "card button"}
