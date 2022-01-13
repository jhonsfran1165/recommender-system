from app.crud.base import CRUDBase
from app.models import TransactionType
from app.schemas import TransactionTypeCreate, TransactionTypeUpdate


from typing import Any, Optional, TypeVar
from sqlalchemy.orm import Session
from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDTransactionType(CRUDBase[TransactionType, TransactionTypeCreate, TransactionTypeUpdate]):
    def get_by_code(self, db: Session, trans_type_code: str) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.trans_type_code == trans_type_code).first()


transaction_type = CRUDTransactionType(TransactionType)
