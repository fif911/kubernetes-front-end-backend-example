from typing import Optional

from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    title: Optional[str] = None
    checked: Optional[bool] = None


# Properties to receive on item creation
class ItemCreate(ItemBase):
    title: str
    checked: bool


# Properties to receive on item update
class ItemUpdate(ItemBase):
    pass


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int
    title: str
    checked: bool

    class Config:
        orm_mode = True


# Properties to return to client
class Item(ItemInDBBase):
    pass


# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    pass
