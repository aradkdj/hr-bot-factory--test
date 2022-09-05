from pydantic import BaseModel


# Shared properties
class MessageBase(BaseModel):
    response: str | None = None


# Properties to receive via API on creation
class MessageCreate(MessageBase):
    response: str


# Properties to receive via API on update
class MessageUpdate(MessageBase):
    pass


# Properties shared by DB models
class MessageInDBBase(BaseModel):
    id: int
    response: str
    type: str

    class Config:
        orm_mode = True


# Additional properties to return via API
class Message(MessageInDBBase):
    pass


# Additional properties stored in DB
class MessageInDB(MessageInDBBase):
    pass
