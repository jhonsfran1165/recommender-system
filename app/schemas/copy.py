from typing import Optional
from pydantic import BaseModel


# Shared properties
class CopyBase(BaseModel):
    title_id: Optional[int] = None
    medium_type: Optional[str] = None
    author_name: Optional[str] = None
    pr_classmark: Optional[str] = None
    shelfmark: Optional[str] = None
    bar_code: Optional[str] = None
    location: Optional[str] = None


# Properties to receive on item creation
class CopyCreate(CopyBase):
    id: int
    copy_title: str


# Properties to receive on item update
class CopyUpdate(CopyBase):
    copy_title: str


# Properties shared by models stored in DB
class CopyInDBBase(CopyBase):
    id: Optional[str] = None
    copy_title: Optional[str] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Copy(CopyInDBBase):
    pass


# Properties properties stored in DB
class CopyInDB(CopyInDBBase):
    pass
