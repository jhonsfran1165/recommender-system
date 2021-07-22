from typing import Optional
from pydantic import BaseModel


# Shared properties
class TitleBase(BaseModel):
    subtitle: Optional[str] = None


# Properties to receive on item creation
class TitleCreate(TitleBase):
    id: int
    title_name: str


# Properties to receive on item update
class TitleUpdate(TitleBase):
    title_name: str


# Properties shared by models stored in DB
class TitleInDBBase(TitleBase):
    id: int
    title_name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Title(TitleInDBBase):
    pass


# Properties properties stored in DB
class TitleInDB(TitleInDBBase):
    pass
