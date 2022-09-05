from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relation

from app.db.base_class import Base

if TYPE_CHECKING:
    from .message import Message  # noqa: F401


class Way(Base):
    id = Column(Integer, primary_key=True, index=True)
    origin_message_id = Column(Integer, ForeignKey("message.id"), nullable=False)
    origin_message = relation(
        "Message", back_populates="origin_for", foreign_keys=[origin_message_id]
    )
    destination_message_id = Column(Integer, ForeignKey("message.id"), nullable=False)
    destination_message = relation(
        "Message",
        back_populates="destination_for",
        foreign_keys=[destination_message_id],
    )
    condition = Column(String, nullable=False)
