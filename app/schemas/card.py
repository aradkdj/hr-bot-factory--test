from pydantic import AnyHttpUrl, BaseModel

from app.schemas.card_button import CardButton


# Shared properties
class CardBase(BaseModel):
    image: AnyHttpUrl | None = None
    text: str | None = None


# Properties to receive via API on creation
class CardCreate(CardBase):
    image: AnyHttpUrl
    text: str


# Properties to receive via API on update
class CardUpdate(CardBase):
    pass


# Properties shared by DB models
class CardInDBBase(BaseModel):
    id: int
    image: str
    text: str
    message_id: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class Card(CardInDBBase):
    buttons: list[CardButton]


# Additional properties stored in DB
class CardInDB(CardInDBBase):
    pass
