from typing import Optional
from pydantic import BaseModel


# Shared properties
class RuleBase(BaseModel):
    antecedent_support: Optional[float] = None
    consequent_support: Optional[float] = None
    support: Optional[float] = None
    confidence: Optional[float] = None
    lift: Optional[float] = None
    leverage: Optional[float] = None
    conviction: Optional[float] = None


# Properties to receive on item creation
class RuleCreate(RuleBase):
    id: int
    antecedents: int
    consequents: int


# Properties to receive on item update
class RuleUpdate(RuleBase):
    pass


# Properties shared by models stored in DB
class RuleInDBBase(RuleBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Rule(RuleInDBBase):
    pass


# Properties properties stored in DB
class RuleInDB(RuleInDBBase):
    pass
