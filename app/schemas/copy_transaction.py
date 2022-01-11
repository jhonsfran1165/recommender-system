from typing import Optional
from pydantic import BaseModel


# Shared properties
class CopyTransactionBase(BaseModel):
    trans_type: str
    trans_borrower_code: str
    trans_location_code: str
    trans_tittle_code: int
    trans_copy_code: int
    trans_borrower_deleted: int


# Properties to receive on item creation
class CopyTransactionCreate(CopyTransactionBase):
    id: int
    trans_date: str


# Properties to receive on item update
class CopyTransactionUpdate(CopyTransactionBase):
    trans_date: str


# Properties shared by models stored in DB
class CopyTransactionInDBBase(CopyTransactionBase):
    id: int
    trans_date: str

    class Config:
        orm_mode = True


# Properties to return to client
class CopyTransaction(CopyTransactionInDBBase):
    pass


# Properties properties stored in DB
class CopyTransactionInDB(CopyTransactionInDBBase):
    pass
