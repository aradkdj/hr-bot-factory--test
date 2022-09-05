from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .message import Message

if TYPE_CHECKING:
    from .message_button import MessageButton  # noqa: F401


class ButtonMessage(Message):
    id = Column(
        Integer,
        ForeignKey("message.id", ondelete="CASCADE"),
        primary_key=True,
    )
    image = Column(String)
    buttons = relationship("MessageButton", back_populates="message")

    __mapper_args__ = {"polymorphic_identity": "button message"}
