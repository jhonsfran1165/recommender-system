from typing import Optional
from pydantic import BaseModel


# Shared properties
class CopyTransactionBase(BaseModel):
    trans_date_id: int
    trans_type_id: int
    trans_borrower_code: int
    trans_location_code_id: int
    trans_tittle_code_id: int
    trans_copy_code_id: int
    trans_borrower_deleted: int


# Properties to receive on item creation
class CopyTransactionCreate(CopyTransactionBase):
    pass

# Properties to receive on item update
class CopyTransactionUpdate(CopyTransactionBase):
    pass


# Properties shared by models stored in DB
class CopyTransactionInDBBase(CopyTransactionBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Properties to return to client
class CopyTransaction(CopyTransactionInDBBase):
    pass


# Properties properties stored in DB
class CopyTransactionInDB(CopyTransactionInDBBase):
    pass
