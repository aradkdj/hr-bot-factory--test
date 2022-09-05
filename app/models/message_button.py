from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.models.button import Button

if TYPE_CHECKING:
    from .button_message import ButtonMessage  # noqa: F401


class MessageButton(Button):
    id = Column(
        Integer,
        ForeignKey("button.id", ondelete="CASCADE"),
        primary_key=True,
        index=True,
    )
    message_id = Column(Integer, ForeignKey("buttonmessage.id"))
    message = relationship("ButtonMessage", back_populates="buttons")

    __mapper_args__ = {"polymorphic_identity": "message button"}
