from app.schemas.card import Card
from app.schemas.message import MessageBase, MessageInDBBase


# Shared properties
class CarouselMessageBase(MessageBase):
    pass


# Properties to receive via API on creation
class CarouselMessageCreate(CarouselMessageBase):
    response: str


# Properties to receive via API on update
class CarouselMessageUpdate(CarouselMessageBase):
    pass


# Properties shared by DB models
class CarouselMessageInDBBase(MessageInDBBase):
    class Config:
        orm_mode: True


# Additional properties to return via API
class CarouselMessage(CarouselMessageInDBBase):
    cards: list[Card]


# Additional properties stored in DB
class CarouselMessageInDB(CarouselMessageInDBBase):
    pass
