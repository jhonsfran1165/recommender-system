from pydantic import BaseModel


# Shared properties
class TransactionTypeBase(BaseModel):
    pass


# Properties to receive on item creation
class TransactionTypeCreate(TransactionTypeBase):
    trans_type_code: str
    trans_type_description: str


# Properties to receive on item update
class TransactionTypeUpdate(TransactionTypeBase):
    trans_type_code: str
    trans_type_description: str


# Properties shared by models stored in DB
class TransactionTypeInDBBase(TransactionTypeBase):
    id: int
    trans_type_code: str
    trans_type_description: str

    class Config:
        orm_mode = True


# Properties to return to client
class TransactionType(TransactionTypeInDBBase):
    pass


# Properties properties stored in DB
class TransactionTypeInDB(TransactionTypeInDBBase):
    pass
