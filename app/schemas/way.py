from pydantic import BaseModel


# Shared properties
class WayBase(BaseModel):
    origin_message_id: int | None = None
    destination_message_id: int | None = None
    condition: str | None = None


# Properties to receive via API on creation
class WayCreate(WayBase):
    origin_message_id: int
    destination_message_id: int
    condition: str


# Properties to receive via API on update
class WayUpdate(WayBase):
    pass


# Properties shared by DB models
class WayInDBBase(BaseModel):
    id: int
    origin_message_id: int
    destination_message_id: int
    condition: str

    class Config:
        orm_mode = True


# Additional properties to return via API
class Way(WayInDBBase):
    pass


# Additional properties stored in DB
class WayInDB(WayInDBBase):
    pass
