from typing import Optional

from pydantic import BaseModel


# Shared properties
class LocationBase(BaseModel):
    location_code: str
    location_name: str


# Properties to receive on item creation
class LocationCreate(LocationBase):
    pass


# Properties to receive on item update
class LocationUpdate(LocationBase):
    pass


# Properties shared by models stored in DB
class LocationInDBBase(LocationBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Location(LocationInDBBase):
    pass


# Properties properties stored in DB
class LocationInDB(LocationInDBBase):
    pass
