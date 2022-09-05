from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Button(Base):
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    value = Column(String, nullable=False)
    type = Column(String, nullable=False)

    __mapper_args__ = {"polymorphic_on": type}
