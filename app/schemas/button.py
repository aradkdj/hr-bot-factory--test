from pydantic import BaseModel


# Shared properties
class ButtonBase(BaseModel):
    text: str | None = None
    value: str | None = None


# Properties to receive on creation
class ButtonCreate(ButtonBase):
    text: str
    value: str


# Properties to receive via API on update
class ButtonUpdate(ButtonBase):
    pass


# Properties shared by DB models
class ButtonInDBBase(BaseModel):
    id: int
    text: str
    value: str
    type: str

    class Config:
        orm_mode = True


# Additional properties to return via API
class Button(ButtonInDBBase):
    pass


# Additional properties stored in DB
class ButtonInDB(ButtonInDBBase):
    pass
