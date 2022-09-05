from pydantic import AnyHttpUrl

from app.schemas.message import MessageBase, MessageInDBBase


# Shared Properties
class TextMessageBase(MessageBase):
    image: AnyHttpUrl | None = None


# Properties to receive via API on creation
class TextMessageCreate(TextMessageBase):
    response: str


# Properties to receive via API on update
class TextMessageUpdate(TextMessageBase):
    pass


# Properties shared by DB models
class TextMessageInDBBase(MessageInDBBase):
    image: AnyHttpUrl | None

    class Config:
        orm_mode = True


# Additional properties to return via API
class TextMessage(TextMessageInDBBase):
    pass


# Additional properties stored in DB
class TextMessageInDB(TextMessageInDBBase):
    pass
