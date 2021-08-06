from typing import Optional
from datetime import date

from pydantic import BaseModel


# Shared properties
class DateBase(BaseModel):
    date: date
    date_format: str
    day_week: int
    day_name: str
    day_month: int
    day_year: int
    month: int
    month_name: str
    month_number_days: int
    week: int
    quarter: int
    year: int
    semester: int


# Properties to receive on item creation
class DateCreate(DateBase):
    id: Optional[int] = None


# Properties to receive on item update
class DateUpdate(DateBase):
    pass


# Properties shared by models stored in DB
class DateInDBBase(DateBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Date(DateInDBBase):
    pass


# Properties properties stored in DB
class DateInDB(DateInDBBase):
    pass
