from pydantic import AnyHttpUrl

from app.schemas.button import Button
from app.schemas.message import MessageBase, MessageInDBBase


# Shared properties
class ButtonMessageBase(MessageBase):
    image: AnyHttpUrl | None = None


# Properties to receive via API on creation
class ButtonMessageCreate(ButtonMessageBase):
    response: str


# Properties to receive via API on update
class ButtonMessageUpdate(ButtonMessageBase):
    pass


# Properties shared by DB models
class ButtonMessageInDBBase(MessageInDBBase):
    image: AnyHttpUrl | None

    class Config:
        orm_mode: True


# Additional properties to return via API
class ButtonMessage(ButtonMessageInDBBase):
    buttons: list[Button]


# Additional properties stored in DB
class ButtonMessageInDB(ButtonMessageInDBBase):
    pass
