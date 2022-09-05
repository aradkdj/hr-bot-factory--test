from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Message(Base):
    id = Column(Integer, primary_key=True)
    response = Column(String, nullable=False)
    type = Column(String, nullable=False)
    origin_for = relationship(
        "Way", back_populates="origin_message", foreign_keys="Way.origin_message_id"
    )
    destination_for = relationship(
        "Way",
        back_populates="destination_message",
        foreign_keys="Way.destination_message_id",
    )

    __mapper_args__ = {"polymorphic_on": type}
