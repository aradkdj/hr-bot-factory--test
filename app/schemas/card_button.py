from app.schemas.button import ButtonBase, ButtonInDBBase


# Shared properties
class CardButtonBase(ButtonBase):
    pass


# Properties to receive on creation
class CardButtonCreate(CardButtonBase):
    text: str
    value: str


# Properties to receive via API on update
class CardButtonUpdate(CardButtonBase):
    pass


# Properties shared by DB models
class CardButtonInDBBase(ButtonInDBBase):
    class Config:
        or_mode = True


# Additional properties to return via API
class CardButton(CardButtonInDBBase):
    pass


# Additional properties stored in DB
class CardButtonInDB(CardButtonInDBBase):
    card_id: int
