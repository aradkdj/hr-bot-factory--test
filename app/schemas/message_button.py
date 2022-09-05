from app.schemas.button import ButtonBase, ButtonInDBBase


# Shared properties
class MessageButtonBase(ButtonBase):
    pass


# Properties to receive on creation
class MessageButtonCreate(MessageButtonBase):
    text: str
    value: str


# Properties to receive via API on update
class MessageButtonUpdate(MessageButtonBase):
    pass


# Properties shared by DB models
class MessageButtonInDBBase(ButtonInDBBase):
    class Config:
        or_mode = True


# Additional properties to return via API
class MessageButton(MessageButtonInDBBase):
    pass


# Additional properties stored in DB
class MessageButtonInDB(MessageButtonInDBBase):
    message_id: int
