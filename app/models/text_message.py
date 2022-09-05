from sqlalchemy import Column, ForeignKey, Integer, String

from app.models.message import Message


class TextMessage(Message):
    id = Column(
        Integer,
        ForeignKey("message.id", ondelete="CASCADE"),
        primary_key=True,
        index=True,
    )
    image = Column(String)

    __mapper_args__ = {"polymorphic_identity": "text message"}
